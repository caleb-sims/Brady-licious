import random
options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']


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
    print('Player 2 chose', cpu + '.')
    print('You drew.')
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
winner = 0
print('Player 2 chose', cpu + '.')

if cpu in user_class.wins:
    winner = True
elif cpu in user_class.loses:
    winner = False

if winner:
    print('You win!')
elif not winner:
    print('You lose.')