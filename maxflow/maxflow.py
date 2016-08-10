from collections import defaultdict
import math

def max_flow(edges, source, sink):
    """Returns the maximum flow that can be routed from source to sink.
    
    Args:
        edges: A list of directed edge tuples of the form 
            (start, end, capacity), where start and end both represent nodes,
            and capacity represents the maximum capacity that can pass through
            this edge at once.

            start and end may be strings or numbers, and capacity must be a
            number.

        source, sink: Node names identifying the start (source) and end (sink)
            nodes of the paths. May be numbers or strings.
            If both names are not included in edges, the maximum flow will be 0.

    Returns:
        A floating point number indicating the maximum flow that can be routed
            from source to sink through edges.
    """
    flow, labels, outgoing_edges, incoming_edges = initialize(edges, source)
    # Fill all nodes adjacent to source with the capacity of their shared edge
    excess_nodes = [edge[1] for edge in outgoing_edges[source]]
    while len(excess_nodes) > 0:
        current = excess_nodes.pop()
        pushed = False
        for edge in outgoing_edges[current]:
            v, w, capacity = edge
            if labels[w] < labels[v]:
                # Node is downhill; try to push flow to edge
                v_excess = excess(flow, outgoing_edges[v], incoming_edges[v])
                push_amount = min(v_excess, capacity - flow[edge])
                if push_amount > 0:
                    flow[edge] += push_amount
                    pushed = True
                    break
        if not pushed:
            if not relabel(current, outgoing_edges[current], labels):
                # Stop if nothing could be pushed or relabeled
                break
        # Only check nodes with outgoing edges; sink has none
        excess_nodes = [node for node in outgoing_edges if excess(
            flow, outgoing_edges[node], incoming_edges[node]) > 0]
    # Use fsum for precision in case capacities are floats
    return math.fsum(flow[x] for x in incoming_edges[sink]) 

def initialize(edges, source):
    """Helper function for max_flow to organize nodes and edges."""
    outgoing_edges = defaultdict(list)
    incoming_edges = defaultdict(list)
    for edge in edges:
        start, end, capacity = edge
        outgoing_edges[start].append(edge)
        incoming_edges[end].append(edge)
    all_nodes = outgoing_edges.keys() + incoming_edges.keys()
    labels = {node:0 for node in all_nodes}
    # Initialize label of source to be able to flow to anything adjacent
    labels[source] = len(all_nodes)
    flow = {edge:0 for edge in edges}
    # Initialize all source edges to have maximum flow for their capacity
    for source_edge in outgoing_edges[source]:
        flow[source_edge] = source_edge[2]
    return flow, labels, outgoing_edges, incoming_edges

def excess(flow, outgoing, incoming):
    """Helper function for max_flow to determine excess of a node."""
    out_flow = sum(flow[edge] for edge in outgoing)
    in_flow = sum(flow[edge] for edge in incoming)
    return in_flow - out_flow

def relabel(v, v_edges, labels):
    """Helper function for max_flow to raise the label of a node."""
    for edge in v_edges:
        v, w, capacity = edge
        if labels[w] >= labels[v]:
            labels[v] += 1
            return True
    return False
