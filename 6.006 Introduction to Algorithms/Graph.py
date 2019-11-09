class FormGraph(object):
    def __init__(self, graph_name):
        """Assumes name is a string"""
        self.graph_name = graph_name
        self.nodes = []
        self.edges = []
        self.adj = {}   
    def add_node(self, node):
        if node in self.nodes:
            raise ValueError('Node already present')
        elif node not in self.nodes:
            self.nodes.append(node)
            self.adj[node] = []
    def add_edge(self, A, B, etype=1):
        """A and B are nodes and etype is an binary value representing
        graph type(digraph(1) or graph(0))"""
        if A and B not in self.nodes:
            raise ValueError("Either A or B or both A and B are not present in this graph")
        else :
            self.adj[A].append(B)
            self.edges.append((A, B))
            if etype == 0:
                self.adj[B].append(A)
                self.edges.append((B, A))
    def get_nodes(self):
        return self.nodes
    def get_edges(self):
        return self.edges
    def adj_list(self):
        print(self)
    def __str__(self):
        result = ''
        for x in self.adj:
            result = result + '\'' + str(x) + '\' -> ' + str(self.adj[x]) + '\n'
        return result[:-1] 

if __name__ == '__main__':
    g = FormGraph("Graph 1")
    g.add_node('A')
    g.add_node('B')
    print('Nodes : {}'.format(g.get_nodes()))
    g.add_node('C')
    g.add_edge('A', 'C', 0)
    g.add_edge('A', 'B')
    print('Edges : {}'.format(g.get_edges()))
    print()
    print('Graph\n{}'.format(g))
    
"""
OUTPUT

Nodes : ['A', 'B']
Edges : [('A', 'C'), ('C', 'A'), ('A', 'B')]

Graph
'A' -> ['C', 'B']
'B' -> []
'C' -> ['A']
"""
