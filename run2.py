import random
import time 

grid = [[]]

grid_size = 10 

num_of_ships = 2 

bullets_left = 50

game_over = False

num_of_ships_sunk = 0

ship_positions = [[]]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def make_grid():
    """
    This will creata a 10x10 grid
    """
    global grid
    global grid_size
    global num_of_ships
    global ship_positions

    random.seed(time.time())

    rows, cols = (grid_size, grid_size)

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        grid.append(row)

    num_of_ships_placed = 0

    ship_positions = []


def print_grid():
    """
    This will print a grid into the terminal
    """
    global alphabet
    global grid

    debug_mode = True

    alphabet = alphabet[0: len(grid) +1]

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")


def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """
    This will check the row or column to see if able to place ship 
    """
    global grid
    global ship_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid