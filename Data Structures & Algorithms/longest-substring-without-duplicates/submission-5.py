class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen, l, r = 0, 0, 0
        ar = set()
        while r < len(s):
            if s[r] in ar:
                print(ar)
                maxLen = max(maxLen, len(ar))
                ar.remove(s[l])
                l += 1
            else:
                ar.add(s[r])
                r += 1
        return max(maxLen, len(ar))


            