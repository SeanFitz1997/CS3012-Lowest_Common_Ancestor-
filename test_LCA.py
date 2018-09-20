import unittest
import LCA

class test_LCA(unittest.TestCase):

    def test_findLCA(self):
        #Test 1: test all values equal None
        self.assertAlmostEqual(LCA.findLCA(None, None, None), None)

        #Test 2: test when both node are root
        root = LCA.Node(1)
        self.assertAlmostEqual(LCA.findLCA(root, 1, 1), 1)

        #Test 3: test when a value is not in tree
        self.assertSequenceEqual(LCA.findLCA(root, 50, 51), None)

        #Test 4: LCA 4-5
        root.left = LCA.Node(2) 
        root.right = LCA.Node(3) 
        root.left.left = LCA.Node(4) 
        root.left.right = LCA.Node(5) 
        root.right.left = LCA.Node(6) 
        root.right.right = LCA.Node(7)
        self.assertSequenceEqual(LCA.findLCA(root, 4, 5), 2)

        #Test 5: LCA 4-6
        self.assertSequenceEqual(LCA.findLCA(root, 4, 6), 1)

        #Test 6: LCA 3-4
        self.assertSequenceEqual(LCA.findLCA(root, 3, 4), 1)

        #Test 7: LCA 2-4
        self.assertSequenceEqual(LCA.findLCA(root, 2, 4), 2)

if(__name__ == '__main__'):
    unittest.main()