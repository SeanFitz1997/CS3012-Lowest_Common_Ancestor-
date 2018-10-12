#Imports==================================================
#Classes==================================================
class Node:
    def __init__(self, key):
        self.key = key
        self.children = []
#Functions================================================
def findLCA(root, x, y):
    if(root is None or x is None or y is None):
        return None

    px = []
    pathTo(root, px, x)
    py = []
    pathTo(root, py, y)

    lca = None 
    for x_key, y_key, in zip(px, py):
        if(x_key == y_key):
            lca = x_key
            
    return lca

def pathTo(root, path, key):
    if(root == None): 
        return False
  
    # Store this node is path vector. The node will be 
    path.append(root.key) 
    if(root.key == key): 
        return True

    for node in root.children:
        if node != None and pathTo(node, path, key):
            return True
        
    # removed if not in path from root to k 
    path.pop()
    return False

#Program==================================================