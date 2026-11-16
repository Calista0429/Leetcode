def digitSum(s: str, k: int) -> str:
    if not s or not k:
        return ""
 
    while len(s) > k:
        next_part = []
        for i in range(0, len(s), k):
            group = s[i: i + k]
            group_sum = sum(int(ch) for ch in group)
            next_part.append(str(group_sum))
        s = ''.join(next_part)
    return s
digitSum(s = "11111222223", k = 3)