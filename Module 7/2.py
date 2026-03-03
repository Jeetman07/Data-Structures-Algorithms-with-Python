def BFS(graph, start):
    """
    Perform Breadth-First Search of the graph starting from Vertex start.
    """
    from collections import deque

    visited = {start: None}
    queue = deque([start])

    while queue:
        current = queue.popleft()

        for neighbor in graph._adj_map[current]:
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)

    return visited