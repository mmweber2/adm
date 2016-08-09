from collections import defaultdict

def max_flow(edges, source, sink):
    """Returns the maximum flow that can be routed from source to sink.
    
    Args:
        edges: A list of directed edge tuples of the form 
            (start, end, capacity), where start and end both represent vertices,
            and capacity represents the maximum capacity that can pass through
            this edge at once.

        source, sink: Vertex names identifying the start (source) and end (sink)
            vertices of the paths. May be numbers or strings.
            If both names are not included in edges, the maximum flow will be 0.
    """
    # TODO: Return the path and amount of capacity through each, or just the total capacity?
    # Edge format: (start, end, capacity)
    outgoing_edges = defaultdict(list)
    incoming_edges = defaultdict(list)
    for edge in edges:
        start, end, capacity = edge
        outgoing_edges[start].append(edge)
        incoming_edges[end].append(edge)
    # Initially vertex labeling
    labels = {vertex:0 for vertex in outgoing_edges}
    labels[source] = len(outgoing_edges)
    flow = {edge:0 for edge in edges}
    # Get an arbitrary edge from the source node
    first_edge = outgoing_edges[source[0]]
    # TODO: Why does the source start flowing to its first edge?
    flow[first_edge] = first_edge[2]
    excess_nodes = [first_edge[2]]
    while len(excess_nodes) > 0:
        current = excess_nodes.pop()
        pushed = False
        for edge in outgoing_edges[current]:
            v, w, capacity = edge
            if labels[w] < labels[v]:
                # Push flow to edge
                v_excess = excess(v, outgoing_edges, incoming_edges)
                flow[edge] += min(v_excess, capacity)
                pushed = True
                break
        if not pushed:
            relabel(current, outgoing_edges[current], labels)
        excess_nodes = [node for node in outgoing_edges if excess(
            node, outgoing_edges, incoming_edges) > 0]
    return sum(flow[x] for x in outgoing_edges[source]) 

def excess(v, outgoing_edges, incoming_edges):
    return incoming_edges[v][2] - outgoing_edges[v][2]

def relabel(v, v_edges, labels):
    for edge in v_edges:
        v, w, capacity = edge
        if labels[w] >= labels[v]:
            labels[v] += 1
