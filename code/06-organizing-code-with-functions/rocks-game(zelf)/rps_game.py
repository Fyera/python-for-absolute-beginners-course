import random


def main():
    show_header()
    # player_1 = input("Enter player 1's name: ")
    # player_2 = input("Enter player 2's name: ")
    player = "You"
    ai = "Computer"
    play_game(player, ai)


def show_header():
    print("----------------------------------------------")
    print("     Rock Paper Scissors Lizard Spock V1      ")
    print("----------------------------------------------")


def play_game(player_1, player_2):
    rolls = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    roll1 = get_roll(player_1, rolls)
    # roll1_input = input("What is your roll? [rock, paper, scissors, lizard, spock]: ")
    # roll1 = roll1_input.lower().strip()
    # roll2_input = input(f"{player_2}, what is your roll? [rock, paper, scissors, lizard, spock]: ")
    # roll2 = roll2_input.lower().strip()
    roll2 = random.choice(rolls)
    if not roll1:
        print("Can't play that, exiting")
        return
    # if roll1 not in rolls:
    # print(f"Sorry {player_1}, {roll1} is not a valid play!")
    # if roll2 not in rolls:
    # print(f"Sorry {player_2}, {roll2} is not a valid play!")

    # test for a winner
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
    print("The game is settled!")
    if winner is None:
        print("It was a tie!")
    else:
        print(f"{winner}")


def get_roll(player_name, rolls):
    roll = input(f"{player_name}What is your roll? [rock, paper, scissors, lizard, spock]: ")
    roll = roll.lower().strip()
    if roll not in rolls:
        # print(f"Sorry {player_name}, {roll} is not a valid play!")
        return None
    return roll


if __name__ == '__main__':
    main()
