class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return None

        lmap = {}
        size = end = 0

        for idx, ch in enumerate(s):
            lmap[ch] = idx

        res = []
        for idx, ch in enumerate(s):
            size += 1
            end = max(end, lmap[ch])
            if idx == end:
                res.append(size)
                size = 0
        return res


