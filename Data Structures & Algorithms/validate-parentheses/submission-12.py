class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in bracketMap:
                if not stack or stack[-1] != bracketMap[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
                
        if stack:
            return False
        
        return True