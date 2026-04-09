class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(start, end) -> int:
            if start > end:
                return -1
            m = start + (end - start) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                return bs(m + 1, end)
            else:
                return bs(0, m - 1)
        
        return bs(0, len(nums) - 1)
                