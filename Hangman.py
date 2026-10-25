import random
WORDS = ["python", "internship", "developer", "variable", "function"]

MAX_WRONG_GUESSES = 6
HANGMAN_STAGES = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========""",
]

def display_state(word, guessed_letters, wrong_guesses):
    print(HANGMAN_STAGES[len(wrong_guesses)])

    progress = ""
    for letter in word:
        if letter in guessed_letters:
            progress += letter + " "
        else:
            progress += "_ "
    print("\nWord:", progress)

    print("Wrong guesses ({}/{}): {}".format(
        len(wrong_guesses), MAX_WRONG_GUESSES, ", ".join(wrong_guesses)))


def get_guess(guessed_letters, wrong_guesses):
    """Ask the player for a single valid letter they haven't tried yet."""
    while True:
        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter (a-z).")
        elif guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed '{}'. Try a different letter.".format(guess))
        else:
            return guess


def play_game():
    """Run one round of Hangman."""
    word = random.choice(WORDS)
    guessed_letters = []   # correct guesses
    wrong_guesses = []     # incorrect guesses

    print("\n=== Welcome to Hangman! ===")
    print("The word has {} letters. You have {} incorrect guesses.".format(
        len(word), MAX_WRONG_GUESSES))

    while len(wrong_guesses) < MAX_WRONG_GUESSES:
        display_state(word, guessed_letters, wrong_guesses)

        guess = get_guess(guessed_letters, wrong_guesses)

        if guess in word:
            guessed_letters.append(guess)
            print("Good job! '{}' is in the word.".format(guess))
        else:
            wrong_guesses.append(guess)
            print("Sorry, '{}' is not in the word.".format(guess))

        if all(letter in guessed_letters for letter in word):
            display_state(word, guessed_letters, wrong_guesses)
            print("\nCongratulations! You guessed the word: {}".format(word.upper()))
            return

    display_state(word, guessed_letters, wrong_guesses)
    print("\nGame over! The word was: {}".format(word.upper()))


def main():
    """Play rounds until the player decides to quit."""
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()