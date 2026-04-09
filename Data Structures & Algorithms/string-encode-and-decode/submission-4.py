class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += '#'
            res += str(len(word))
            res += '#'
            for i in word:
                res += i
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        curWord = ''
        sizeStr = ''
        size = -1
        inSize = False
        if not s:
            return []
        for i in s:
            if size > 0:
                curWord += i
                size -= 1
                continue
            if i == '#':
                if not inSize:
                    if curWord:
                        res.append(curWord)
                    curWord = ''
                    inSize = True
                    continue
                else:
                    inSize = False
                    size = int(sizeStr)
                    if not size:
                        res.append('')
                    sizeStr = ''
                    curWord = ''
                    continue
            if inSize:
                sizeStr += i
        if curWord:
            res.append(curWord)
        return res

