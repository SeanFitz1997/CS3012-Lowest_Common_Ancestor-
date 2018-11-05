#Imports==================================================
from github import Github
#Functions================================================
''' 
Returns user projects as a string. Displays:
- Username and Name
- Projects & Toppics
'''
def getProjects(user):

    if user is None:
        return 'No User Provided'
    return ''

#Program==================================================
if __name__ == '__main__':
    #Create github account using access token
    g = Github("a28d927e2e3ed1098f299df8c11868c7ffc290ce")

    for repo in g.get_user().get_repos():
        print('Repo: %s, Toppics: %s' % (repo.name, repo.get_topics()))