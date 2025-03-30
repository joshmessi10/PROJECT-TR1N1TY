from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def dfs(x, y, moves):
            if y == len(grid[0]) - 1:
                return moves
            max_moves = moves
            directions = [(-1, 1), (0, 1), (1, 1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] > grid[x][y]:
                    max_moves = max(max_moves, dfs(nx, ny, moves + 1))
            
            return max_moves
        
        max_result = 0
        for start_row in range(len(grid)):
            max_result = max(max_result, dfs(start_row, 0, 0))
        
        return max_result

solution = Solution()
print(solution.maxMoves([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]))
        
