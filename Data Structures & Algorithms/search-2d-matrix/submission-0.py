class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen, colLen = len(matrix), len(matrix[0])
        def binary (start: int, end: int) -> bool:
            if start > end:
                return False
            mid = start + (end - start) // 2
            midCol = mid % colLen
            minRow = mid // colLen
            midNum = matrix[minRow][midCol]
            print(start, mid, end)
            print(midNum, target)
            if midNum == target:
                print('found target')
                return True
            elif midNum > target:
                return binary(start, mid - 1)
            else:
                return binary(mid + 1, end)
        hi = binary(0, colLen * rowLen - 1)
        print(hi)
        return hi