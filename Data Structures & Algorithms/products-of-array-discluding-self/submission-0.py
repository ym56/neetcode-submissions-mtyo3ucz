class Solution:
    # pre: 1, 1, 2, 8
    # suf: 48, 24, 6, 1
    # res: 48, 24, 12, 8
    # [i] = pre[i] * suf[i]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        suf = [0] * len(nums)
        pre[0] = suf[len(nums) - 1] = 1
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i - 1]
        for i in range(len(suf) - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]
        res = [0] * len(nums)
        for i in range(len(res)):
            res[i] = pre[i] * suf[i]
        return res
