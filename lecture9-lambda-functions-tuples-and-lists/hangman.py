# Problem Set 2, hangman.py
# Name: Rafael Ederli
# Time spent: 2:00

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------

# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    for char in secret_word:
        if char in letters_guessed:
            return True
        else:
            return False

# Test 1
# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(has_player_won(secret_word, letters_guessed))

def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    word_guessed = ""
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            word_guessed += secret_word[i]
        else:
            word_guessed += "*"
    return word_guessed

# Test 2
# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_word_progress(secret_word, letters_guessed))

def get_available_letters(secret_word, letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far
    secret_word: string, the lowercase word the user is guessing

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters_guessed_str = ""
    for char in letters:
        if (char not in letters_guessed) & (char in secret_word):
            letters_guessed_str += char
    
    return letters_guessed_str

# Test 3
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_available_letters(letters_guessed))

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    guesses = 10
    letters_guessed = []

    print(secret_word)

    while guesses > 0:
        guess = input("Guess a letter: ")
        if guess in secret_word:
            letters_guessed.append(guess)
            if (len(letters_guessed) == len(secret_word)) & has_player_won(secret_word, letters_guessed):
                print("Congratulations! You won!")
                break
            else:
              print(f"The letter {guess} appears in the word.")
              print(get_word_progress(secret_word, letters_guessed))
              print(f"You still have {guesses} guesses.") if guesses > 0 else print("End Game")
        elif guess in "aeiou":
            guesses -= 1
            print(f"The vowel {guess} doesn't appear in the word. You lost a guess")
            print(get_word_progress(secret_word, letters_guessed))
            if guesses == 0:
                print("You lose")
            else:
                print(f"You still have {guesses} guesses.") if guesses > 0 else print("End Game")
        elif guess in "bcdfghjklmnpqrstvwxyz":
            guesses -= 2
            print(f"The consonant {guess} doesn't appear in the word. You lost two guesses")
            print(get_word_progress(secret_word, letters_guessed))
            if guesses == 0:
                print("You lose")
            else:
                print(f"You still have {guesses} guesses.") if guesses > 0 else print("End Game")
        elif guess == "!":
            if guesses >= 3:
                guesses -= 3
                help_letter = get_available_letters(secret_word, letters_guessed)[0]
                letters_guessed.append(help_letter)
                if (len(letters_guessed) == len(secret_word)) & has_player_won(secret_word, letters_guessed):
                    print("Congratulations! You won!")
                    break
                else:
                    print(f"The word has the letter {help_letter}")
                    print(get_word_progress(secret_word, letters_guessed))
                    print(f"You still have {guesses} guesses.") if guesses > 0 else print("End Game")
            else:
                print(f"You have only {guesses} guesses. You need at a least 3 guesses to get help.")

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

