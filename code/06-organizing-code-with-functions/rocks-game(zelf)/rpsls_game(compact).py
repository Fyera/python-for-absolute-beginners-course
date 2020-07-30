import random


def main():
    show_header()
    play_game("Player", "Computer")


def show_header():
    print("----------------------------------------------")
    print("     Rock Paper Scissors Lizard Spock V1      ")
    print("----------------------------------------------")


def play_game(player_1, player_2):
    rounds = 3
    wins_p1 = 0
    wins_p2 = 0

    rolls = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    while wins_p1 < rounds and wins_p2 < rounds:

        roll1 = get_roll(player_1, rolls)
        # roll2 = get_roll(player_2, rolls)
        roll2 = random.choice(rolls)
        if not roll1:
            print("Try again")
            continue
        winner = check_for_winning_throw(player_1, player_2, roll1, roll2)

        if winner is None:
            print("This round was a tie!")
        else:
            print(f"{winner}")
            if f"{player_1}" in winner:
                wins_p1 += 1
                print(f"{player_1} wins the round!")
            elif f"{player_2}" in winner:
                wins_p2 += 1
                print(f"{player_2} wins the round!")
        print()
        print(f"Score is {player_1}: {wins_p1} and {player_2}: {wins_p2}.")
        print()

    if wins_p1 >= rounds:
        overall_wins = player_1
    if wins_p2 >= rounds:
        overall_wins = player_2
    print(f"{overall_wins} wins the game!")


def check_for_winning_throw(player_1, player_2, roll1, roll2):
    winner = None
    if roll1 == roll2:
        print("The play was tied")

    # Rock
    #   Rock -> tie
    #   Paper -> Lose
    #   Scissors -> Win
    #   Lizard -> Win
    #   Spock -> Lose
    elif roll1 == 'rock':
        if roll2 == 'paper':
            winner = f"{player_2}'s paper covers rock!"
        elif roll2 == 'scissors':
            winner = f"{player_1}'s rock crushes scissors!"
        elif roll2 == 'lizard':
            winner = f"{player_1}'s rock crushes lizard!"
        elif roll2 == 'spock':
            winner = f"{player_2}'s spock vaporizes rock!"
    # Paper
    #   Rock -> Win
    #   Paper -> Tie
    #   Scissors -> Lose
    #   Lizard -> Lose
    #   Spock -> Win
    elif roll1 == 'paper':
        if roll2 == 'rock':
            winner = f"{player_1}'s paper covers rock!"
        elif roll2 == 'scissors':
            winner = f"{player_2}'s scissors cuts paper!"
        elif roll2 == 'lizard':
            winner = f"{player_2}'s lizard eats paper!"
        elif roll2 == 'spock':
            winner = f"{player_1}'s paper disproves spock!"
    # Scissors
    #   Rock -> Lose
    #   Paper -> Win
    #   Scissors -> Tie
    #   Lizard -> Win
    #   Spock -> Lose
    elif roll1 == 'scissors':
        if roll2 == 'rock':
            winner = f"{player_2}'s rock crushes scissors!"
        elif roll2 == 'paper':
            winner = f"{player_1}'s scissors cuts paper!"
        elif roll2 == 'lizard':
            winner = f"{player_1}'s scissors decapitates lizard!"
        elif roll2 == 'spock':
            winner = f"{player_2}'s spock smashes scissors!"
    # Lizard
    #   Rock -> Lose
    #   Paper -> Win
    #   Scissors -> Lose
    #   Lizard -> Tie
    #   Spock -> Win
    elif roll1 == 'lizard':
        if roll2 == 'rock':
            winner = f"{player_2}'s rock crushes lizard!"
        elif roll2 == 'paper':
            winner = f"{player_1}'s lizard eats paper!"
        elif roll2 == 'scissors':
            winner = f"{player_2}'s scissors decapitates lizard!"
        elif roll2 == 'spock':
            winner = f"{player_1}'s lizard poisons spock!"
    # Spock
    #   Rock -> Win
    #   Paper -> Lose
    #   Scissors -> Win
    #   Lizard -> Lose
    #   Spock -> Tie
    elif roll1 == 'spock':
        if roll2 == 'rock':
            winner = f"{player_1}'s spock vaporizes rock!"
        elif roll2 == 'paper':
            winner = f"{player_2}'s paper disproves spock!"
        elif roll2 == 'scissors':
            winner = f"{player_1}'s spock smashes scissors!"
        elif roll2 == 'lizard':
            winner = f"{player_2}'s lizard poisons spock!"
    return winner


def get_roll(player_name, rolls):
    roll = input(f"{player_name}, What is your roll? [rock, paper, scissors, lizard, spock]: ")
    print()
    roll = roll.lower().strip()
    if roll not in rolls:
        return None
    return roll


if __name__ == '__main__':
    main()
