import random

options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

user = input('Enter Rock, Paper, Scissors, Lizard, or Spock:\n')
cpu = options[random.randint(0,4)]

while user not in options:
    print('Error: invalid input')
    user = input('Enter Rock, Paper, Scissors, Lizard, or Spock:\n')

class Game():   #create parent class
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
