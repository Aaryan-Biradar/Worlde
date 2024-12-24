# Wordle Game (Python)

This is a simple terminal-based Wordle game implemented in Python. The game selects a random 5-letter English word and the player has six attempts to guess the word. Feedback is provided after each guess in the form of color-coded letters to indicate correct and incorrect guesses.

## Features

- **Random Word Generator**: The game selects a random 5-letter word from a list of valid English words.
- **Color-Coded Feedback**: After each guess, letters are color-coded based on their correctness:
  - **Green** for correct letters in the correct position.
  - **Yellow** for correct letters in the wrong position.
  - **Red** for incorrect letters.
- **Valid Word Check**: The game ensures that each guess is a valid 5-letter English word.
- **Interactive Keyboard Display**: The status of each letter in the word is updated after every guess.

## Requirements

Before running the game, you need to install the required Python libraries. You can install them by running:

```bash
pip install termcolor random-words nltk
```
- Additionally, `nltk` needs to download its word corpus the first time it is run. This is automatically handled within the script.

## How to Play

- 1 Run the Python script:
```bash
  python wordle.py
```
- 2 The game will prompt you to guess a 5-letter word.

- 3 After each guess, you will see color-coded feedback:
  - Green means the letter is correct and in the correct position.
  - Yellow means the letter is correct but in the wrong position.
  - Red means the letter is incorrect.

- 4 You have 6 attempts to guess the word. If you guess the word correctly, you win; otherwise, the game will reveal the word at the end.

- 5 After completing a game, you can press `q` to quit or any other key to play again.

## Code Explanation

  - The program uses the `RandomWords` library to generate a random 5-letter word.
  - It validates the guess to ensure it's a valid English word, and ensures it's the correct length (5 letters).
  - It uses the `termcolor` library to colorize the feedback (green, yellow, red).
  - The `nltk` library is used to validate the guess against a set of valid English words.


















