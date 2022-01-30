import random
import sys

words = ["python", "java", "kotlin", "javascript"]

def play() -> bool:
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: ')
        if choice == "exit":
            sys.exit(0)
        elif choice == "play":
            return True

def main() -> None:
    print("H A N G M A N")

    tries = 8
    secret = random.choice(words)
    to_guess = set(secret)
    guessed = set()

    def print_state() -> None:
        print("".join("-" if x in to_guess else x for x in secret))

    while play():
        while tries:
            print()
            print_state()
            guess = input("Input a letter: ")

            if len(guess) != 1:
                print("You should input a single letter")
            elif not (guess.isascii() and guess.islower()):
                print("Please enter a lowercase English letter")
            elif guess in guessed:
                print("You've already guessed this letter")
            elif guess in to_guess:
                to_guess.remove(guess)
                guessed.add(guess)
            else:
                print("That letter doesn't appear in the word")
                guessed.add(guess)
                tries -= 1

            if not to_guess:
                print()
                print_state()
                print("You guessed the word!")
                print("You survived!")
                print()
                break
        else:
            print("You lost!")
            print()

if __name__ == "__main__":
    main()