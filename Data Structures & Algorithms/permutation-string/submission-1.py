class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charSet = Counter(s1)
        curSet = defaultdict(int)
        target = len(s1)
        l = 0
        for r in range(len(s2)):
            char = s2[r]
            if char not in charSet:
                l = r + 1
                curSet = defaultdict(int)
                continue
            while charSet[char] < curSet[char] + 1:
                curSet[s2[l]] -= 1
                l += 1

            curSet[char] += 1
            if r - l + 1 == target:
                return True
        
        return False

                
