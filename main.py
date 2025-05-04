import random
import csv
import os
from player import Player

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
        self.cpu_wins = 0
        self.round_counter = 0
        self.player = Player()
    print("\nWelcome to Rock, Paper, Scissor+",
          "\nThe game where you make a player and choose from one of five options against the CPU as you strive to dominate your opponent",
          "\nCompete with your friends for the top of are all new Leaderboard!")
    def display_options(self):
        print("\n \n")
        print("-------------------------------------")
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
            self.player.wins += 1
        elif user_move.name in cpu_move.wins_against:
            print("💥 You lose this round.")
            self.cpu_wins += 1
        else:
            print("🤝 It's a tie!")
        self.round_counter += 1

    def update_leaderboard(self, file_path="leaderboard.csv"):
        accuracy = round((self.player.wins / self.round_counter) * 100, 2) if self.round_counter > 0 else 0
        new_entry = [self.player.name, str(self.player.wins), str(accuracy)]

        leaderboard = []

        if os.path.exists(file_path):
            with open(file_path, "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                next(reader, None) 
                leaderboard = list(reader)

        leaderboard.append(new_entry)
        leaderboard.sort(key=lambda x: int(x[1]), reverse=True)

        with open(file_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Player", "Wins", "Accuracy (%)"])
            writer.writerows(leaderboard)

    def show_top_leaderboard(self, file_path="leaderboard.csv", top_n=5):
        if os.path.exists(file_path):
            with open(file_path, "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                data = list(reader)
                print("\n🏆 Top Players Leaderboard 🏆")
                for i, row in enumerate(data[1:top_n+1], start=1):  
                    print(f"{i}. {row[0]} - Wins: {row[1]}, Accuracy: {row[2]}%")
        else:
            print("\nNo leaderboard data found yet.")

    def play(self):
        while True:
            user_move = self.get_user_move()
            cpu_move = self.get_cpu_move()
            self.decide_winner(user_move, cpu_move)

            while True:
                play_again = input("\nPlay again? (Y/N): ").strip().lower()
                if play_again in ['n', 'no']:
                    print("\n--- Final Score ---")
                    print(f"{self.player.name}'s Wins: {self.player.wins}")
                    print(f"CPU Wins: {self.cpu_wins}")
                    win_percent = (self.player.wins / self.round_counter) * 100 if self.round_counter else 0
                    print(f'Win Percentage: {round(win_percent, 2)}%')
                    self.update_leaderboard()

                    while True:
                        view = input("\nView top 5 leaderboard? (Y/N): ").strip().lower()
                        if view in ['y', 'yes']:
                            self.show_top_leaderboard()
                            break
                        elif view in ['n', 'no']:
                            break
                        else:
                            print("Invalid input. Please enter Y or N.")

                    print("\nThanks for playing!\n")
                    return
                elif play_again in ['y', 'yes']:
                    break
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.")


if __name__ == "__main__":
    game = Game()
    game.play()
