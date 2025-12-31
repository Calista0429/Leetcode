from collections import Counter

def removeDuplicateLetters(s: str) -> str:
    stack = []
    scount = Counter(s) #{'a': 1, 'b': 2, 'c': 2}
    visited = set()
    for char in s:
        
        scount[char] -= 1

        if char in visited:
            continue
            
        while stack and stack[-1] > char and scount[stack[-1]] > 0:
            visited.remove(stack[-1])
            stack.pop()
        stack.append(char)
        visited.add(char)
    return ''.join(stack)




        