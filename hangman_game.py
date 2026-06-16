
# TASK 1: HANGMAN GAME
import random

def choose_word():
    words = ["python", "software", "alpha", "intern", "program"]
    return random.choice(words)

def display_hangman(incorrect_guesses):
    stages = [
        "\n  --------\n  |      |\n  |      O\n  |     \\|/\n  |      |\n  |     / \\\n  -",
        "\n  --------\n  |      |\n  |      O\n  |     \\|/\n  |      |\n  |     / \n  -",
        "\n  --------\n  |      |\n  |      O\n  |     \\|/\n  |      |\n  |      \n  -",
        "\n  --------\n  |      |\n  |      O\n  |     \\|\n  |      |\n  |      \n  -",
        "\n  --------\n  |      |\n  |      O\n  |      |\n  |      |\n  |      \n  -",
        "\n  --------\n  |      |\n  |      O\n  |    \n  |    \n  |      \n  -",
        "\n  --------\n  |      |\n  |      \n  |    \n  |    \n  |      \n  -"
    ]
    return stages[incorrect_guesses]

def play_hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("=== Welcome to CodeAlpha Hangman! ===")
    
    while incorrect_guesses < max_incorrect:
        print(display_hangman(max_incorrect - incorrect_guesses))
        
        displayed_word = [letter if letter in guessed_letters else "_" for letter in word]
        print(f"Word to guess: {' '.join(displayed_word)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining lives: {max_incorrect - incorrect_guesses}")
        
        if "_" not in displayed_word:
            print(f"\nCongratulations! You guessed the word correctly: {word.upper()}")
            return

        guess = input("\nEnter a letter: ").strip().lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetical letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
            
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Oops! '{guess}' is not in the word.")
            incorrect_guesses += 1

    print(display_hangman(0))
    print(f"Game Over! You ran out of lives. The word was: {word.upper()}")

if __name__ == "__main__":
    play_hangman()
