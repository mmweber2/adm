from graph import Vertex
from graph import Edge
from graph import find_path
from graph import dfs
from graph import Graph
from nose.tools import assert_raises

# Since each Vertex needs a unique name, I need to either give them all
# unique names in these tests or break the tests into more files.
# For this purpose, I created Vertex._make_test_vertex(), but the older
# tests still use manual test names.
def test_new_vertex():
    a = Vertex("A1")
    assert a.name == "A1"
    assert a.edges == []

def test_duplicate_vertex_name():
    a = Vertex("A2")
    assert_raises(ValueError, Vertex, "A2")

def test_new_vertex_empty_string():
    a = Vertex("")
    assert a.name == ""

def test_vertex_invalid_edges():
    assert_raises(TypeError, Vertex, "A3", "A2")

def test_make_test_vertex():
    s = Vertex._make_test_vertex()
    a = Vertex(s)
    assert a.name == s

# Test for creating a vertex with existing edges can be found
# after the other Edge tests.

def test_edge_default():
    b = Vertex("A4")
    a = Edge(b)
    assert a.vertex.name == "A4"
    assert a.weight == 0

def test_edge_weight():
    a = Vertex(Vertex._make_test_vertex())
    b = Edge(a, 10)
    assert b.weight == 10

def test_edge_invalid_weight():
    a = Vertex(Vertex._make_test_vertex())
    assert_raises(ValueError, Edge, a, "test")

def test_add_edge_normal():
    a = Vertex("A5")
    b = Vertex("A6")
    c = Edge(b)
    a.add_edge(c)
    assert len(a.edges) == 1
    assert c in a.edges

def test_add_edge_duplicate():
    a = Vertex("A7")
    b = Vertex("A8")
    c = Edge(b)
    d = Edge(b)
    a.add_edge(d)
    a.add_edge(c)
    assert len(a.edges) == 2
    assert d in a.edges
    assert c in a.edges

def test_add_edge_self_loop():
    a = Vertex(Vertex._make_test_vertex())
    a.add_edge(Edge(a))
    assert len(a.edges) == 1
    assert a in [e.vertex for e in a.edges]

def test_add_edge_invalid():
    a = Vertex("A9")
    assert_raises(TypeError, a.add_edge, "B")

def test_vertex_valid_edges():
    """Test Vertex creation with a list of already-existing Edges."""
    b = Vertex(Vertex._make_test_vertex())
    c = Vertex(Vertex._make_test_vertex())
    d = Edge(b)
    e = Edge(c)
    a = Vertex(Vertex._make_test_vertex(), [d, e])
    assert a.edges == [d, e]

def test_size():
    g = Graph([Vertex(Vertex._make_test_vertex())])
    assert g.size() == len(g.vertices)

def test_graph_empty():
    a = Graph([])
    assert a.size() == 0

def test_graph_single_vertex():
    a = Vertex(Vertex._make_test_vertex())
    b = Graph([a])
    assert b.size() == 1

def test_graph_normal_set():
    a = Vertex(Vertex._make_test_vertex())
    b = Vertex(Vertex._make_test_vertex())
    g = Graph([a, b])
    assert g.size() == 2

def test_graph_duplicate_vertex():
    a = Vertex(Vertex._make_test_vertex())
    g = Graph([a, a])
    assert g.size() == 1

def test_graph_add_new_vertex_exists():
    a = Vertex(Vertex._make_test_vertex())
    g = Graph([a])
    g.add_vertex(a)
    assert g.size() == 1

def test_graph_add_new_vertex_new():
    a = Vertex(Vertex._make_test_vertex())
    g = Graph([a])
    g.add_vertex(Vertex(Vertex._make_test_vertex()))
    assert g.size() == 2

def test_graph_add_invalid_vertex():
    g = Graph([Vertex(Vertex._make_test_vertex())])
    assert_raises(TypeError, g.add_vertex, "String name")

def test_is_connected_empty():
    g = Graph([])
    assert g.is_connected()

def test_is_connected_single():
    g = Graph([Vertex(Vertex._make_test_vertex())])
    assert g.is_connected()

def test_is_connected_two_single():
    a = Vertex(Vertex._make_test_vertex())
    b = Vertex(Vertex._make_test_vertex())
    g = Graph([a, b])
    assert not g.is_connected()

def test_is_connected_two_vert_one_edge():
    a = Vertex(Vertex._make_test_vertex())
    b = Vertex(Vertex._make_test_vertex())
    a.add_edge(Edge(b))
    g = Graph([a, b])
    assert not g.is_connected()

