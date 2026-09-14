from collections import deque
from typing import List
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    in_degree = [0] * numCourses
    adj = [[] for _ in range(numCourses)]
    for cur, pre in prerequisites:
        in_degree[cur] += 1
        adj[pre].append(cur)
    q = deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            q.append(i)
    count = 0
    while q:
        count += 1
        node = q.popleft()
        for nb in adj[node]:
            in_degree[nb] -= 1
            if in_degree[nb] == 0:
                q.append(nb)
    return count == numCourses
canFinish(5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]])