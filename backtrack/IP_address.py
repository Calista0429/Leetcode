class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        path = []

        def backtracking(index):
            if len(path) > 4:
                return 
            if len(path) == 4 and index == len(s):
                res.append('.'.join(path))
                return
            for i in range(index, len(s)):
                sub = s[index: i + 1]
                if int(sub) > 255:
                    continue
                if int(sub) == 0 and index != i:
                    continue
                if int(sub) > 0 and sub[0] == '0':
                    continue
                path.append(sub)
                backtracking(i + 1)
                path.pop()
        backtracking(0)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))  # Example usage