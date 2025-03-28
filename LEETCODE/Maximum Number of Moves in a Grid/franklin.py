class Solution:
    def maxMoves(self, grid):
        counter = 0
        rows = set(range(len(grid)))
        columns = list(range(len(grid[0])))

        for column in columns[: len(columns) - 1]:
            new_rows = set()

            for row in rows:
                new_rows = new_rows.union(self.moves(grid, row, column))

            if new_rows:
                rows = new_rows
                counter += 1

            else:
                break

        return counter

    def moves(self, grid, row, column):
        new_rows = set()
        grid_value = grid[row][column]
        next_column = column + 1

        if row - 1 >= 0 and grid[row - 1][next_column] > grid_value:
            new_rows.add(row - 1)

        if grid[row][next_column] > grid_value:
            new_rows.add(row)

        if row + 1 < len(grid) and grid[row + 1][next_column] > grid_value:
            new_rows.add(row + 1)

        return new_rows


solution = Solution()
max_moves = solution.maxMoves(
    [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]
)
print(max_moves)


"""
(0, 0) ==>
    (0, 1)
    (1, 1)

(1, 0) ==>
    (0, 1)
    (1, 1)
    (2, 1)

(2, 0) ==>  
    (1, 1)
    (2, 1)
    (3, 1)

(3, 0) ==>
    (2, 1)
    (3, 1)
"""
