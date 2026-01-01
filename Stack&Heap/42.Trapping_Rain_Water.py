from typing import List
def trap(height: List[int]) -> int:
    stack = []
    area = 0
    
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            mid = stack.pop()
            if stack:
                pre = stack[-1]
                h = min(height[i], height[pre])
                w = i - pre - 1
                area += h * w
        stack.append(i)
    return area

trap(height=[0,1,0,2,1,0,1,3,2,1,2,1])

        