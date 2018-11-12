#Imports==================================================
import re
from github import Github
#Functions================================================
''' Returns info on users repos '''
def getRepoDetails(user):

    if user is None:
        return None

    userDetails = {
        'UserName' : user.get_user().login,
        'Name' : user.get_user().name,
        'Repos' : []
    }

    for repo in user.get_user().get_repos():
        repoDetails = {
            'Name' : repo.name,
            'Toppics' : repo.get_topics(),
            'Branchs' : list(repo.get_branches()),
            'Commits' : list(repo.get_commits()),
            'Collaburators' : list(repo.get_collaborators()),
            'Stars' : repo.stargazers_count
        }
        userDetails['Repos'].append(repoDetails)

    return userDetails

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
    userDetails = { 'Name' : 'User',
                    'Total' : 0    }
    userInfo = []
    repos = user.get_user().get_repos()
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
                    userDetails['Total'] += file_content.size
                    if lang in userDetails:
                        userDetails[lang] += file_content.size
                    else:
                        userDetails[lang] = file_content.size
                    #Add to repo totals
                    repoDetails['Total'] += file_content.size
                    if lang in repoDetails:
                        repoDetails[lang] += file_content.size
                    else:
                        repoDetails[lang] = file_content.size

        #Add repo_details to userInfo
        userInfo.append(repoDetails)

    #Add user to start of userInfo
    userInfo = [userDetails] + userInfo
    return userInfo

#Program==================================================
if __name__ == '__main__':
    #Create github account using personal access token
    login = input('Enter: <userName> <password>\t')
    uName, passW = login.split(' ')
    g = Github(uName, passW)
    print(getRepoDetails(g))
    print(getLangSkills(g))