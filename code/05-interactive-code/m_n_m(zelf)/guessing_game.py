import random

print("-------------------------------------------------------------")
print("                       M&M guessing game!                    ")
print("-------------------------------------------------------------")

mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0

print("Guess the number of M&Ms and you get a lunch on the house. You have 5 attempts!")
print()

while attempts < attempt_limit:
    guess_text = input("How many M&Ms are in the jar? ")
    guess = int(guess_text)
    attempts += 1

    if mm_count == guess:
        print(f"You won a free lunch! It was {guess}.")
        break
    elif guess < mm_count:
        print("Sorry, that's too LOW!")
    else:
        print("Sorry, that's too HIGH!")

print(f"Bye, you are done in {attempts}")
