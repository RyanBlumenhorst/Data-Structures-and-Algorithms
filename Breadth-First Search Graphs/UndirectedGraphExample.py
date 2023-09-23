from GraphAndVertexClass import Graph, Vertex

# Refer to notes figure 6.6.4
g = Graph()
vertex_a = Vertex("Tokyo")
vertex_b = Vertex("New York")
vertex_c = Vertex("London")
vertex_d = Vertex("Sydney")
g.add_vertex(vertex_a)
g.add_vertex(vertex_b)
g.add_vertex(vertex_c)
g.add_vertex(vertex_d)

g.add_undirected_edge(vertex_a, vertex_b, 6743)
g.add_undirected_edge(vertex_a, vertex_c, 5941)
g.add_undirected_edge(vertex_a, vertex_d, 4863)
g.add_undirected_edge(vertex_b, vertex_c, 3425)
g.add_undirected_edge(vertex_b, vertex_d, 9868)
g.add_undirected_edge(vertex_c, vertex_d, 10562)
