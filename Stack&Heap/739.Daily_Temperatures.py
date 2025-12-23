from typing import List
def dailyTemperatures(c: List[int]) -> List[int]:
    stack = []
    # res = [0 for _ in range(len(c))]
    res = [0] * len(c)
    
    # for idx, t in enumerate(c):
    #     while stack and t > stack[-1][1]:
    #         res[stack[-1][0]] = idx - stack[-1][0]
    #         stack.pop()
    #     stack.append([idx, t])
    
    for i in range(len(c)):
        while stack and c[i] > c[stack[-1]]:
            idx = stack.pop()
            res[idx] = i - idx
        stack.append(i)

    return res
dailyTemperatures([73,74,75,71,69,72,76,73])
# dailyTemperatures([30,40,50,60])