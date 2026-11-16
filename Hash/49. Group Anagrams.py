from collections import defaultdict
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        res[tuple(count)].append(s)
    # return list(res.values())
    print(list(res.values()))
groupAnagrams(strs=['eat', 'tea','ant', 'tna', 'abc'])

# 这种方法的思路是，使用一个长度为26个英文字母长度的数组，来保存每个单词的字母个数
# 类似于对每一个单词做 one-hot encoding, 具有相同字母组成的单词的one-hot 是一样的
# 然后用相同的one hot 数组作为key, 单词作为值，记录相同字母组成的所有单词
# 例如 [0, 1, 0, ...., 0]: [eat, tea, ate]