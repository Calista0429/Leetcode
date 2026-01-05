from typing import List
from collections import deque
import heapq
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    
    #Solution A
    q = deque()
    res = []
    for i in range(len(nums)):
        while q and q[-1] < nums[i]:
            q.pop()
        q.append(nums[i])

        if i >= k and nums[i - k] == q[0]:
            q.popleft()
        
        if i >= k - 1:
            res.append(q[0])
    return res

    #Solution B
    
    heap = [(-nums[i], i) for i in range(k)]
    heapq.heapify(heap)
    res = [-heap[0][0]]
    for i in range(k, len(nums)):
        heapq.heappush(heap, (-nums[i], i))
        #如果当前堆顶元素的下标不在窗口内，则弹出
        while heap[0][1] <= i - k:
            heapq.heappop(heapq)
        res.append(-heap[0][0])
    return res


maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)

    


        


    
    