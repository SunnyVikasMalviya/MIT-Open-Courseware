from Depth_First_Visit import Depth_First_Visit
from itertools import permutations, product
from random import randrange
from Graph import FormGraph
    

def Level_Assign(V, adj):
    """
    This function assigns levels to all the nodes of the DAG.
    It returns a dictionary with levels as key values and a list of all the
    nodes at that level. 
    """
    level = {}
    parent = {}
    #Depth_First_Visit(V, adj, {}, level)
    for s in adj.keys():
        if s not in level and s not in parent:
            parent[s] = None
            Depth_First_Visit(s, adj, parent, level)
    print("#Ignore this line")
    print()
    res = {}
    for x in set(level.values()):
        res[x] = []
    [res[level[x]].append(x) for x in level]
    return res
    

def Topological_All(V, adj):
    """
    This function returns all of the possible topologically sorted sequences,
    which means all possible sequence of schedulling the given graph.
    The number of sequences can be calculated by taking the product of the
    factorials of the lengths of all the dict.values() of the Lvl_assign
    dictionary. 
    """
    level = Level_Assign(V, adj)
    res = []
    all_ = []
    for x in level.values():
        res.append(list(permutations(x)))
    for i in product(*res):
        all_.append(i)
    return all_
    
        
def Topological_Sort(V, adj):
    """
    Topological sorting is only done for Direct-Acyclic_Graphs(DAG).
    It is a schedulling algorithm that gives a sequence of visiting nodes of the
    DAG.
    Topological Sorting Algorithm
    1. Depth-First_Visit is done for each node starting from the root node.
    2. Each node is assigned a level in the DFS tree.
    3. All the nodes at the same level can be independently schedulled.
    4. All the nodes having a higher level can only be schedulled once all the
        lesser leveled nodes have been schedulled.
    5. Their can be more than one sequence of topological sorting as x levels at
        one level can be arranged in x! ways.
    This function returns a random sequence from all of the possible 
    topologically sorted sequences.
    """
    all_ = Topological_All(V, adj)
    return all_[randrange(len(all_))]
        

if __name__ == '__main__':
    g = FormGraph("Graph")
    g.add_node('S')
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_node('E')
    g.add_node('F')
    g.add_node('G')
    g.add_node('H')
    g.add_node('I')
    g.add_edge('S', 'A', 1)
    g.add_edge('S', 'D', 1)
    g.add_edge('A', 'B', 1)
    g.add_edge('D', 'B', 1)
    g.add_edge('H', 'E', 1)
    g.add_edge('D', 'E', 1)
    g.add_edge('I', 'G', 1)
    g.add_edge('E', 'F', 1)
    g.add_edge('F', 'G', 1)
    g.add_edge('H', 'I', 1)
    adj = g.get_adj()
    lvl_ = Level_Assign('S', adj)
    all_ = Topological_All('S', adj)
    sort_ = Topological_Sort('S', adj)
    print('Nodes:\n {}'.format(g.get_nodes()))
    print('Edges:\n {}'.format(g.get_edges()))
    print('Graph\n{}'.format(g))
    #print('Adjoint Matrix of the graph: {}'.format(adj))
    print()
    print("Nodes on each level:\n {}".format(lvl_))
    print("\nAll topologically sorted sequence:")
    [print("{}".format(x)) for x in all_]
    print()
    print("One of the topological sort:\n {}".format(sort_))



