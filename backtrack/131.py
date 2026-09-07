from typing import List
def partition(s: str) -> List[List[str]]:
    path = []
    res = []
    if not s:
        return res
    def backtracking(s, index):
        if index == len(s):
            res.append(path[:])
            return
        for i in range(index, len(s)):
            substring = s[index: i + 1]
            if substring == substring[::-1]:
                path.append(substring)
                backtracking(s, i + 1)
                path.pop()
    backtracking(s, 0)
    return res
partition("aab")