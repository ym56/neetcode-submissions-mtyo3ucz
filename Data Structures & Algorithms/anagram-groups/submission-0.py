class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getHash(word: str) -> List[str]:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord('a')] += 1
            return key
        res = defaultdict(list)

        for word in strs:
            key = getHash(word)
            res[tuple(key)].append(word)
        
          
        return list(res.values())