from graph import Vertex
from graph import Edge
from graph import find_path
from graph import dfs
from nose.tools import assert_raises

# Since each Vertex needs a unique name, I need to either give them all
# unique names in these tests or break the tests into more files.
def test_new_vertex():
    a = Vertex("A1")
    assert a.name == "A1"
    assert a.edges == []

def test_duplicate_vertex_name():
    a = Vertex("A2")
    assert_raises(ValueError, Vertex, "A2")

def test_vertex_invalid_edges():
    assert_raises(TypeError, Vertex, "A3", "A2")

def test_edge_default():
    b = Vertex("A4")
    a = Edge(b)
    assert a.vertex.name == "A4"
    assert a.weight == 0

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

def test_add_edge_invalid():
    a = Vertex("A9")
    assert_raises(TypeError, a.add_edge, "B")

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



