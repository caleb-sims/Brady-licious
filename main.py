import random
options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
cpu_wins = 0
user_wins = 0
play_again = 'Y'

while play_again in ['y']:


    # 1: Take Inputs
    user = input('Enter Rock, Paper, Scissors, Lizard, or Spock:\n')
    cpu = options[random.randint(0,4)]


    # 2: Check For Invalid Input

    # a: Input not in domain
    while user not in options:
        print('Error: invalid input')
        user = input('Enter Rock, Paper, Scissors, Lizard, or Spock:\n')

    # b: Input equals cpu input
    while cpu == user:
        print(f'Player 2 chose {cpu}.')
        print('You drew.')
        cpu = options[random.randint(0,4)]
        user = input('Enter Rock, Paper, Scissors, Lizard, or Spock:\n')


    # 3: Create Classes

    class Game():   # parent class
        def __init__(self):
            self.wins = []
            self.loses = []

    class Rock(Game):
        def __init__(self):
            super().__init__()
            self.wins = ['Scissors', 'Lizard']
            self.loses = ['Paper', 'Spock']

    class Paper(Game):
        def __init__(self):
            super().__init__()
            self.wins = ['Rock', 'Spock']
            self.loses = ['Scissors', 'Lizard']

    class Scissors(Game):
        def __init__(self):
            super().__init__()
            self.wins = ['Paper', 'Lizard']
            self.loses = ['Rock', 'Spock']

    class Lizard(Game):
        def __init__(self):
            super().__init__()
            self.wins = ['Paper', 'Spock']
            self.loses = ['Rock', 'Scissors']

    class Spock(Game):
        def __init__(self):
            super().__init__()
            self.wins = ['Scissors', 'Rock']
            self.loses = ['Paper', 'Lizard']


    # 4: Apply Input to Respective Class

    user_class = 0

    if user == 'Rock':
        user_class = Rock()
    elif user == 'Paper':
        user_class = Paper()
    elif user == 'Scissors':
        user_class = Scissors()
    elif user == 'Lizard':
        user_class = Lizard()
    elif user == 'Spock':
        user_class = Spock()


    # 5: Find Winner

    def get_winner(cpu, wins_list):
        winner = 0
        if cpu in wins_list:
            winner = True
        elif cpu in wins_list:
            winner = False
        return winner


    print(f'Player 2 chose {cpu}.')

    if get_winner(cpu, user_class.wins):
        print('You win!')
        user_wins +=1
    elif not get_winner(cpu, user_class.wins):
        print('You lose.')
        cpu_wins +=1


    # 6: Play again?

    play_again = input('Press "Y" to play again or "N" to end the game:\n').lower()


print(f'Player wins: {user_wins}')
print(f'CPU wins: {cpu_wins}')

