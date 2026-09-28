import heapq

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    open_set = [(heuristic(start, goal), start, [start])]
    while open_set:
        _, node, path = heapq.heappop(open_set)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(open_set, (heuristic(neighbor, goal), neighbor, path + [neighbor]))
    return None
