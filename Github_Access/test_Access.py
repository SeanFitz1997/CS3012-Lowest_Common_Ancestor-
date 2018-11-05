import unittest
import Access

class test_LCA(unittest.TestCase):

    def test_getProjects(self):
        #Test 1: Test fuction with None value
        self.assertEqual(Access.getProjects(None), 'No User Provided')

        #Test 2: Test with valid user
        # TODO test with my account

if(__name__ == '__main__'):
    unittest.main()