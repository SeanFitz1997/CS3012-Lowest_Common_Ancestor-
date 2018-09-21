#Imports==================================================
#Classes==================================================
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
#Functions================================================
def findLCA(root, x, y):
    if(root is None or x is None or y is None):
        return None
    return None

def pathTo(root, path, key):
    if(root is None): 
        return False
  
    # Store this node is path vector. The node will be 
    path.append(root.key) 

    if(root.key == key): 
        return True

    if(((root.left != None and pathTo(root.left, path, key)) or
            (root.right!= None and pathTo(root.right, path, key)))): 
        return True 
    # removed if not in path from root to k 
    path.pop() 
    return False

#Program==================================================