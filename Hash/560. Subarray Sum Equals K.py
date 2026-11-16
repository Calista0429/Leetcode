from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    numSum = 0
    res = 0
    prefixSum = {0: 1}
    for n in nums:
        numSum += n
        diff = numSum - k
        res += prefixSum.get(diff, 0)
        prefixSum[numSum] = prefixSum.get(numSum, 0) + 1
    return res

subarraySum(nums = [1,1,1], k = 2)
# 这个方法的思路是，通过一个累加和，让这个累加和与k做差，
# 得到前缀和，并在hash表中查找这个前缀和出现过几次。
# 在数学上就是 numSum - 历史上某个前缀和 = k
# 那么 历史上某个前缀和 = numSum - k, 因此我们需要将每次计算得到的
# 前缀和出现次数保存到哈希表中
    