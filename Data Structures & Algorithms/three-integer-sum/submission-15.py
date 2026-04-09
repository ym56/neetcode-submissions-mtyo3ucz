class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            target = -nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                cur = nums[l] + nums[r]
                if cur == target:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                elif cur < target:
                    l += 1
                else:
                    r -= 1
        
        return [list(t) for t in res]