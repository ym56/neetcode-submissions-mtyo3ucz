class Solution:
    def isNumber(self, token) -> bool:
        try:
            int(token)
            return True
        except:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if self.isNumber(token):
                stack.append(int(token))
            elif token == '+':
                num1 = stack[-1]
                stack.pop()
                num2 = stack[-1]
                stack.pop()
                stack.append(num1 + num2)
                print(stack)
            elif token == '-':
                num1 = stack[-1]
                stack.pop()
                num2 = stack[-1]
                stack.pop()
                stack.append(num2 - num1)
                print(stack)
            elif token == '*':
                num1 = stack[-1]
                stack.pop()
                num2 = stack[-1]
                stack.pop()
                stack.append(num1 * num2)
                print(stack)
            elif token == '/':
                num1 = stack[-1]
                stack.pop()
                num2 = stack[-1]
                stack.pop()
                stack.append(int(num2 / num1))
                print(stack)
        return stack[-1]
