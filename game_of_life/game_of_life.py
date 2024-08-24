# based on shinjanpatra's python implementation available at
# https://www.geeksforgeeks.org/program-for-conways-game-of-life/


import time


# Function to print next generation
def next_generation(grid):
    n_rows, n_cols = len(grid), len(grid[0])

    future = [[0 for i in range(n_cols)] for j in range(n_rows)]

    # Loop through every cell
    for y in range(n_rows):
        for x in range(n_cols):
            # finding no Of Neighbours that are alive
            alive_eighbours = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (y + i >= 0 and y + i < n_rows) and (x + j >= 0 and x + j < n_cols):
                        alive_eighbours += grid[y + i][x + j]

            # The cell needs to be subtracted from
            # its neighbours as it was counted before
            alive_eighbours -= grid[y][x]

            # Implementing the Rules of Life

            # Cell is lonely and dies
            if (grid[y][x] == 1) and (alive_eighbours < 2):
                future[y][x] = 0

            # Cell dies due to over population
            elif (grid[y][x] == 1) and (alive_eighbours > 3):
                future[y][x] = 0

            # A new cell is born
            elif (grid[y][x] == 0) and (alive_eighbours == 3):
                future[y][x] = 1

            # Remains the same
            else:
                future[y][x] = grid[y][x]

    return future


# Displaying the grid
def print_grid(grid):
    for row in grid:
        for field in row:
            if field == 0:
                print("  ", end="")
            else:
                print(" O", end="")
        print()
    print()


if __name__ == "__main__":
    g = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    prev_g = []

    while True:
        g = next_generation(g)

        if g == prev_g:
            break

        print("\033[2J\033[0;0HGame Of Life")
        print_grid(g)

        prev_g = g

        time.sleep(0.1)
