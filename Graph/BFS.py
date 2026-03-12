from collections import deque


def bfs(graph,start):
    visited_list = set()
    queue = deque([start])

    visited_list.add(start)

    while queue:
        node = queue.popleft()
        print(node,end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited_list:
                visited_list.add(neighbor)
                queue.append(neighbor)

adj_list = {
    1 : [2,3],
    2 : [1,4,5],
    3 : [1,6,7],
    4 : [2],
    5 : [2],
    6 : [3,8],
    7 : [3,10],
    8 : [6,9],
    9 : [8,10],
    10 : [7,9]
}
bfs(adj_list,1)


