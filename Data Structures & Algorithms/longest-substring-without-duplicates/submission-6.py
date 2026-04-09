class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        cur = ''

        for char in s:
            if char in cur:
                while char in cur:
                    cur = cur[1:]
            cur += char
            res = max(res, len(cur))
        return res
