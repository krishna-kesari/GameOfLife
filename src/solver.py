#---------------------------- TASK 1 ----------------------------
def count_neighbors(grid, row, col):
    """
    Counts the number of alive neighbors for a specific cell in the grid.
    A cell can have up to 8 neighbors (horizontal, vertical, and diagonal).
    
    Args:
        grid (list of lists): The current 2D state of the game.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        
    Returns:
        int: The total number of alive neighbors (0 to 8).
    """
    
    alive_count = 0
    
    # TODO: Implement your neighbor-counting logic here!
    
    #Count the number of alive neighbors surrounding cell (row, col).
    #Checks all 8 directions. Skips cells outside the grid boundary.
    
    rows = len(grid)
    cols = len(grid[0])
    

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue          # skip the cell itself

            r = row + dr
            c = col + dc

            if 0 <= r < rows and 0 <= c < cols:   # stay inside the grid
                if grid[r][c] == 1:
                   alive_count += 1

    
    return alive_count

#---------------------------- TASK 2 ----------------------------
def compute_next_generation(grid):
    """
    Generates the next state of the grid based on Conway's rules.
    
    Args:
        grid (list of lists): The current 2D state of the game.
        
    Returns:
        list of lists: A BRAND NEW 2D grid representing the next generation.
        
    Note:
        - Do NOT modify the original `grid` directly while iterating through it. 
          You must create a new grid to store the updated states, otherwise 
          your changes will mess up the neighbor counts for subsequent cells!
    """
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Create a new blank grid of the same size, filled with 0s (dead cells)
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # TODO: Iterate through every cell in the `grid`.


    # Build a fresh grid and never modify the original mid-step
    next_grid = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            neighbors = count_neighbors(grid, r, c)
            alive = grid[r][c] == 1

            if alive:
                # Rule 1  Underpopulation: fewer than 2 neighbours then dies
                # Rule 3  Overpopulation: more than 3 neighbours then dies
                # Rule 2  Survival: 2 or 3 neighbours → lives on
                next_grid[r][c] = 1 if neighbors in (2, 3) else 0
            else:
                # Rule 4  Reproduction: exactly 3 neighbours then becomes alive
                next_grid[r][c] = 1 if neighbors == 3 else 0



    return next_grid