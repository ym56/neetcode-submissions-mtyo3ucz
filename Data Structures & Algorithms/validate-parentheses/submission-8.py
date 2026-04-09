class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ['(', '{', '[']
        for para in s:
            if para in left:
                stack.append(para)
            else:
                if not stack:
                    return False
                if para == ')' and stack[-1] != '(':
                    return False
                elif para == '}' and stack[-1] != '{':
                    return False
                elif para == ']' and stack[-1] != '[':
                    return False
                stack.pop()
        
        if stack:
            return False
        return True