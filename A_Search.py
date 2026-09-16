import heapq

def a_star_search(graph, start, goal, heuristic):
    open_set = [(0, start, [start])]
    g_score = {start: 0}
    while open_set:
        _, node, path = heapq.heappop(open_set)
        if node == goal:
            return path
        for neighbor, cost in graph.get(node, []):
            tentative = g_score[node] + cost
            if neighbor not in g_score or tentative < g_score[neighbor]:
                g_score[neighbor] = tentative
                f = tentative + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, neighbor, path + [neighbor]))
    return None
