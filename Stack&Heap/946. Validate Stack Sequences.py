from typing import List
def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    stack = []
    i = 0
    for num in pushed:
        stack.append(num)
        while stack and stack[-1] == popped[i]:
            stack.pop()
            i += 1
    return len(stack) == 0

validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2])
        