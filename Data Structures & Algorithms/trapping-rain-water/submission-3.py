class Solution:
    def trap(self, height: List[int]) -> int:
        pre, suf = [], []
        maxPre = 0
        maxSuf = 0
        for i in range(len(height)):
            maxPre = max(height[i], maxPre)
            pre.append(maxPre)
            maxSuf = max(height[-(i + 1)], maxSuf)
            suf.append(maxSuf)
        suf = suf[::-1]

        res = 0
        waterAtIndex = []
        for i in range(len(height)):
            waterAtIndex.append(max(min(pre[i], suf[i]) - height[i], 0))
            res += max(min(pre[i], suf[i]) - height[i], 0)
        return res    