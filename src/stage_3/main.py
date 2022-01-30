import random

words = ["python", "java", "kotlin", "javascript"]

def main() -> None:
    print("H A N G M A N")
    secret = random.choice(words)
    guess = input("Guess the word: ")

    if guess == secret:
        print("You survived!")
    else:
        print("You lost!")

if __name__ == "__main__":
    main()

    