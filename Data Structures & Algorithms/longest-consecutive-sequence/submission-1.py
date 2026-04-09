class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in numSet:
            # Start of set
            if num - 1 not in numSet:
                streak = 1
                target = num + 1
                while target in numSet:
                    streak += 1
                    target += 1

                res = max(res, streak)

        return res   