"""
OUTPUT

A B D E F G I #Ignore this line

A B D E F G I #Ignore this line

A B D E F G I #Ignore this line

Nodes:
 ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
Edges:
 [('S', 'A'), ('S', 'D'), ('A', 'B'), ('D', 'B'), ('H', 'E'), ('D', 'E'), ('I', 'G'), ('E', 'F'), ('F', 'G'), ('H', 'I')]
Graph
'S' -> ['A', 'D']
'A' -> ['B']
'B' -> []
'C' -> []
'D' -> ['B', 'E']
'E' -> ['F']
'F' -> ['G']
'G' -> []
'H' -> ['E', 'I']
'I' -> ['G']

Nodes on each level:
 {0: ['S', 'C', 'H'], 1: ['A', 'D', 'I'], 2: ['B', 'E'], 3: ['F'], 4: ['G']}

All topologically sorted sequence:
(('S', 'C', 'H'), ('A', 'D', 'I'), ('B', 'E'), ('F',), ('G',))
(('S', 'C', 'H'), ('A', 'D', 'I'), ('E', 'B'), ('F',), ('G',))
(('S', 'C', 'H'), ('A', 'I', 'D'), ('B', 'E'), ('F',), ('G',))
(('S', 'C', 'H'), ('A', 'I', 'D'), ('E', 'B'), ('F',), ('G',))
(('S', 'C', 'H'), ('D', 'A', 'I'), ('B', 'E'), ('F',), ('G',))
(('S', 'C', 'H'), ('D', 'A', 'I'), ('E', 'B'), ('F',), ('G',))
(('S', 'C', 'H'), ('D', 'I', 'A'), ('B', 'E'), ('F',), ('G',))
(('S', 'C', 'H'), ('D', 'I', 'A'), ('E', 'B'), ('F',), ('G',))
(('S', 'C', 'H'), ('I', 'A', 'D'), ('B', 'E'), ('F',), ('G',))
(('S', 'C', 'H'), ('I', 'A', 'D'), ('E', 'B'), ('F',), ('G',))
(('S', 'C', 'H'), ('I', 'D', 'A'), ('B', 'E'), ('F',), ('G',))
(('S', 'C', 'H'), ('I', 'D', 'A'), ('E', 'B'), ('F',), ('G',))
(('S', 'H', 'C'), ('A', 'D', 'I'), ('B', 'E'), ('F',), ('G',))
(('S', 'H', 'C'), ('A', 'D', 'I'), ('E', 'B'), ('F',), ('G',))
(('S', 'H', 'C'), ('A', 'I', 'D'), ('B', 'E'), ('F',), ('G',))
(('S', 'H', 'C'), ('A', 'I', 'D'), ('E', 'B'), ('F',), ('G',))
(('S', 'H', 'C'), ('D', 'A', 'I'), ('B', 'E'), ('F',), ('G',))
(('S', 'H', 'C'), ('D', 'A', 'I'), ('E', 'B'), ('F',), ('G',))
(('S', 'H', 'C'), ('D', 'I', 'A'), ('B', 'E'), ('F',), ('G',))
(('S', 'H', 'C'), ('D', 'I', 'A'), ('E', 'B'), ('F',), ('G',))
(('S', 'H', 'C'), ('I', 'A', 'D'), ('B', 'E'), ('F',), ('G',))
(('S', 'H', 'C'), ('I', 'A', 'D'), ('E', 'B'), ('F',), ('G',))
(('S', 'H', 'C'), ('I', 'D', 'A'), ('B', 'E'), ('F',), ('G',))
(('S', 'H', 'C'), ('I', 'D', 'A'), ('E', 'B'), ('F',), ('G',))
(('C', 'S', 'H'), ('A', 'D', 'I'), ('B', 'E'), ('F',), ('G',))
(('C', 'S', 'H'), ('A', 'D', 'I'), ('E', 'B'), ('F',), ('G',))
(('C', 'S', 'H'), ('A', 'I', 'D'), ('B', 'E'), ('F',), ('G',))
(('C', 'S', 'H'), ('A', 'I', 'D'), ('E', 'B'), ('F',), ('G',))
(('C', 'S', 'H'), ('D', 'A', 'I'), ('B', 'E'), ('F',), ('G',))
(('C', 'S', 'H'), ('D', 'A', 'I'), ('E', 'B'), ('F',), ('G',))
(('C', 'S', 'H'), ('D', 'I', 'A'), ('B', 'E'), ('F',), ('G',))
(('C', 'S', 'H'), ('D', 'I', 'A'), ('E', 'B'), ('F',), ('G',))
(('C', 'S', 'H'), ('I', 'A', 'D'), ('B', 'E'), ('F',), ('G',))
(('C', 'S', 'H'), ('I', 'A', 'D'), ('E', 'B'), ('F',), ('G',))
(('C', 'S', 'H'), ('I', 'D', 'A'), ('B', 'E'), ('F',), ('G',))
(('C', 'S', 'H'), ('I', 'D', 'A'), ('E', 'B'), ('F',), ('G',))
(('C', 'H', 'S'), ('A', 'D', 'I'), ('B', 'E'), ('F',), ('G',))
(('C', 'H', 'S'), ('A', 'D', 'I'), ('E', 'B'), ('F',), ('G',))
(('C', 'H', 'S'), ('A', 'I', 'D'), ('B', 'E'), ('F',), ('G',))
(('C', 'H', 'S'), ('A', 'I', 'D'), ('E', 'B'), ('F',), ('G',))
(('C', 'H', 'S'), ('D', 'A', 'I'), ('B', 'E'), ('F',), ('G',))
(('C', 'H', 'S'), ('D', 'A', 'I'), ('E', 'B'), ('F',), ('G',))
(('C', 'H', 'S'), ('D', 'I', 'A'), ('B', 'E'), ('F',), ('G',))
(('C', 'H', 'S'), ('D', 'I', 'A'), ('E', 'B'), ('F',), ('G',))
(('C', 'H', 'S'), ('I', 'A', 'D'), ('B', 'E'), ('F',), ('G',))
(('C', 'H', 'S'), ('I', 'A', 'D'), ('E', 'B'), ('F',), ('G',))
(('C', 'H', 'S'), ('I', 'D', 'A'), ('B', 'E'), ('F',), ('G',))
(('C', 'H', 'S'), ('I', 'D', 'A'), ('E', 'B'), ('F',), ('G',))
(('H', 'S', 'C'), ('A', 'D', 'I'), ('B', 'E'), ('F',), ('G',))
(('H', 'S', 'C'), ('A', 'D', 'I'), ('E', 'B'), ('F',), ('G',))
(('H', 'S', 'C'), ('A', 'I', 'D'), ('B', 'E'), ('F',), ('G',))
(('H', 'S', 'C'), ('A', 'I', 'D'), ('E', 'B'), ('F',), ('G',))
(('H', 'S', 'C'), ('D', 'A', 'I'), ('B', 'E'), ('F',), ('G',))
(('H', 'S', 'C'), ('D', 'A', 'I'), ('E', 'B'), ('F',), ('G',))
(('H', 'S', 'C'), ('D', 'I', 'A'), ('B', 'E'), ('F',), ('G',))
(('H', 'S', 'C'), ('D', 'I', 'A'), ('E', 'B'), ('F',), ('G',))
(('H', 'S', 'C'), ('I', 'A', 'D'), ('B', 'E'), ('F',), ('G',))
(('H', 'S', 'C'), ('I', 'A', 'D'), ('E', 'B'), ('F',), ('G',))
(('H', 'S', 'C'), ('I', 'D', 'A'), ('B', 'E'), ('F',), ('G',))
(('H', 'S', 'C'), ('I', 'D', 'A'), ('E', 'B'), ('F',), ('G',))
(('H', 'C', 'S'), ('A', 'D', 'I'), ('B', 'E'), ('F',), ('G',))
(('H', 'C', 'S'), ('A', 'D', 'I'), ('E', 'B'), ('F',), ('G',))
(('H', 'C', 'S'), ('A', 'I', 'D'), ('B', 'E'), ('F',), ('G',))
(('H', 'C', 'S'), ('A', 'I', 'D'), ('E', 'B'), ('F',), ('G',))
(('H', 'C', 'S'), ('D', 'A', 'I'), ('B', 'E'), ('F',), ('G',))
(('H', 'C', 'S'), ('D', 'A', 'I'), ('E', 'B'), ('F',), ('G',))
(('H', 'C', 'S'), ('D', 'I', 'A'), ('B', 'E'), ('F',), ('G',))
(('H', 'C', 'S'), ('D', 'I', 'A'), ('E', 'B'), ('F',), ('G',))
(('H', 'C', 'S'), ('I', 'A', 'D'), ('B', 'E'), ('F',), ('G',))
(('H', 'C', 'S'), ('I', 'A', 'D'), ('E', 'B'), ('F',), ('G',))
(('H', 'C', 'S'), ('I', 'D', 'A'), ('B', 'E'), ('F',), ('G',))
(('H', 'C', 'S'), ('I', 'D', 'A'), ('E', 'B'), ('F',), ('G',))

One of the topological sort:
 (('S', 'C', 'H'), ('A', 'D', 'I'), ('E', 'B'), ('F',), ('G',))
"""



