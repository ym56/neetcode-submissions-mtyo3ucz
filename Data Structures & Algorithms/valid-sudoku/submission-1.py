class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        len = 9
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell.isdigit():
                    digit = float(cell)
                    square = (i // 3) * 3 + j // 3
                    print(square)
                    if digit in rows[i] or digit in cols[j] or digit in squares[square]:
                        return False
                    rows[i].add(digit)
                    cols[j].add(digit)
                    squares[square].add(digit)

        return True
