import heapq
def frequencySort(s: str) -> str:
    counter = {}
    for char in s:
        counter[char] = 1 + counter.get(char, 0)

    # heap = []
    # for key,val in counter.items():
    #     #(-2, e)
    #     heapq.heappush(heap, (-val, key))
    # res = ""
    # while len(res) < len(s):
    #     mchar = heapq.heappop(heap)
    #     times = -mchar[0]
    #     chars = mchar[1]
    #     for i in range(times):
    #         res += chars
    # return res
    freq = [[] for _ in range(len(s) + 1)]
    for key, val in counter.items():
        freq[val].append(key)
    res = ""
    
    for i in range(len(freq) - 1, -1, -1):
        for char in freq[i]:
            res += i * char
    
    return res

frequencySort(s = "tree")