#Imports==================================================
import re
from github import Github
#Functions================================================
''' Returns info on users repos '''
def getRepoDetails(user):

    if user is None:
        return 'No User Provided'

    output = 'UserName: %s, Name: %s\n' % (g.get_user().login, g.get_user().name)
    
    output += 'Repositories:\n'
    for repo in g.get_user().get_repos():
        output +=   '''
        Name: %s,
            Topics: %s,
            Branches: %s,
            Number of Commits: %d,
            Number of Contribuators %d,
            Number of Stars %d
                    ''' % (
                        repo.name, repo.get_topics(), list(repo.get_branches()),
                        len(list(repo.get_commits())), len(list(repo.get_collaborators())), 
                        repo.stargazers_count)
        #print('Repo: %s, Toppics: %s' % (repo.name, repo.get_topics()))

    return output

''' Gets the language breakdown of all repos
    and each individual repo '''
def getLangSkills(user):

    if user == None:
        return None

    #Map for file extentions to programing language
    proLang = {
        '.ML' :	'ML',
        '.CS' : 'C#',
        '.HPP':	'C++',
        '.CLASS' : 'Java',
        '.CPP' : 'C++',
        '.ERB' : 'Ruby',
        '.CP' : 'C++',
        '.MF' : 'Java',
        '.DMD' : 'SQL',
        '.JAVA' : 'Java',
        '.PY' : 'Python',
        '.RES' : 'C++',
        '.SWIFT' : 'Swift',
        '.ASM' : 'Assembly',
        '.XSD' : 'XML',
        '.RBW' : 'Ruby',
        '.CLW' : 'C++',
        '.NCB' : 'C++',
        '.FSX' : 'F#',
        '.SH' : 'Shell',
        '.C' : 'C',
        'PL' : 'Perl',
        '.FS' : 'F#',
        '.INO' : 'Arduino',
        'RPY' : 'Python',
        '.VCPROJ' : 'C++',
        '.HH' :	'C++',
        '.CC' : 'C++',
        '.PYD' : 'Python',
        '.R' : 'R',
        '.APS' : 'C++',
        '.HS' : 'Haskell',
        '.PM' : 'Perl',
        '.PH' : 'Perl',
        '.CSX' : 'Visual C#',
        '.JS' : 'JavaScript',
        '.HTML' : 'HTML',
        '.CSS' : 'CSS',
        '.PHP' : 'PHP'
    }
    user = {   'Name' : 'User',
                'Total' : 0    }
    userInfo = []
    repos = g.get_user().get_repos()
    for repo in repos:
        repoDetails = { 'Name' : repo.name,
                        'Total' : 0         }
        #Traverse through repo
        contents = repo.get_contents('')
        while len(contents) > 1:
            file_content = contents.pop(0)
            if file_content.type == 'dir':
                contents.extend(repo.get_contents(file_content.path))
            else:
                #Get file extention
                extention = re.search(r'.+(\..+)$', file_content.name, re.IGNORECASE)
                #If proramming file
                if extention and extention.group(1).upper() in proLang:
                    lang = proLang[extention.group(1).upper()]
                    #Add to user totals
                    user['Total'] += file_content.size
                    if lang in user:
                        user[lang] += file_content.size
                    else:
                        user[lang] = file_content.size
                    #Add to repo totals
                    repoDetails['Total'] += file_content.size
                    if lang in repoDetails:
                        repoDetails[lang] += file_content.size
                    else:
                        repoDetails[lang] = file_content.size

        #Add repo_details to userInfo
        userInfo.append(repoDetails)

    #Add user to start of userInfo
    userInfo = [user] + userInfo
    return userInfo

#Program==================================================
if __name__ == '__main__':
    #Create github account using personal access token
    login = input('Enter: <userName> <password>\t')
    uName, passW = login.split(' ')
    g = Github(uName, passW)
    #print(getRepoDetails(g))
    print(getLangSkills(g))