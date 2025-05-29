from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        positions = [-1]*n

        def placing(path, positions, row):
            if row == n:
                results.append(path[:])
                return
            for col in range(n):
                if is_valid(positions, row, col):
                    positions[row] = col
                    path.append(make_row(col, n))
                    placing(path, positions, row+1)
                    path.pop()
                    positions[row] = -1

        
        def is_valid(positions: List[int], row: int, col: int):
            for row_x in range(row):
                col_x = positions[row_x]
                if col == col_x or abs(col_x-col) == abs(row_x - row):
                    return False
            return True

        def make_row(col, n):
            return '.' * col + 'Q' + '.' * (n - col - 1)
        
        placing([], positions, 0)
        return results
