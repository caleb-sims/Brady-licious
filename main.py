import random

class Move:
    def __init__(self, name, display_name, wins_against):
        self.name = name  
        self.display_name = display_name  
        self.wins_against = wins_against  

class Game:
    def __init__(self):
        self.moves = {
            '1': Move('Rock', 'Rock 🪨', ['Scissors', 'Lizard']),
            '2': Move('Paper', 'Paper 📄', ['Rock', 'Spock']),
            '3': Move('Scissors', 'Scissors ✂️', ['Paper', 'Lizard']),
            '4': Move('Lizard', 'Lizard 🦎', ['Spock', 'Paper']),
            '5': Move('Spock', 'Spock 🖖', ['Scissors', 'Rock'])
        }
        self.user_wins = 0
        self.cpu_wins = 0

    def display_options(self):
        print("\nChoose your move:")
        for key, move in self.moves.items():
            print(f"{key}. {move.display_name}")
        print("6. Game key")

    def get_user_move(self):
        while True:
            self.display_options()
            choice = input("Enter the number of your move: ").strip()
            if choice in self.moves:
                return self.moves[choice]
            elif choice == '6':
                print(
                    "\nRock > Scissors: Rock crushes Scissors",
                    "\nRock > Lizard: Rock crushes Lizard",
                    "\nPaper > Rock: Paper covers Rock",
                    "\nPaper > Spock: Paper disproves Spock",
                    "\nScissors > Paper: Scissors cuts Paper",
                    "\nScissors > Lizard: Scissors decapitates Lizard",
                    "\nLizard > Spock: Lizard poisons Spock",
                    "\nLizard > Paper: Lizard eats Paper",
                    "\nSpock > Scissors: Spock smashes Scissors",
                    "\nSpock > Rock: Spock vaporizes Rock"
                )
            else:
                print("Invalid input. Please enter a number from the list.")

    def get_cpu_move(self):
        return random.choice(list(self.moves.values()))

    def decide_winner(self, user_move, cpu_move):
        print(f"\n>>> You chose: {user_move.display_name}")
        print(f">>> CPU chose: {cpu_move.display_name}\n")

        if cpu_move.name in user_move.wins_against:
            print("🎉 You win this round!")
            self.user_wins += 1
        elif user_move.name in cpu_move.wins_against:
            print("💥 You lose this round.")
            self.cpu_wins += 1
        else:
            print("🤝 It's a tie!")

    def play(self):
        while True:
            user_move = self.get_user_move()
            cpu_move = self.get_cpu_move()
            self.decide_winner(user_move, cpu_move)

            while True:
                play_again = input("\nPlay again? (Y/N): ").strip().lower()
                if play_again in ['n', 'no']:
                    print("\n--- Final Score ---")
                    print(f"Player Wins: {self.user_wins}")
                    print(f"CPU Wins: {self.cpu_wins}")
                    print("Thanks for playing!\n")
                    return
                elif play_again in ['y', 'yes']:
                    break
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.")


if __name__ == "__main__":
    game = Game()
    game.play()
