def twoSum(nums: list[int], target: int) -> list[int]:
        seen = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], idx]
            seen[] = idx
        return []

twoSum(nums = [2,7,11,15], target = 9)
