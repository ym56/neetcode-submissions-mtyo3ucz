class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        o = {}
        for i, v in enumerate(nums):
            if v in o:
                return [o[v], i]
            o[target - v] = i
        return []