import math
import os
from time import sleep as wait

current_play = 1
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def clear_cli():
    os.system("cls")

def convert_state(state):
    if state == 0:
        return " "

    if isinstance(state, int):
        if state == 1:
            return "O"
        elif state == 4:
            return "X"
    elif isinstance(state, str):
        if state == "O":
            return 1
        elif state == "X":
            return 4

def win_condition():
    for row in grid:
        if sum(row) == 3:
            return "O"
        if sum(row) == 12:
            return "X"
    for column in range(3):
        if grid[0][column] + grid[1][column] + grid[2][column] == 3:
            return "O"
        if grid[0][column] + grid[1][column] + grid[2][column] == 12:
            return "X"
    if grid[0][0] + grid[1][1] + grid[2][2] == 3:
        return "O"
    if grid[0][0] + grid[1][1] + grid[2][2] == 12:
        return "X"
    if grid[0][2] + grid[1][1] + grid[2][0] == 3:
        return "O"
    if grid[0][2] + grid[1][1] + grid[2][0] == 12:
        return "O"
    return None


def input_to_grid(i):
    return math.floor((i-1)/3), (i-1) % 3 

def prompt():
    global current_play

    print("Please select a square (1-9).")
    row, column = input_to_grid(int(input("> ")))

    if grid[row][column] != 0:
        print("Invalid input - selection is already filled.")
        return wait(2)

    grid[row][column] = current_play
    current_play = 5 - current_play # hop betwene 1 and 4

def render():
    clear_cli()

    output = ""
    for i, row in enumerate(grid):
        output += f"\n{convert_state(row[0])} | {convert_state(row[1])} | {convert_state(row[2])}"
        if i<2:
            output += "\n---------"
    
    print(output)

    victor = win_condition()
    if victor:
        print(f"Player {victor} has won!")
        return exit()

    prompt()

while True:
    render()