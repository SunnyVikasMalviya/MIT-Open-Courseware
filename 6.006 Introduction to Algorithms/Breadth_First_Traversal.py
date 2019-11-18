def Breadth_First_Traversal(s, adj):
    """
    Takes the starting node for breadth first traversal and the adjoint matrix
    of the graph and returns the level of each node in the graph starting from
    0 for the start node.
    """
    level, parent = {}, {}
    level[s] = 0
    parent[s] = None
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1
    return level

if __name__ == '__main__' :
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
    g.add_edge('D', 'E', 0)
    g.add_edge('D', 'F', 0)
    g.add_edge('D', 'G', 0)
    g.add_edge('E', 'F', 0)
    g.add_edge('F', 'G', 0)
    adj = g.get_adj()
    lvl = Breadth_First_Traversal('S', adj)
    print('Nodes: {}'.format(g.get_nodes()))
    print('Edges: {}'.format(g.get_edges()))
    print('Graph\n{}'.format(g))
    print('Adjoint Matrix of the graph: {}'.format(adj))
    print('Levels of each node after breadth-first-traversal: {}'.format(lvl))


"""
OUTPUT

Nodes: ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
Edges: [('S', 'A'), ('A', 'S'), ('S', 'C'), ('C', 'S'), ('A', 'B'), ('B', 'A'),\
    ('C', 'D'), ('D', 'C'), ('C', 'G'), ('G', 'C'), ('D', 'E'), ('E', 'D'),\
    ('D', 'F'), ('F', 'D'), ('D', 'G'), ('G', 'D'), ('E', 'F'), ('F', 'E'),\
    ('F', 'G'), ('G', 'F')]
Graph
'S' -> ['A', 'C']
'A' -> ['S', 'B']
'B' -> ['A']
'C' -> ['S', 'D', 'G']
'D' -> ['C', 'E', 'F', 'G']
'E' -> ['D', 'F']
'F' -> ['D', 'E', 'G']
'G' -> ['C', 'D', 'F']
Adjoint Matrix of the graph: {'S': ['A', 'C'], 'A': ['S', 'B'], 'B': ['A'],\
    'C': ['S', 'D', 'G'], 'D': ['C', 'E', 'F', 'G'], 'E': ['D', 'F'], \
    'F': ['D', 'E', 'G'], 'G': ['C', 'D', 'F']}
Levels of each node after breadth-first-traversal: {'S': 0, 'A': 1, 'C': 1, \
    'B': 2, 'D': 2, 'G': 2, 'E': 3, 'F': 3}"""
