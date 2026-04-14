class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        curSet = set()
        l = 0
        res = 0

        for i in range(0, len(s)):
            while s[i] in curSet:
                curSet.remove(s[l])
                l += 1
            curSet.add(s[i])
            res = max(len(curSet), res)
        
        return res

