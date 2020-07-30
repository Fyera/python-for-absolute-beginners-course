import random


def main():
    show_header()
    play_game()


def show_header():
    print("-------------------------------------------------------------")
    print("                       M&M guessing game!                    ")
    print("-------------------------------------------------------------")
    print()
    print("Guess the number of M&Ms and you get a lunch on the house. You have 5 attempts!")
    print()


def play_game():
    mm_count = random.randint(1, 100)
    attempt_limit = 5
    attempts = 0
    attempts = guess_attempts(attempt_limit, attempts, mm_count)
    if attempts == 5:
        print(f"Sorry, you've used up your {attempts} attempts. Better luck next time!")


def guess_attempts(attempt_limit, attempts, mm_count):
    while attempts < attempt_limit:
        guess_text = input("How many M&Ms are in the jar? ")
        guess = int(guess_text)

        if mm_count == guess:
            print(f"You won a free lunch! It was {guess}.")
            print(f"You've guessed it in {attempts+1} attempts.")
            break
        elif guess < mm_count:
            attempts += 1
            print("Sorry, that's too LOW!")
        else:
            attempts += 1
            print("Sorry, that's too HIGH!")
    return attempts


if __name__ == '__main__':
    main()