def test_is_connected_two_doubly_connected():
    a = Vertex(Vertex._make_test_vertex())
    b = Vertex(Vertex._make_test_vertex())
    a.add_edge(Edge(b))
    b.add_edge(Edge(a))
    g = Graph([a, b])
    assert g.is_connected()

def test_is_connected_three_vert_two_connections():
    a = Vertex(Vertex._make_test_vertex())
    b = Vertex(Vertex._make_test_vertex())
    c = Vertex(Vertex._make_test_vertex())
    a.add_edge(Edge(b))
    b.add_edge(Edge(c))
    c.add_edge(Edge(a))
    g = Graph([a, b, c])
    assert g.is_connected()

def test_has_cycle_self_loop():
    a = Vertex(Vertex._make_test_vertex())
    a.add_edge(Edge(a))
    g = Graph([a])
    assert g.has_cycle()

def test_has_cycle_single_no_loop():
    a = Vertex(Vertex._make_test_vertex())
    g = Graph([a])
    assert not g.has_cycle()

def test_has_cycle_two_vertices_linked():
    a = Vertex(Vertex._make_test_vertex())
    b = Vertex(Vertex._make_test_vertex())
    a.add_edge(Edge(b))
    b.add_edge(Edge(a))
    g = Graph([a, b])
    assert g.has_cycle()

def test_has_cycle_indirect():
    a = Vertex(Vertex._make_test_vertex())
    b = Vertex(Vertex._make_test_vertex())
    c = Vertex(Vertex._make_test_vertex())
    a.add_edge(Edge(b))
    b.add_edge(Edge(c))
    c.add_edge(Edge(a))
    g = Graph([a, b, c])
    assert g.has_cycle()

def test_has_cycle_implicit():
    """A Vertex is accessible to the Graph but not explicitly part of it."""
    a = Vertex(Vertex._make_test_vertex())
    b = Vertex(Vertex._make_test_vertex())
    c = Vertex(Vertex._make_test_vertex())
    a.add_edge(Edge(b))
    b.add_edge(Edge(c))
    c.add_edge(Edge(a))
    g = Graph([a, b])
    assert g.has_cycle()

def test_find_path_no_path():
    a = Vertex("A10")
    b = Vertex("A11")
    assert find_path(a, b) == []

def test_find_path_start_is_end():
    a = Vertex("A12")
    assert find_path(a, a) == [a]

def test_find_path_direct_connection():
    a = Vertex("A13")
    b = Vertex("A14")
    a.add_edge(Edge(b))
    assert find_path(a, b) == [a, b]
    # Path is only in one direction
    assert find_path(b, a) == []

def test_find_path_ignores_weights():
    a = Vertex(Vertex._make_test_vertex())
    b = Vertex(Vertex._make_test_vertex())
    a.add_edge(Edge(b, 1))
    c = Vertex(Vertex._make_test_vertex())
    a.add_edge(Edge(c, 100))
    b.add_edge(Edge(c, 1))
    assert find_path(a, c) == [a, c]

def test_find_path_chain():
    a = Vertex("A15")
    b = Vertex("A16")
    c = Vertex("A17")
    a.add_edge(Edge(b))
    b.add_edge(Edge(c))
    assert find_path(a, c) == [a, b, c]

def test_find_path_cycle():
    a = Vertex("A33")
    b = Vertex("A34")
    c = Vertex("A35")
    a.add_edge(Edge(b))
    b.add_edge(Edge(a))
    b.add_edge(Edge(c))
    assert find_path(a, c) == [a, b, c]

def test_dfs_start_node():
    a = Vertex("A18")
    assert dfs(a, a)

def test_dfs_direct_connection():
    a = Vertex("A19")
    b = Vertex("A20")
    a.add_edge(Edge(b))
    assert dfs(a, b)

def test_dfs_no_path():
    a = Vertex("A21")
    b = Vertex("A22")
    assert not dfs(a, b)

def test_dfs_chain():
    a = Vertex("A23")
    b = Vertex("A24")
    c = Vertex("A25")
    a.add_edge(Edge(b))
    b.add_edge(Edge(c))
    assert dfs(a, c)

def test_dfs_multiple_paths():
    a = Vertex("A26")
    b = Vertex("A27")
    c = Vertex("A28")
    d = Vertex("A29")
    a.add_edge(Edge(b))
    b.add_edge(Edge(c))
    c.add_edge(Edge(d))
    a.add_edge(Edge(d))
    assert dfs(a, d)

def test_dfs_cycle():
    a = Vertex("A30")
    b = Vertex("A31")
    c = Vertex("A32")
    a.add_edge(Edge(b))
    b.add_edge(Edge(a))
    b.add_edge(Edge(c))
    assert dfs(a, c)



