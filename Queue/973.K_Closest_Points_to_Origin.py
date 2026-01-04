from typing import List
import heapq
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    counter = {}
    z = lambda p: p[0]**2 + p[1]**2
    for i in range(len(points)):
        counter[i] = z(points[i])
    heap = []
    for key, val in counter.items():
        heapq.heappush(heap,(val, key))
    res = []
    while len(res) < k:
        res.append(points[heapq.heappop(heap)[1]])
    return res

kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2)
        