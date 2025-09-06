import random
import time
import os
from colorama import Fore, Style

# -------- Clear terminal screen --------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# -------- Color functions --------
def lght_cyn(text):
    return Fore.LIGHTCYAN_EX + f"{text}" + Style.RESET_ALL

def lght_rd(text):
    return Fore.LIGHTRED_EX + f"{text}" + Style.RESET_ALL

def col_yellow(text):
    return Fore.YELLOW + f"{text}" + Style.RESET_ALL

def col_green(text):
    return Fore.GREEN + f"{text}" + Style.RESET_ALL

def col_blue(text):
    return Fore.BLUE + f"{text}" + Style.RESET_ALL

# -------- Simulated processing --------
def Check():
    for i in range(5):
        print("Comparing" + "." * (i & 4), end='\r')
        time.sleep(random.uniform(0.4, 0.6))

# -------- Main Hangman Game Function --------
def hangman():
    clear()
    words = ["python", "computer", "programming", "hangman", "developer", "keyboard"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    used_letters = []
    intro = "Welcome to Hangman!"
    print(lght_cyn(intro))
    print(lght_cyn("Word:"), " ".join(guessed))
    while attempts > 0 and "_" in guessed:
        guess = input(col_green("Guess a letter or word: ")).lower()
        if not guess.isalpha():
            print(lght_rd("Enter letters or a word!\n"))
            continue
        if len(guess) == 1:
            if guess in used_letters:
                print(col_yellow("You already guessed that letter!\n"))
                time.sleep(2)
                continue
            used_letters.append(guess)
            if guess in word:
                Check()
                print(col_blue("Good guess!\n"))
                time.sleep(2)
                clear()
                for i, letter in enumerate(word):
                    if letter == guess:
                        guessed[i] = guess
            else:
                Check()
                attempts -= 1
                print(lght_rd(f"Wrong! Attempts left: {attempts}\n"))
                time.sleep(2)
                clear()
        else:
            if guess == word:
                guessed = list(word)
                print(col_blue("Good guess!\n"))
                time.sleep(2)
                clear()
            else:
                attempts -= 1
                print(lght_rd(f"Wrong! Attempts left: {attempts}\n"))
                time.sleep(2)
                clear()
        print(lght_cyn("Word:"), " ".join(guessed))
        if len(guess) == 1:
            print(lght_cyn("Used letters:"), ", ".join(used_letters), "\n")
    if "_" not in guessed:
        print(col_green("Congratulations! You guessed the word:"), word, "\n")
    else:
        print(col_green("Game over! The word was:"), word, "\n")

# -------- Play Again Loop --------
if __name__ == "__main__":
    hangman()
    while True:
        again = input(col_green("Do you want to play again? (y/n): ")).lower()
        if again != "y":
            print(col_green("Goodbye!"))
            break
        else:
            clear()
            hangman()