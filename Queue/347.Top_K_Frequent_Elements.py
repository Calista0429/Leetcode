import heapq
from collections import Counter
from typing import List
def topKFrequent(nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return None
        counter = Counter(nums)
        #Solution A
        # sorted_counter = sorted(counter.items(), key = lambda item: item[1], reverse=True)
        # res = []
        # for t in sorted_counter:
        #     res.append(t[0])
        #     if len(res) == k:
        #         return res

        #Solution B
        # heap = []
        # for key,val in counter.items():
        #     heapq.heappush(heap, [-val, key])
        # res = []
        # while len(res) < k:
        #     res.append(heapq.heappop(heap)[1])
        # return res

        #Solution C
        freq = [[] for _ in range(len(nums) + 1)]

        for key,val in counter.items():
              freq[val].append(key)
        res = []
        for i in range(len(freq)-1, -1, -1):
              for n in freq[i]:
                    res.append(n)
                    if len(res) == k:
                          return res
        


nums = [1,1,1,2,2,3]
k = 2
# nums = [1]
# k = 1
topKFrequent(nums,k)