import random

LIST = ["r", "p", "s"]
def get_player_choice():
    """Get user input and validate it is one of the choices above"""
    player_choice = NoneO
    while player_choice is None:
        player_choice = input('Choices: \n(R)ock \n(P)aper \n(S)cissors \n\nPick: ')
        if player_choice.lower() not in LIST:
            player_choice = None
    return player_choice.lower()






def get_computer_choice(LIST):
    computer_choice = random.choice(LIST)
    return computer_choice

def edge_case_draw(player_choice, computer_choice):
    if computer_choice == player_choice:
        return True


def print_winner(player_choice, computer_choice):
    if player_choice == "r" and computer_choice == "s":
        print("Rock beats Scissors, User Wins!")
    elif player_choice == "p" and computer_choice == "r":
        print("Paper beats Rock, User Wins!")
    elif player_choice == "s" and computer_choice == "p":
        print("Scissors beats Paper, User Wins!")
    else:
        print('Computer wins!')
        print('%s beats %s' % (computer_choice, player_choice))


def play_game():
    """play the game"""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice(LIST)
    if edge_case_draw(player_choice, computer_choice):
        print("It's a draw, both players picked %s: " % player_choice)
    else:
        print("Computer picked: %s" % computer_choice)
        print("Player picked: %s" % player_choice)
        print_winner(player_choice, computer_choice)


if __name__ == "__main__":
    play_game()
