from StringIO import StringIO
from nose.tools import assert_raises
from file_graph import graph_from_file
from graph import Vertex

# Most tests use StringIO, so confirm that files can be read in
# the same way. (This file is not formatted for Graph creation.)
def test_reads_from_file():
    with open('test_file.txt', 'r') as handle:
        assert_raises(ValueError, graph_from_file, handle)

def test_empty_file():
    s = StringIO("")
    assert_raises(ValueError, graph_from_file, s)

def test_non_number_vertex_count():
    s = StringIO("Sam\nPaul")
    assert_raises(ValueError, graph_from_file, s)

def test_float_vertex_count():
    s = StringIO("3.5")
    assert_raises(ValueError, graph_from_file, s)

def test_zero_vertex():
    s = StringIO("0")
    g = graph_from_file(s)
    assert g.size() == 0
    assert g.top_sort() == []

def test_negative_vertex():
    s = StringIO("-1")
    assert_raises(ValueError, graph_from_file, s)

def test_duplicate_vertex_name():
    s = StringIO("2\nA\nA")
    assert_raises(ValueError, graph_from_file, s)

def test_small_vertex_count():
    s = StringIO("1\nE\nF")
    assert_raises(ValueError, graph_from_file, s)

def test_large_vertex_count():
    s = StringIO("3\nC\nD\nC|D")
    assert_raises(ValueError, graph_from_file, s)

def test_no_edges():
    name1 = Vertex._make_test_vertex()
    name2 = Vertex._make_test_vertex()
    s = StringIO("2\n{}\n{}".format(name1, name2))
    g = graph_from_file(s)
    assert g.size() == 2
    assert not g.is_connected()

def test_valid_no_weights():
    name1 = Vertex._make_test_vertex()
    name2 = Vertex._make_test_vertex()
    s = StringIO("2\n{0}\n{1}\n{0}|{1}\n{1}|{0}".format(name1, name2))
    g = graph_from_file(s)
    assert g.size() == 2
    assert g.is_connected()
    assert g.has_cycle()

# Attempt to create an edge from an unknown vertex
def test_invalid_from_edge():
    name1 = Vertex._make_test_vertex()
    name2 = Vertex._make_test_vertex()
    s = StringIO("2\n{0}\n{1}\n{2}|{1}\n{1}|{0}".format(name1, name2, "Fake name"))
    assert_raises(ValueError, graph_from_file, s)

# Attempt to create an edge to an unknown vertex
def test_invalid_from_edge():
    name1 = Vertex._make_test_vertex()
    name2 = Vertex._make_test_vertex()
    s = StringIO("2\n{0}\n{1}\n{0}|{2}\n{1}|{0}".format(name1, name2, "Fake name"))
    assert_raises(ValueError, graph_from_file, s)

def test_valid_with_weights():
    name1 = Vertex._make_test_vertex()
    name2 = Vertex._make_test_vertex()
    s = StringIO("2\n{0}\n{1}\n{0}|{1}|5\n{1}|{0}|2".format(name1, name2))
    g = graph_from_file(s)
    assert g.size() == 2
    assert g.is_connected()

# Extra pipes should be ignored
def test_extra_pipes():
    name1 = Vertex._make_test_vertex()
    name2 = Vertex._make_test_vertex()
    s = StringIO("2\n{0}\n{1}\n{0}|{1}|5|2\n{1}|{0}|2|5".format(name1, name2))
    g = graph_from_file(s)
    assert g.size() == 2
    assert g.is_connected()

def test_self_loop():
    name1 = Vertex._make_test_vertex()
    s = StringIO("1\n{0}\n{0}|{0}".format(name1))
    g = graph_from_file(s)
    assert g.size() == 1
    assert g.has_cycle()

def test_multi_edge():
    name1 = Vertex._make_test_vertex()
    name2 = Vertex._make_test_vertex()
    s = StringIO("2\n{0}\n{1}\n{0}|{1}|5\n{0}|{1}|2".format(name1, name2))
    g = graph_from_file(s)
    assert g.size() == 2

def test_extra_newlines():
    name1 = Vertex._make_test_vertex()
    name2 = Vertex._make_test_vertex()
    s = StringIO("2\n{0}\n\n{1}".format(name1, name2))
    assert_raises(ValueError, graph_from_file, s) 


