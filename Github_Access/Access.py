#Imports==================================================
from github import Github
#Functions================================================
#Program==================================================

#Create github account using access token
g = Github("a28d927e2e3ed1098f299df8c11868c7ffc290ce")

for repo in g.get_user().get_repos():
    print('Repo: %s, Toppics: %s' % (repo.name, repo.get_topics()))