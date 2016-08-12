from collections import defaultdict
import math

def max_flow(edges, source, sink):
    """Returns the maximum flow that can be routed from source to sink.

    Uses the push-relabel algorithm (also known as pre-flow push) to push
        flow to nodes, then divert any excess flow at the nodes to 'downhill'
        (lower labeled) nodes until the flow reaches sink.
    
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
    flow, labels, outgoing_edges, incoming_edges = _initialize(edges, source)
    # Fill all nodes adjacent to source with the capacity of their shared edge
    excess_nodes = [edge[1] for edge in outgoing_edges[source]]
    while len(excess_nodes) > 0:
        current = excess_nodes.pop()
        pushed = _push(
                outgoing_edges[current], incoming_edges[current], labels, flow)
        if not (pushed or _relabel(outgoing_edges[current], labels)):
            # Try next node if nothing could be pushed or relabeled
            continue
        # Only check nodes with outgoing edges
        excess_nodes = [node for node in outgoing_edges if _excess(
            flow, outgoing_edges[node], incoming_edges[node]) > 0]
    # Use fsum for precision in case capacities are floats
    return math.fsum(flow[x] for x in incoming_edges[sink]) 

def _initialize(edges, source):
    """Creates data structures of nodes and edges for max_flow."""
    # Track all outgoing and incoming edges for each node
    outgoing_edges = defaultdict(list)
    incoming_edges = defaultdict(list)
    for edge in edges:
        start, end, capacity = edge
        outgoing_edges[start].append(edge)
        incoming_edges[end].append(edge)
    all_nodes = outgoing_edges.keys() + incoming_edges.keys()
    # Labels or heights of nodes; flow can only flow to a smaller labeled node
    labels = {node:0 for node in all_nodes}
    # Source can flow to any other node
    labels[source] = len(all_nodes)
    # Amount of flow (<= capacity) for each edge
    flow = {edge:0 for edge in edges}
    # All edges start with 0 flow, except for edges adjacent to source,
    # which have maximum flow for their capacity
    for source_edge in outgoing_edges[source]:
        flow[source_edge] = source_edge[2]
    return flow, labels, outgoing_edges, incoming_edges

def _excess(flow, outgoing, incoming):
    """Returns the amount of excess flow (if any) for a single node."""
    out_flow = sum(flow[edge] for edge in outgoing)
    in_flow = sum(flow[edge] for edge in incoming)
    return in_flow - out_flow

def _relabel(v_edges, labels):
    """Raises the label of a node such that it can push to more edges."""
    for edge in v_edges:
        v, w, capacity = edge
        if labels[w] >= labels[v]:
            labels[v] += 1
            return True
    # Nothing to relabel
    return False

def _push(edges_out, edges_in, labels, flow):
    """Pushes flow from a node to one of its edges."""
    for edge in edges_out:
        v, w, capacity = edge
        if labels[w] < labels[v]:
            # Node is downhill; try to push flow to edge
            v_excess = excess(flow, edges_out, edges_in)
            push_amount = min(v_excess, capacity - flow[edge])
            if push_amount > 0:
                flow[edge] += push_amount
                return True
    # Could not push to any edges
    return False
