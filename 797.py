def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    path = [0]
    res = []
    n = len(graph)
    def dfs(node):
        if node == n - 1:
            res.append(path[:])
            return
    
        for node in graph[node]:
            path.append(node)
            dfs(graph, node, path, res)
            path.pop()
    dfs(graph, 0, path, res)
    return res
allPathsSourceTarget(graph = [[1,2],[3],[3],[]])
    