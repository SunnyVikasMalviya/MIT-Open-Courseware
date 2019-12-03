class FormGraph(object):
    def __init__(self, graph_name):
        """Assumes name is a string"""
        self.graph_name = graph_name
        self.nodes = []
        self.edges = []
        self.weights = {}
        self.adj = {}   
    def add_node(self, node):
        if node in self.nodes:
            raise ValueError('Node already present')
        elif node not in self.nodes:
            self.nodes.append(node)
            self.adj[node] = []
    def add_edge(self, A, B, etype=1, weight=0, weight1=None):
        """A and B are nodes and etype is an binary value representing
        graph type(digraph(1) or graph(0))"""
        if A and B not in self.nodes:
            raise ValueError("Either A or B or both A and B are not present in this graph")
        else :
            self.adj[A].append(B)
            self.edges.append((A, B))
            #Now assigning weight to the edge
            self.weights[(A, B)] = weight
            if etype == 0:
                self.adj[B].append(A)
                self.edges.append((B, A))
                #Assigning weight to returning edge
                #weight1(if defined) is weight of returning edge
                if not weight1 :
                    self.weights[(B, A)] = weight
                #else, returning edge will have the same weight as going edge
                else :
                    self.weights[(B, A)] = weight1
    def get_nodes(self):
        return self.nodes
    def get_edges(self):
        return self.edges
    def get_weights(self):
        return self.weights
    def get_edge_weight(self, A, B):
        return self.weights[(A, B)]
    def adj_list(self):
        print(self)
    def get_adj(self):
        return self.adj
    def __str__(self):
        result = ''
        for x in self.adj:
            result = result + '\'' + str(x) + '\' -> ' + str(self.adj[x]) + '\n'
        return result[:-1]

if __name__ == '__main__':
    g = FormGraph("Graph 1")
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_edge('A', 'C', 0, 2)
    g.add_edge('A', 'B', weight=4)
    g.add_edge('C', 'D', 0, weight1=3)
    print('Nodes : {}'.format(g.get_nodes()))
    print('Edges : {}'.format(g.get_edges()))
    print('Weights : {}'.format(g.get_weights()))
    print('Edge Weight form {} to {} is {}'.format('A', 'B', g.get_edge_weight('A', 'B')))
    print()
    print('Graph\n{}'.format(g))
    
"""
OUTPUT

Nodes : ['A', 'B', 'C', 'D']
Edges : [('A', 'C'), ('C', 'A'), ('A', 'B'), ('C', 'D'), ('D', 'C')]
Weights : {('A', 'C'): 2, ('C', 'A'): 2, ('A', 'B'): 4, ('C', 'D'): 0, ('D', 'C'): 3}
Edge Weight form A to B is 4

Graph
'A' -> ['C', 'B']
'B' -> []
'C' -> ['A', 'D']
'D' -> ['C']
"""
