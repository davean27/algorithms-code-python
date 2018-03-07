def bfs(graph, root) :
    queue = []
    visited = []

    queue.append(root)

    while queue :
        node = queue.pop(0)
        if node not in visited :
            visited.append(node)
            for child in [x for x in graph[node] if x not in visited] :
                queue.append(child)

    return visited


graph = {0 : [1, 5],
         1 : [0, 2, 3],
         2 : [1, 4],
         3 : [1, 4, 5],
         4 : [2, 3, 5],
         5 : [0, 3, 4]}



print(bfs(graph, 0))