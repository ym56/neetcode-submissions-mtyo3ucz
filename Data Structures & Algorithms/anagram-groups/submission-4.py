class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        def getHash(s):
            stringHash = [0] * 26

            for let in s:
                stringHash[ord(let) - ord('a')] += 1

            return stringHash

        
        for s in strs:
            res[tuple(getHash(s))].append(s)


        return list(res.values())