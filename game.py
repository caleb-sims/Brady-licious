import random

options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
win_conditions = {
    'Rock': ['Scissors', 'Lizard'],
    'Paper': ['Rock', 'Spock'],
    'Scissors': ['Paper', 'Lizard'],
    'Lizard': ['Paper', 'Spock'],
    'Spock': ['Scissors', 'Rock']
}

cpu_wins = 0
user_wins = 0
play_again = 'y'

while play_again == 'y':
    user = input('Enter Rock, Paper, Scissors, Lizard, or Spock:\n').capitalize()
    cpu = random.choice(options)

    # Validate input
    while user not in options:
        print('Error: invalid input.')
        user = input('Enter Rock, Paper, Scissors, Lizard, or Spock:\n').capitalize()

    # Handle draw
    while cpu == user:
        print(f'Player 2 chose {cpu}.')
        print('You drew.')
        cpu = random.choice(options)
        user = input('Enter Rock, Paper, Scissors, Lizard, or Spock:\n').capitalize()
        while user not in options:
            print('Error: invalid input.')
            user = input('Enter Rock, Paper, Scissors, Lizard, or Spock:\n').capitalize()

    # Determine winner
    print(f'Player 2 chose {cpu}.')
    if cpu in win_conditions[user]:
        print('You win!')
        user_wins += 1
    else:
        print('You lose.')
        cpu_wins += 1

    play_again = input('Press "Y" to play again or "N" to end the game:\n').lower()

print(f'Player wins: {user_wins}')
print(f'CPU wins: {cpu_wins}')

        