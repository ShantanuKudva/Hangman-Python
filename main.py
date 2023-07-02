import random

def check_win(player,computer):
    # if player == computer:
    #     return f"Its a Tie! You chose {player} and computer chose {computer}"
    # elif player == 'rock' and computer == 'paper':
    #     return f"Computer wins! You chose {player} and computer chose {computer}"
    # elif player == 'rock' and computer == 'scissors':
    #     return f"You win! You chose {player} and computer chose {computer}"
    # elif player == 'paper' and computer == 'rock':
    #     return f"You win! You chose {player} and computer chose {computer}"
    # elif player == 'paper' and computer == 'scissors':
    #     return f"Computer wins! You chose {player} and computer chose {computer}"
    # elif player == 'scissors' and computer == 'rock':
    #     return f"Computer wins! You chose {player} and computer chose {computer}"
    # elif player == 'scissors' and computer == 'paper':
    #     return f"You win! You chose {player} and computer chose {computer}"

    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    if player == computer:
        return f"It's a Tie! You chose {player} and computer chose {computer}"
    elif winning_combinations[player] == computer:
        return f"You win! You chose {player} and computer chose {computer}"
    else:
        return f"Computer wins! You chose {player} and computer chose {computer}"


def get_choices():
    options = ['rock', 'paper', 'scissors']
    player_choice = input("Enter a choice (rock, paper, scissors) \n")
    computer_choice = random.choice(options)
    choices = {'player': player_choice, 'computer': computer_choice}
    response = check_win(choices['player'], choices['computer'])
    print(response)



get_choices()

