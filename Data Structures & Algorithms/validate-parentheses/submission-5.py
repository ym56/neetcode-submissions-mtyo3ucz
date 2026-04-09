class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paras = {'(': ')', '{': '}', '[': ']'}
        leftPar = ['(', '{', '[']
        rightPar = [')', '}', ']']

        for i in s:
            if i in leftPar:
                stack.append(i)
            elif i in rightPar:
                if len(stack) == 0:
                    return False
                poped = stack.pop()
                if paras[poped] != i:
                    return False
        if len(stack) != 0:
            return False

        return True
            