class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        path = []
        if not digits:
            return result
        d_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                 "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def backtracking(index):
            if index == len(digits):
                result.append("".join(path))
                return
            for letter in d_map[digits[index]]:
                path.append(letter)
                backtracking(index + 1)
                path.pop()
        backtracking(0)
        return result



        

        
        