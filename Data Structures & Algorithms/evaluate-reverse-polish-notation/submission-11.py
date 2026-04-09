class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            print(stack)
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(token))
        return stack.pop()