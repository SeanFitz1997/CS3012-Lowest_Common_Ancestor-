#Imports==================================================
#Classes==================================================
class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

    def __repr__(self):
        return str(self.key)
#Functions================================================
def findLCA(root, x, y):
    if(root is None or x is None or y is None):
        return None

    px = findPathsTo(root, x)
    pxFlat = list(set([item for sublist in px for item in sublist]))
    py = findPathsTo(root, y)
    lca = (None, -1)

    for keyX in pxFlat:
        for l in py:
            if (keyX in l) and l.index(keyX) > lca[1]:
                lca = (keyX, l.index(keyX))

    return lca[0]

def findPathsTo(root, key):
    if(root == None or key == None):
        return []
    
    paths = []
    queue = [(root, [root.key])]
    while queue != []:
        curNode = queue[0][0]
        curPath = queue[0][1]
        del queue[0]

        if(curNode.key == key):
            paths.append(curPath)
            continue

        for child in curNode.children:
            if(pathTo(child, [], key)):
                queue.append((child, curPath + [child.key]))

    return paths

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