def dfs(graph, start, target, visited=None):
    if visited is None:
        visited = set()
    if start == target:
        return [start]
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            path = dfs(graph, neighbor, target, visited)
            if path:
                return [start] + path
    return None
