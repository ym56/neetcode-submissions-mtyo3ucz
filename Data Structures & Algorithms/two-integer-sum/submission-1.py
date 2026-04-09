class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetSet = {}
        for idx, num in enumerate(nums):
            if num in targetSet:
                return [targetSet[num], idx]
            else:
                targetSet[target - num] = idx
