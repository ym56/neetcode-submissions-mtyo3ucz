class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in numSet:
            if num - 1 not in numSet:
                count = 1
                nextNum = num + 1
                while nextNum in numSet:
                    count += 1
                    nextNum += 1
                if count > res:
                    res = count
        
        return res

