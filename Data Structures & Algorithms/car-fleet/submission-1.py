class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        pairs.sort(reverse=True)
        print(pairs)
        for pos, speed in pairs:
            time = (target - pos) / speed
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        return len(stack)
