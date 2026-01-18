class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        i, n = 0, len(s)
        INT_MAX, INT_MIN = 2 ** 31 - 1, -2**31

        #step1: Whitespace
        while i < n and s[i] == " ":
            i += 1
        if i == n:
            return 0
        
        #step2: Signedness
        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1
        
        #step3&4: Conversion and Rounding
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            res = res * 10 + digit
            if res * sign >= INT_MAX:
                return INT_MAX
            elif res * sign <= INT_MIN:
                return INT_MIN
            i += 1
        return res * sign

        



        