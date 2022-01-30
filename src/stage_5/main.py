import random

words = ["python", "java", "kotlin", "javascript"]
tries = 8

def main() -> None:
    print("H A N G M A N")

    secret = random.choice(words)
    to_guess = set(secret)

    def print_state() -> None:
        print("".join("-" if x in to_guess else x for x in secret))

    for _ in range(tries):
        print()
        print_state()
        guess = input("Input a letter: ")
        if guess in to_guess:
            to_guess.remove(guess)
        else:
            print("That letter doesn't appear in the word")

    print()
    print("Thanks for playing!")
    print("We'll see how well you did in the next stage")


if __name__ == "__main__":
    main()