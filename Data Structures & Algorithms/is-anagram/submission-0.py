class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        test1 = {}
        for i in s:
            if i not in test1:
                test1[i] = 0
            
            test1[i] += 1
        
        for i in t:
            if i not in test1:
                test1[i] = 0
            test1[i] -= 1

        for i in test1.values():
            if (i != 0):
                return False

        return True

            