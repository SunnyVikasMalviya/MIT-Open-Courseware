
def Depth_First_Visit(s, adj, parent):
    """
    Takes the starting node for depth first visit and the adjoint matrix of the
    graph and returns the level of each node in the graph starting from the 0
    for the start node.
    """
    #parent = {}
    #level[s] = lvl_s
    parent[s] = None
    for v in adj[s]:
        if v not in parent:
            parent[v] = s
            #level[v] = lvl_s + 1
            print(v, end=' ')
            Depth_First_Visit(v, adj, parent)
    #print()

