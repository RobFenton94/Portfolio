def minesweeper(grid):
    """Generates a minesweeper grid where each '-' is replaced by the count of adjacent mines."""
    # Get the dimensions of the grid.
    rows = len(grid)
    columns = len(grid[0]) if rows > 0 else 0

    def count_mines(r, c):
        """Counts mines around a cell at position (r, c)."""
        # List of possible adjacent positions (8 directions).
        adjacent_positions = [
            (r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
            (r, c - 1),                 (r, c + 1),
            (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)
        ]
        mine_count = 0
        # Check each adjacent cell.
        for pos in adjacent_positions:
            adj_r, adj_c = pos
            # Ensure the position is within grid bounds.
            if 0 <= adj_r < rows and 0 <= adj_c < columns:
                # Increment count if there's a mine.
                if grid[adj_r][adj_c] == '#':
                    mine_count += 1
        return mine_count

    # Create a new grid to store the counts of adjacent mines.
    new_grid = []
    for r in range(rows):
        new_row = []
        for c in range(columns):
            if grid[r][c] == '#':
                # Copy the mine indicator to the new grid.
                new_row.append('#')
            else:
                # Calculate and add the number of adjacent mines.
                new_row.append(str(count_mines(r, c)))
        new_grid.append(new_row)

    return new_grid


# Example grid input.
input_grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# Generate and print the output grid.
output_grid = minesweeper(input_grid)
for row in output_grid:
    print(row)
