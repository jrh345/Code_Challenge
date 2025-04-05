# Hangman Game

This is a Python implementation of a word guessing game. Players attempt to guess a hidden word by suggesting letters in the least attempts. The game uses the Datamuse API to fetch random words of varying lengths.

## Features

- Randomly selects a word for the player to guess using the Datamuse API.
- Tracks the player's guesses and displays progress.
- Provides feedback for repeated guesses.
- Calculates and displays a score based on the player's performance.
- Saves game history (words, scores, and guesses) to a the hangman_scores.txt file. 
- This file will be made within a new "Code_Challenge" directory.

## How to Play

1. The program will display the length of the mystery word using underscores (e.g., `_ _ _ _ _` for a 5-letter word).
2. Guess one letter at a time (all letters are in lowercase).
3. If the guessed letter is correct, it will be revealed in the word.
4. If the guessed letter is incorrect, it will count as a failed attempt.
5. The game ends when:
   - The player guesses the word correctly.
   - The player quits the program.

## How to Run

1. **Prerequisites**:
   - Python 3.x installed on your system.
   - Internet connection (required to fetch words from the Datamuse API).

2. **Steps**:
   - Clone or download this repository.
   - Open a terminal and navigate to the folder containing `hangman.py`. Most likely "Code_Challenge"
   - Run the program using the following command:
     ```bash
     python hangman.py
     ```
     or
     ```bash
     python3 hangman.py
     ```

3. Follow the on-screen instructions to play the game.

## File Structure

- `hangman.py`: The main Python script for the Hangman game.
- `hangman_scores.txt`: A file where the game saves the player's scores and history.
- [README.md](http://_vscodecontentref_/1): This file, providing an overview of the project.

## Requirements

- Python 3.x
- `requests` library (used to fetch words from the Datamuse API).

## Installing Dependencies

If the `requests` library is not installed, you can install it using pip:
```bash
pip install requests