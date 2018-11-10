#Imports==================================================
from github import Github
#Functions================================================
''' 
Returns user projects as a string. Displays:
'''
def getProjects(user):

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
                        repo.name, list(repo.get_branches()),repo.get_topics(), 
                        len(list(repo.get_commits())), len(list(repo.get_collaborators())), 
                        repo.stargazers_count)
        #print('Repo: %s, Toppics: %s' % (repo.name, repo.get_topics()))

    return output

#Program==================================================
if __name__ == '__main__':
    #Create github account using personal access token
    login = input('Enter: <userName> <passWord>\t')
    uName, passW = login.split(' ')
    g = Github(uName, passW)
    print(getProjects(g))