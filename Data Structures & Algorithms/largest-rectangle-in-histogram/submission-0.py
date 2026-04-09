class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pre, suf = [], []
        size = len(heights)
        maxPre, maxSuf = 0, 0
        leftMost = [-1] * size
        for i in range(size):
            while pre and heights[pre[-1]] >= heights[i]:
                pre.pop()
            if pre:
                leftMost[i] = pre[-1]
            pre.append(i)
        print(leftMost)

        rightMost = [size] * size
        for i in range(size - 1, -1, -1):
            while suf and heights[suf[-1]] >= heights[i]:
                suf.pop()
            if suf:
                rightMost[i] = suf[-1]
            suf.append(i)
        print(rightMost)

        maxArea = 0
        for i in range(size):
            leftMost[i] += 1
            rightMost[i] -= 1
            maxArea = max(maxArea, heights[i] * (rightMost[i] -  leftMost[i] + 1))
        return maxArea