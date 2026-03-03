def DFS(graph, vertex, visited=None):
    if visited is None:
        visited = {vertex: None}

    for neighbor in graph._adj_map[vertex]:
        if neighbor not in visited:
            visited[neighbor] = vertex
            DFS(graph, neighbor, visited)

    return visited