from Depth_First_Visit import Depth_First_Visit

def Depth_First_Search(V, adj):
    """

    """
    parent = {}
    for s in V:
        if s not in parent:
            parent[s] = None
            Depth_First_Visit(V, adj, parent)
        

if __name__ == '__main__':
    from Graph import FormGraph
    g = FormGraph("Graph")
    g.add_node('S')
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_node('E')
    g.add_node('F')
    g.add_node('G')
    #g.add_node('H')
    g.add_edge('S', 'A', 0)
    g.add_edge('S', 'C', 0)
    g.add_edge('A', 'B', 0)
    g.add_edge('C', 'D', 0)
    g.add_edge('C', 'G', 0)
    g.add_edge('D', 'F', 0)
    g.add_edge('D', 'G', 0)
    g.add_edge('E', 'F', 0)
    g.add_edge('F', 'G', 0)
    g.add_edge('D', 'E', 0)
    adj = g.get_adj()
    lvl = Depth_First_Search('S', adj)
    print('\nThe above line shows the Depth First Search Implementation of the graph')
    print('Nodes: {}'.format(g.get_nodes()))
    print('Edges: {}'.format(g.get_edges()))
    print('Graph\n{}'.format(g))
    print('Adjoint Matrix of the graph: {}'.format(adj))
    print('Levels of each node after breadth-first-traversal: {}'.format(lvl))




"""
OUTPUT

A B C D F E G 
The above line shows the Depth First Search Implementation of the graph
Nodes: ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
Edges: [('S', 'A'), ('A', 'S'), ('S', 'C'), ('C', 'S'), ('A', 'B'), ('B', 'A'), ('C', 'D'), ('D', 'C'), ('C', 'G'), ('G', 'C'), ('D', 'F'), ('F', 'D'), ('D', 'G'), ('G', 'D'), ('E', 'F'), ('F', 'E'), ('F', 'G'), ('G', 'F'), ('D', 'E'), ('E', 'D')]
Graph
'S' -> ['A', 'C']
'A' -> ['S', 'B']
'B' -> ['A']
'C' -> ['S', 'D', 'G']
'D' -> ['C', 'F', 'G', 'E']
'E' -> ['F', 'D']
'F' -> ['D', 'E', 'G']
'G' -> ['C', 'D', 'F']
Adjoint Matrix of the graph: {'S': ['A', 'C'], 'A': ['S', 'B'], 'B': ['A'], 'C': ['S', 'D', 'G'], 'D': ['C', 'F', 'G', 'E'], 'E': ['F', 'D'], 'F': ['D', 'E', 'G'], 'G': ['C', 'D', 'F']}
Levels of each node after breadth-first-traversal: None
"""



