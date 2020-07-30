import random

rolls = {
    'rock': {
        'defeats': ['scissors', 'lizard'],
        'defeated_by': ['paper', 'spock']
    }, 'paper': {
        'defeats': ['rock', 'spock'],
        'defeated_by': ['scissors', 'lizard']
    }, 'scissors': {
        'defeats': ['paper', 'lizard'],
        'defeated_by': ['rock', 'spock']
    }, 'lizard': {
        'defeats': ['paper', 'spock'],
        'defeated_by': ['rock', 'scissors']
    }, 'spock': {
        'defeats': ['rock', 'scissors'],
        'defeated_by': ['paper', 'lizard']
    }
}


def main():
    show_header()
    play_game("Player", "Computer")


def show_header():
    print("----------------------------------------------")
    print("     Rock Paper Scissors Lizard Spock V4      ")
    print("           Data Structure Edition             ")
    print("----------------------------------------------")


def play_game(player_1, player_2):
    wins = {player_1: 0, player_2: 0}
    # wins[player_1]=0
    # wins[player_2]=0

    roll_names = list(rolls.keys())

    while not find_winner(wins, wins.keys()):

        roll1 = get_roll(player_1, roll_names)
        # roll2 = get_roll(player_2, roll_names)
        roll2 = random.choice(roll_names)

        if not roll1:
            print("Try again")
            continue

        print(f"{player_1} rolls {roll1}")
        print(f"{player_2} rolls {roll2}")

        winner = check_for_winning_throw(player_1, player_2, roll1, roll2)

        if winner is None:
            print("This round was a tie!")
        else:
            print(f"{winner} takes the round!")
            wins[winner] += 1
        print(f"Current win status: {wins}")
        print()
        print(f"Score is {player_1}: {wins[player_1]} and {player_2}: {wins[player_2]}.")
        print()

    # if wins_p1 >= rounds:
    #     overall_wins = player_1
    # if wins_p2 >= rounds:
    #     overall_wins = player_2
    overall_winner=find_winner(wins, wins.keys())
    print(f"{overall_winner} wins the game!")


def find_winner(wins, names):
    best_of = 3
    for name in names:
        if wins.get(name, 0) >= best_of:
            return name
    return None


def check_for_winning_throw(player_1, player_2, roll1, roll2):
    winner = None
    if roll1 == roll2:
        print("The play was tied")
    outcome = rolls.get(roll1, {})
    # print(f"{roll1}-->{outcome}")
    if roll2 in outcome.get('defeats'):
        return player_1
    elif roll2 in outcome.get('defeated_by'):
        return player_2
    return winner


def get_roll(player_name, roll_names):
    print("Avaliable rolls")
    for index, r in enumerate(roll_names, start=1):
        print(f"{index}. {r}")
    # -1 zodat het overeen komt met de index
    selected_index = int(input(f"{player_name}, What is your roll? ")) - 1
    print()
    if selected_index < 0 or selected_index >= len(rolls):
        print(f"Sorry {player_name}, {selected_index + 1} is out of bounds!")
        return None
    return roll_names[selected_index]


if __name__ == '__main__':
    main()
