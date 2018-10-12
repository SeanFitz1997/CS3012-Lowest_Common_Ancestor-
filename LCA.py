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

    px = []
    pathTo(root, px, x)
    py = []
    pathTo(root, py, y)

    lca = None 
    for x_key, y_key, in zip(px, py):
        if(x_key == y_key):
            lca = x_key

    return lca

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
root = Node(1)
root.children.append(Node(2))
root.children.append(Node(5))
root.children.append(Node(3))
root.children[0].children.append(Node(4))
root.children[2].children.append(Node(5))
root.children[2].children.append(Node(6))
root.children[2].children.append(Node(7))

print(findPathsTo(root, 4))