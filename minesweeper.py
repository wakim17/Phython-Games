import tkinter as tk
import tkinter.messagebox as messagebox
import random

MINE_SYMBOL = 'X'

class MinesweeperGame:
    def __init__(self, rows, cols, mine_count):
        self.rows = rows
        self.cols = cols
        self.mine_count = mine_count
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.mine_locations = set()
        self.game_over = False

    def place_mines(self):
        indices = random.sample(range(self.rows * self.cols), self.mine_count)
        for index in indices:
            row = index // self.cols
            col = index % self.cols
            self.board[row][col] = -1
            self.mine_locations.add((row, col))

    def update_counts(self):
        for row, col in self.mine_locations:
            for i in range(max(0, row - 1), min(row + 2, self.rows)):
                for j in range(max(0, col - 1), min(col + 2, self.cols)):
                    if self.board[i][j] != -1:
                        self.board[i][j] += 1

    def reveal(self, row, col):
        if self.game_over:
            return

        if self.board[row][col] == -1:
            self.game_over = True
            self.show_all_mines()
            messagebox.showinfo("Game Over", "You hit a mine! Game over.")
        elif self.board[row][col] == 0:
            self.reveal_zeroes(row, col)

    def reveal_zeroes(self, row, col):
        queue = [(row, col)]
        visited = set(queue)

        while queue:
            current_row, current_col = queue.pop(0)
            self.board[current_row][current_col] = -2  # Mark cell as visited

            for i in range(max(0, current_row - 1), min(current_row + 2, self.rows)):
                for j in range(max(0, current_col - 1), min(current_col + 2, self.cols)):
                    if self.board[i][j] == 0 and (i, j) not in visited:
                        queue.append((i, j))
                        visited.add((i, j))

    def show_all_mines(self):
        for row, col in self.mine_locations:
            self.board[row][col] = -1

    def is_game_won(self):
        for row in self.board:
            for cell in row:
                if cell >= 0:
                    return False
        return True


class MinesweeperGUI:
    def __init__(self, rows, cols, mine_count):
        self.rows = rows
        self.cols = cols
        self.mine_count = mine_count

        self.window = tk.Tk()
        self.window.title("Minesweeper")
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]

        self.game = MinesweeperGame(rows, cols, mine_count)
        self.create_board()
        self.game.place_mines()
        self.game.update_counts()

    def create_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                button = tk.Button(
                    self.window,
                    width=2,
                    command=lambda row=row, col=col: self.reveal_cell(row, col),
                    disabledforeground='black'
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def reveal_cell(self, row, col):
        if self.game.board[row][col] != -2:  # Check if cell is already visited
            self.game.reveal(row, col)
            self.update_button_text(row, col)
            if self.game.is_game_won():
                self.game_over("Congratulations! You won the game.")

    def update_button_text(self, row, col):
        cell_value = self.game.board[row][col]
        button = self.buttons[row][col]
        button.config(state='disabled', bg='light gray')
        if cell_value == -1:
            button.config(text=MINE_SYMBOL, bg='red')
        elif cell_value > 0:
            button.config(text=str(cell_value))

    def game_over(self, message):
        for row in self.buttons:
            for button in row:
                button.config(state='disabled')
        messagebox.showinfo("Game Over", message)


# Game setup
rows = 8
cols = 8
mine_count = 10

# Create and play the game
minesweeper = MinesweeperGUI(rows, cols, mine_count)
minesweeper.window.mainloop()
