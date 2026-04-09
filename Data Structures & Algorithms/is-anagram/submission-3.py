class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        charSDict = defaultdict(int)
        charTDict = defaultdict(int)
        
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            charSDict[s[i]] += 1
            charTDict[t[i]] += 1

        return charSDict == charTDict
