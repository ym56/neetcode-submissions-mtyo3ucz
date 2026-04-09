class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) 
        stack = []

        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                curI, curV = stack.pop()
                res[curI] = i - curI
            stack.append((i, v))
        return res 

            
