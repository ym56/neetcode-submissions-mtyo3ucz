class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            target = -nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[r] + nums[l]
                if total == target:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                if total < target:
                    l += 1
                if total > target:
                    r -= 1
                

        return [list(t) for t in res]