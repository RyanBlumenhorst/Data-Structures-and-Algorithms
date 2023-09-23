from GraphAndVertexClass import Graph, Vertex

# Refer to notes Figure 6.6.3
g = Graph()
vertex_a = Vertex("1")
vertex_b = Vertex("2")
vertex_c = Vertex("3")
vertex_d = Vertex("4")
vertex_e = Vertex("5")
g.add_vertex(vertex_a)
g.add_vertex(vertex_b)
g.add_vertex(vertex_c)
g.add_vertex(vertex_d)
g.add_vertex(vertex_e)

g.add_directed_edge(vertex_a, vertex_b, 8)
g.add_directed_edge(vertex_a, vertex_c, 12)
g.add_directed_edge(vertex_a, vertex_d, 17)
g.add_directed_edge(vertex_b, vertex_e, 11)
g.add_directed_edge(vertex_e, vertex_c, 23)
g.add_directed_edge(vertex_c, vertex_d, 15)
g.add_directed_edge(vertex_e, vertex_d, 6)