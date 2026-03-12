def dfs(graph,start,visited):
    if start in visited:
        return
    visited.add(start)
    print(start,end=" ")
    for neighbor in graph[start]:
        dfs(graph,neighbor,visited)


adj_list = {
    1:[2,3],
    2:[1,5,6],
    3:[1,4,7],
    4:[3,8],
    5:[2],
    6:[2],
    7:[3,8],
    8:[4,7]
}
visit = set()
dfs(adj_list,18 ,visit)
