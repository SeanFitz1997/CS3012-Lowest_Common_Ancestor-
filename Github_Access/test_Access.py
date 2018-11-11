import unittest
import Access
from github import Github

class test_LCA(unittest.TestCase):

    def setUp(self):
        login = input('Test User Enter: <userName> <password>\t')
        uName, passW = login.split(' ')
        self.testUser = Github(uName, passW)

    def test_getProjects(self):
        #Test 1: Test fuction with None value
        self.assertEqual(Access.getRepoDetails(None), None)

        #Test 2: Test with valid user
        repoDetails = Access.getRepoDetails(self.testUser)
        self.assertEqual(repoDetails['UserName'], 'SeanFitz1997')
        self.assertEqual(repoDetails['Name'], 'Sean Fitzpatrick')
        self.assertEqual(repoDetails['Repos'][2]['Name'], 'CS3012_SoftwareEngineering')
        self.assertEqual(repoDetails['Repos'][2]['Toppics'], ['python', 'algorithm', 'lowest-common-ancestor'])
        self.assertEqual(repoDetails['Repos'][2]['Stars'], 0)
        
        

if(__name__ == '__main__'):
    unittest.main()