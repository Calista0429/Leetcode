from typing import List
import heapq
def isPossibleDivide(nums: List[int], k: int) -> bool:
    if len(nums) % k != 0:
        return False
    counter = {}
    for n in nums:
        counter[n] = 1 + counter.get(n, 0)
    heap = list(counter.keys())
    heapq.heapify(heap)
    while heap:
        first = heap[0]
        for i in range(first, first + k):
            if i not in counter:
                return False
            counter[i] -= 1
            if counter[i] == 0:
                if heap[0] != i:
                    return False
                heapq.heappop(heap)
    return True

isPossibleDivide(nums = [1,2,3,3,4,4,5,6], k = 4)
    