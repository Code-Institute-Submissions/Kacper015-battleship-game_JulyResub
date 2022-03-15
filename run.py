# import random
# import time

grid = [[]]

grid_size = 10

num_of_ships = 2 

bullets_left = 50

game_over = False

ship_positions = [[]]

num_of_ships_sunk = 0 

ship_position = [[]]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """
    This will check if placing ship there will be safe to do so
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


def place_ship_on_grid(row, col, direction, length):
    global grid_size

    start_col, end_col, start_row, end_row = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "up":
        if row - lenght < 0:
            return False
        start_row = row - length + 1

    elif direction == "right":
        if col + lenght < 0:
            return False
        end_col = col + length + 1
    
    elif direction == "down":
        if row + lenght < 0:
            return False
        end_row = row + length

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)
