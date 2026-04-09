class Solution:
    # 4#abcd10#
    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            wordLen = len(word)
            res += str(wordLen) + '#' + word
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            wordLen = ''
            while s[i] != '#' and i < len(s):
                wordLen += s[i]
                i += 1
            i += 1
            res.append(s[i: i + int(wordLen)])
            i += int(wordLen)
        return res