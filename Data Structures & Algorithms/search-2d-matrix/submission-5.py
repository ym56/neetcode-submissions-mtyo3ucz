class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:   
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, (rows * cols) - 1

        while l <= r:
            mid = l + (r - l) // 2
            midr = mid // cols
            midc = mid % cols
            if matrix[midr][midc] == target:
                return True
            elif matrix[midr][midc] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
