class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        charDict = defaultdict(int)
        
        for c in s:
            charDict[c] += 1
        
        for c in t:
            if charDict[c] == 0:
                return False
            charDict[c] -= 1

        for value in charDict.values():
            if value != 0:
                return False

        return True
