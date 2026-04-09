class MinStack:
    def __init__(self):
        self.extra = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        extraVal = val
        if len(self.extra) > 0:
            extraVal = min(self.extra[-1], val)
        self.extra.append(extraVal)

    def pop(self) -> None:
        self.stack.pop()
        self.extra.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.extra)
        return self.extra[-1]
