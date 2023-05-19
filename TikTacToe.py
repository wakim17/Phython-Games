from tkinter import *


def on_click(row, col):
    global current_player

    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].configure(text=current_player)

        if check_win(current_player):
            label.configure(text="Player " + current_player + " wins the round!")
            disable_buttons()
            new_game_button.configure(state=NORMAL)
        elif is_board_full():
            label.configure(text="It's a tie!")
            disable_buttons()
            new_game_button.configure(state=NORMAL)
        else:
            current_player = "O" if current_player == "X" else "X"
            label.configure(text="Player " + current_player + "'s turn")


def check_win(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def is_board_full():
    for row in board:
        if "" in row:
            return False
    return True


def disable_buttons():
    for row in buttons:
        for button in row:
            button.configure(state=DISABLED)


def enable_buttons():
    for row in buttons:
        for button in row:
            button.configure(state=NORMAL)


def reset_board():
    global current_player
    for i in range(3):
        for j in range(3):
            buttons[i][j].configure(text="")
            board[i][j] = ""
    current_player = "X"
    label.configure(text="Player " + current_player + "'s turn")
    new_game_button.configure(state=DISABLED)
    enable_buttons()


def start_new_game():
    reset_board()
    label.configure(text="Player " + current_player + "'s turn")


# Create the main window
root = Tk()
root.title("Tic-Tac-Toe")

# Initialize the game state
board = [["", "", ""], ["", "", ""], ["", "", ""]]
current_player = "X"

# Create the buttons
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = Button(root, text="", font=("Arial", 24), width=6, height=3,
                        command=lambda r=i, c=j: on_click(r, c))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

# Create the label
label = Label(root, text="Player X's turn", font=("Arial", 18))
label.grid(row=3, columnspan=3)

# Create the "New Game" button
new_game_button = Button(root, text="New Game", font=("Arial", 16), width=10, height=2, command=start_new_game)
new_game_button.grid(row=4, columnspan=3)
new_game_button.configure(state=DISABLED)  # Disable the button initially

# Run the main loop
root.mainloop()
