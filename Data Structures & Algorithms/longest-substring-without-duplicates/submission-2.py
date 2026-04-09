class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen, l, r = 0, 0, 0
        ar = []
        while r < len(s):
            if s[r] in ar:
                print(ar)
                maxLen = max(maxLen, len(ar))
                l += 1
                ar = ar[1:]
            else:
                ar.append(s[r])
                r += 1
        return max(maxLen, len(ar))


            