class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        charDictS = defaultdict(int)
        charDictT = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            charDictS[s[i]] += 1
            charDictT[t[i]] += 1
        
        return charDictS == charDictT


