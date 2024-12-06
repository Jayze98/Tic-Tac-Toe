import tkinter as tk
from tkinter import messagebox

# Initialize main variables
current_player = "X"
xstate = [0] * 9
zstate = [0] * 9

# Define the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Functions to handle the game logic
def check_win():
    # Define all winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for combo in win_combinations:
        if xstate[combo[0]] and xstate[combo[1]] and xstate[combo[2]]:
            messagebox.showinfo("Game Over", "Player X wins!")
            reset_game()
            return True
        elif zstate[combo[0]] and zstate[combo[1]] and zstate[combo[2]]:
            messagebox.showinfo("Game Over", "Player O wins!")
            reset_game()
            return True
    
    if all(xstate[i] or zstate[i] for i in range(9)):  # Check for a tie
        messagebox.showinfo("Game Over", "It's a tie! :(")
        reset_game()
        return True
    
    return False

def reset_game():
    global xstate, zstate, current_player
    xstate = [0] * 9
    zstate = [0] * 9
    current_player = "X"
    for button in buttons:
        button.config(text="", state="normal")

def on_click(index):
    global current_player
    if current_player == "X":
        xstate[index] = 1
        buttons[index].config(text="X", state="disabled")
        if check_win() is False:
            current_player = "O"
    else:
        zstate[index] = 1
        buttons[index].config(text="O", state="disabled")
        if check_win() is False:
            current_player = "X"

# Create a 3x3 grid of buttons
buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=('normal', 20), width=5, height=2,
                       command=lambda i=i: on_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Start the GUI loop
root.mainloop()

