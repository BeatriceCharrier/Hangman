import random

words = ["python", "java", "kotlin", "javascript"]

def main() -> None:
    print("H A N G M A N")
    secret = random.choice(words)
    hint = secret[:3] + "-" * (len(secret) - 3)
    guess = input(f"Guess the word {hint}: ")

    if guess == secret:
        print("You survived!")
    else:
        print("You lost!")


if __name__ == "__main__":
    main()