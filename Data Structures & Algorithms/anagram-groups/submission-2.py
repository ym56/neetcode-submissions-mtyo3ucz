class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sumToWords = defaultdict(list)

        for word in strs:
            wordHash = [0] * 26
            for char in word:
                wordHash[ord(char) - ord('a')] += 1
            sumToWords[tuple(wordHash)].append(word)

        return list(sumToWords.values())