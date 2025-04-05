import requests
import random
random.seed() #increase likelyhood of an unseen word
import tkinter
import os

# Ensure the folder exists
os.makedirs("Code_Challenge", exist_ok=True)


word_cache = {} # Initialize cache dictionary
letters_guessed = [] #Initialize player guess list. Could probably move to mainloop()

def populate_cache():
    """Gets words of multiple lengths (4-10) and store them in cache, ensuring they contain only letters.
       DataMuse chosen API to avoid the hassel of getting API keys. """
    lengths_to_fetch = list(range(4, 11))  # Generate lengths 4 to 10
    
    for length in lengths_to_fetch:
        pattern = "?" * length
        url = f"https://api.datamuse.com/words?sp={pattern}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            words = [word["word"] for word in data if word["word"].isalpha()]  # Filter non-alpha words
            
            if words:
                word_cache[length] = words  # Store words in cache

def get_random_word():
    """Retrieve a random alphabetic word from cached lengths.
       We are organizing our cache into lists based on word lengths.
       To increase randomization we first pick a random key (length)
       then a random word from that list."""
    if not word_cache:  # If cache is empty, populate it
        populate_cache()
    
    # Select a random length from available cached keys
    length = random.choice(list(word_cache.keys()))

    # Shuffle the list of words for the selected length
    random.shuffle(word_cache[length])
    
    # Retrieve a random word from that length's list
    if word_cache[length]:  
        return word_cache[length].pop()  # Remove and return a word
    
    return "No word found!"

def guess_logic(user_letter, secret_word, word_progress):
    """Guess individual letters. We are organizing this logic to first
       check that the guess is a single char. within our secret word or at least a new guess.
       in this version the player recieves a penalty for repeatedly guessing
       the same letter. Second, to help the player keep track of their guesses
       we show them a list of their previous guesses just above their word progress."""
    input_string = len(user_letter)
    if input_string > 1:
        print("Only input one letter at a time\n")
        return 0
    
    if user_letter in secret_word or user_letter not in letters_guessed:
        if user_letter not in secret_word:
            print("Try again")
            letters_guessed.append(user_letter)
            print(f"previously guessed letters\n{letters_guessed}")
            print(word_progress)
            return 1
        for i in range(len(secret_word)):
            if secret_word[i] == user_letter:
                word_progress[i] = user_letter

        
        letters_guessed.append(user_letter)
    else:
        print("You already guessed that letter")

    print(f"previously guessed letters\n{letters_guessed}")
    print(word_progress)
    
    return 0


def mainloop():
    """This is where the magic happens. The outer while to manage and reset repeated games
       Inner while takes care of the actual user inputs and progress. To avoid unwanted games
       and a potentially lower score in the player's file, only when the user explicitly states
       they want to play again will a new word be given."""
    guess_count = 0
    play_again = True
    
    while(play_again):
        secret_word = get_random_word()
        word_progress = ["_ " for _ in range(len(secret_word))]

        while("_ " in word_progress and guess_count < 7):
            #display the length of the mystery word using '_' eg: apple = _ _ _ _ _
            #prompt user to guess a letter
            #fill in the correct letter if the user picks a correct letter eg apple: 'e' = _ _ _ _ e eg: 'p' = _ p p _ _
            #if letter not in word "guess again" prompt, all of user's attempts are tracked and displayed
            # when user fills in word "Congrats" and score text displayed eg: "Congrats!" score 100 * inverse/score - incorrect penalty
            # inverse score assigns more value to words that are uncommon
            # save user's words and scores to a file
            # Prompt user to play again.
            # at end of game close user's info file, cache is cleared, new cache is generated on each program execution
            #print(secret_word)
            guess = input(f"guess a letter for a {len(secret_word)} letter word:").lower()
            guess_count += guess_logic(guess,secret_word, word_progress)

        if guess_count == 7:
            print(f"Sorry...the word was {secret_word}")
        else:
            formatted_score = f"{(len(secret_word) / guess_count) * 100:.2f}"  # Format to 2 decimal places
            with open("Code_Challenge/hangman_scores.txt", "a") as game_history:
                game_history.write(f"{secret_word}: score: {formatted_score} total guesses: {guess_count}\n")

            print(f"You did it! Your final score for {secret_word} was {formatted_score}!")
        play_again = input("Do you want to play again?: yes/no\n")
        if play_again != "yes":
            play_again = False
        else:
            letters_guessed.clear()
            guess_count = 0

    return 

def main():
    """Main game loop kept in a separate function to allow for quickly switching out functions for tests.
       Potential to add GUI features (opening screen, end game screen, etc.) """
    mainloop()
    print("Thanks For Playing!")
    
    return 0

if __name__ == "__main__":
    main()