import tkinter as tk
from tkinter import messagebox
import random

# List of words for the game
words = [
    "python", "hangman", "programming", "computer", "game", "the", "and", "that", "have", "for", "not",
    "with", "you", "this", "but", "his", "from",
    "they", "say", "her", "she", "will", "one", "all", "would",
    "there", "their", "what", "out",  "about", "who", "get", "which",
    "when", "make", "can", "like", "time", "just", "him", "know",
    "take", "person", "into", "year", "your", "good", "some", "could", "them", "see",
    "other", "than", "then", "now", "look", "only", "come", "its", "over", "think",
    "also", "back", "after", "use", "two", "how", "our", "work", "first", "well",
    "way", "even", "new", "want", "because", "any", "these", "give", "day", "most"
]

# Initialize game variables
secret_word = random.choice(words)
guesses = []
max_attempts = 6

def draw_gallows(incorrect_guesses):
    # Draw the gallows
    canvas.create_line(20, 380, 180, 380)
    canvas.create_line(100, 380, 100, 20)
    canvas.create_line(100, 20, 250, 20)
    canvas.create_line(250, 20, 250, 50)

    if incorrect_guesses >= 1:
        draw_head()

    if incorrect_guesses >= 2:
        draw_body()

    if incorrect_guesses >= 3:
        draw_left_arm()

    if incorrect_guesses >= 4:
        draw_right_arm()

    if incorrect_guesses >= 5:
        draw_left_leg()

    if incorrect_guesses >= 6:
        draw_right_leg()

def draw_head():
    # Draw the head
    canvas.create_oval(225, 50, 275, 100)

def draw_body():
    # Draw the body
    canvas.create_line(250, 100, 250, 250)

def draw_left_arm():
    # Draw the left arm
    canvas.create_line(250, 150, 200, 100)

def draw_right_arm():
    # Draw the right arm
    canvas.create_line(250, 150, 300, 100)

def draw_left_leg():
    # Draw the left leg
    canvas.create_line(250, 250, 200, 300)

def draw_right_leg():
    # Draw the right leg
    canvas.create_line(250, 250, 300, 300)

def draw_word():
    # Draw the word with dashes for unrevealed letters
    display_word = ""
    for char in secret_word:
        if char in guesses:
            display_word += char
        else:
            display_word += "-"
    canvas.create_text(200, 350, text=display_word, font=("Helvetica", 20), fill="black")

def handle_guess(event):
    # Get the guessed letter
    guessed_letter = entry.get().lower()
    entry.delete(0, tk.END)

    # Check if the guessed letter is correct
    if guessed_letter in secret_word:
        guesses.append(guessed_letter)
        draw_word()
    else:
        # Incorrect guess
        incorrect_guesses = len(guesses)
        if incorrect_guesses == max_attempts:
            # Last attempt, game over
            guesses.append(guessed_letter)
            draw_word()
            draw_gallows(incorrect_guesses)
            messagebox.showinfo("Hangman Game", "Game Over! The word was: " + secret_word)
            restart_game()
        else:
            # Increment incorrect guesses count and draw the corresponding body part
            guesses.append(guessed_letter)
            draw_word()
            draw_gallows(incorrect_guesses)

def restart_game():
    if messagebox.askyesno("Hangman Game", "Do you want to play again?"):
        # Reset game variables
        global secret_word, guesses
        secret_word = random.choice(words)
        guesses = []

        # Clear the canvas
        canvas.delete("all")

        # Start a new game
        draw_gallows(0)
        draw_word()

# Initialize the game window
window = tk.Tk()
window.title("Hangman Game")

# Create the canvas for drawing
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Bind the Enter key to the guess handler
window.bind("<Return>", handle_guess)

# Create the entry widget for guessing
entry = tk.Entry(window, font=("Helvetica", 20))
entry.pack()
entry.focus_set()

# Start the game
draw_gallows(0)
draw_word()

# Start the tkinter main loop
tk.mainloop()