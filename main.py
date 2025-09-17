import math
import os

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
        elif state == 2:
            return "X"
    elif isinstance(state, str):
        if state == "O":
            return 1
        elif state == "X":
            return 2

def input_to_grid(i):
    return math.floor((i-1)/3), (i-1) % 3 

def prompt():
    global current_play

    print("Please select a square (1-9).")
    row, column = input_to_grid(int(input("> ")))

    grid[row][column] = current_play
    current_play = 3 - current_play # hop betwene 1 and 2

def render():
    clear_cli()

    output = ""
    for i, row in enumerate(grid):
        output += f"\n{convert_state(row[0])} | {convert_state(row[1])} | {convert_state(row[2])}"
        if i<2:
            output += "\n---------"
    
    print(output)
    prompt()

while True:
    render()