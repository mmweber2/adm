from collections import defaultdict
from time import sleep

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
    flow, labels, outgoing_edges, incoming_edges = initialize(edges, source)
    excess_nodes = [edge[1] for edge in outgoing_edges[source]]
    while len(excess_nodes) > 0:
        current = excess_nodes.pop()
        pushed = False
        for edge in outgoing_edges[current]:
            v, w, capacity = edge
            if labels[w] < labels[v]:
                # Push flow to edge
                v_excess = excess(flow, outgoing_edges[v], incoming_edges[v])
                print "Trying to push excess {} to edge {}".format(v_excess, edge)
                push_amount = min(v_excess, capacity-flow[edge])
                if push_amount <= 0:
                    print "Could not push more"
                else:
                    flow[edge] += push_amount
                    # Remove excess from outgoing edge
                    pushed = True
                    break
        if not pushed:
            if not relabel(current, outgoing_edges[current], labels):
                break
        excess_nodes = [node for node in outgoing_edges if excess(
            flow, outgoing_edges[node], incoming_edges[node]) > 0
            # once filled, sink will always have positive excess
            and node is not sink]
    return sum(flow[x] for x in incoming_edges[sink]) 

def initialize(edges, source):
    outgoing_edges = defaultdict(list)
    incoming_edges = defaultdict(list)
    for edge in edges:
        start, end, capacity = edge
        outgoing_edges[start].append(edge)
        incoming_edges[end].append(edge)
    all_vertices = outgoing_edges.keys() + incoming_edges.keys()
    labels = {vertex:0 for vertex in all_vertices}
    labels[source] = len(all_vertices)
    flow = {edge:0 for edge in edges}
    # Initialize all source edges to have maximum flow
    for source_edge in outgoing_edges[source]:
        flow[source_edge] = source_edge[2]
    return flow, labels, outgoing_edges, incoming_edges

def excess(flow, outgoing, incoming):
    out_flow = sum(flow[edge] for edge in outgoing)
    in_flow = sum(flow[edge] for edge in incoming)
    return in_flow - out_flow

def relabel(v, v_edges, labels):
    for edge in v_edges:
        v, w, capacity = edge
        if labels[w] >= labels[v]:
            labels[v] += 1
            return True
    return False
