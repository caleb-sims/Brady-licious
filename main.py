import random

class Move:
    def __init__(self, name, wins_against):
        self.name = name
        self.wins_against = wins_against

class Game:
    def __init__(self):
        self.moves = {
            '1': Move('Rock 🪨', ['Scissors', 'Lizard']),
            '2': Move('Paper 📄', ['Rock', 'Spock']),
            '3': Move('Scissors ✂️', ['Paper', 'Lizard']),
            '4': Move('Lizard 🦎', ['Spock', 'Paper']),
            '5': Move('Spock 🖖', ['Scissors', 'Rock'])
        }
        self.user_wins = 0
        self.cpu_wins = 0
    
    print()
    print("Welcome to Rock, Paper, Scissors the extended version!")
    def display_options(self):
        print("\nChoose your move:")
        for key, move in self.moves.items():
            print(f"{key}. {move.name}")
        print('6. Game key')

    def get_user_move(self):
        while True:
            self.display_options()
            choice = input("Enter the number of your move: ").strip()
            if choice in self.moves:
                return self.moves[choice]
            elif choice == '6':
                print("\nRock > Scissors: Rock crushes Scissors",
                "\nRock > Lizard: Rock crushes Lizard",
                "\nPaper > Rock: Paper covers Rock",
                "\nPaper > Spock'): Paper disproves Spock",
                "\nScissors > Paper: Scissors cuts Paper",
                "\nScissors > Lizard: Scissors decapitates Lizard",
                "\nLizard > Spock: Lizard poisons Spock",
                "\nLizard > Paper: Lizard eats Paper",
                "\nSpock > Scissors: Spock smashes Scissors",
                "\nSpock > Rock: Spock vaporizes Rock")
            else:
                print("Invalid input. Please enter a number from the list.")

    def get_cpu_move(self):
        return random.choice(list(self.moves.values()))

    def decide_winner(self, user_move, cpu_move):
        print(f"\n>>> You chose: {user_move.name}")
        print(f">>> CPU chose: {cpu_move.name}\n")

        if cpu_move.name in user_move.wins_against:
            print("🎉 You win this round!")
            self.user_wins += 1
        elif user_move.name in cpu_move.wins_against:
            print("💥 You lose this round.")
            self.cpu_wins += 1
        else:
            print("🤝 It's a tie!")

    def play(self):
        play_again = 'Y'
        while play_again.lower() in ['y', 'yes']:
            user_move = self.get_user_move()
            cpu_move = self.get_cpu_move()
            self.decide_winner(user_move, cpu_move)

            play_again = input("\nPlay again? (Y/N): ")
           
        print("\n--- Final Score ---")
        print(f"Player Wins: {self.user_wins}")
        print(f"CPU Wins: {self.cpu_wins}")
        print("Thanks for playing!")
        print()
            

if __name__ == "__main__":
    game = Game()
    game.play()
