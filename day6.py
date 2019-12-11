'''input
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
'''
all_nodes = {}

class Node:
    
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
 
    def add_child(self, node):
        self.children.append(node)

while True:
    try:
        a,b = input().split(')')
        if a in all_nodes:
            node_a = all_nodes[a]
        else:
            node_a = Node(a)
 
        if b in all_nodes:
            node_b = all_nodes[b]
        else:
            node_b = Node(b)
 
        all_nodes[a] = node_a
        all_nodes[b] = node_b
        node_a.add_child(node_b)
        node_b.parent = node_a
    except:
        break

direct = 0
indirect = 0
for name, node in all_nodes.items():
    parent_node = node.parent
    if parent_node != None:
        direct += 1
 
    while parent_node != None:
        parent_node = parent_node.parent
        if parent_node != None:
            indirect += 1
 
 
print('total indirect + direct: ', direct + indirect)

def dfs(node, target):
    if node == None:
        return []

    if node.name == target:
        return [node.name]

    for child in node.children:        
        result = dfs(child, target)
        if len(result) > 0:
            return result + [node.name]

    return []

path = dfs(all_nodes["COM"], "YOU")
path2 = dfs(all_nodes["COM"], "SAN")
path = list(reversed(path))
path2 = list(reversed(path2))

common_parent = 0
for i in range(len(path)):
    a = path[i]
    b = path2[i]
    if a != b:        
        break
    else:
        common_parent += 1        

path = path[common_parent:]
path2 = path2[common_parent:]

#print(path, path2)
print(len(path) + len(path2) - 2)