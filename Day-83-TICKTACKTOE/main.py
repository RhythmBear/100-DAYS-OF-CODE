class TicTacToe:

    def __init__(self):
        self.p_1 = []
        self.p_2 = []
        self.markers = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
        self.current_player = None
        self.game_over = False
        self.score = 0

        self.welcome_rules = f"\n\nWelcome to the Tic-Tac-Toe Game. " \
                             f"\nThe Rules are simple: " \
                             f"\n-->>This is a 2 player Game. " \
                             f"\n-->>Player 1 goes first and is automatically assigned 'x' and Player 2 is assigned 'o'" \
                             f"\n-->>In order to select a box to play in, make reference to the grid below" \
                             f"\n-->> If you Ever need access to the grid, Just Type 'help' in the input session. " \
                             f"\n ENJOY!!!"

    def start_game(self):
        self.p_1 = []
        self.p_2 = []
        self.current_player = 'x'

    @staticmethod
    def print_guide():
        h_grid = "---|---|---"

        line_1 = f" 1 | 2 | 3 "
        line_2 = f" 4 | 5 | 6 "
        line_3 = f" 7 | 8 | 9 "
        guide = f"{line_1} \n{h_grid} \n{line_2} \n{h_grid} \n{line_3} \n"
        print(guide)

    def collect_input(self):
        p1input_valid = False
        p2input_valid = False
        # Collect input from user

        if self.current_player == 'x':

            # Checks to ensure that the input given is valid
            while not p1input_valid:
                p1_raw = input("It's 'X's Turn to play. Pick a spot -->> ")

                try:
                    p1_input = int(p1_raw)
                except ValueError:
                    # i.e if the input cannot be converted to an int the input becomes the raw input.
                    p1_input = p1_raw

                # Checks to see if the number given is in the required range
                if p1_raw == 'help':
                    self.print_guide()

                elif p1_input not in range(1, 10):
                    print("Oopps! Invalid Input. Please pick an empty position from 1 - 9. \n")

                # Checks to ensure the position given is empty
                elif self.markers[p1_input] != ' ':
                    print(f"Sorry, Position {p1_input} is taken. Try Again \n")

                elif p1_input in range(1, 10):
                    p1input_valid = True

                else:
                    print("Invalid Input Please Try Again")


            # Append the new value to its right position
            self.update_p1(p1_input)
            self.current_player = 'o'

        elif self.current_player == 'o':

            # Checks to ensure that the input given is valid
            while not p2input_valid:
                p2_raw = input("It's 'O's turn to play. Pick a spot -->> ")

                # Error Exception is here incase the user enters an input that cannot be converted to a integer
                # So that the input can be processed in the 3rd elif statement
                try:
                    p2_input = int(p2_raw)
                except ValueError:
                    p2_input = p2_raw


                # Check if the input is in the valid Range
                if p2_raw == 'help':
                    self.print_guide()

                elif p2_input not in range(1, 10):
                    print("Oopps! Invalid Input. Please pick an empty position from 1 - 9. \n")

                # Checks if the required position is actually empty to be filled
                elif self.markers[p2_input] != ' ':
                    print(f"Sorry, Position {p2_input} is taken. Try Again \n")

                elif p2_input in range(1, 10):
                    p2input_valid = True

                else:
                    print("Invalid Input Please Try Again")

            # self.p_2.append(p2_input)
            self.update_p2(p2_input)
            self.current_player = 'x'

    def update_markers(self):
        for i in self.p_1:
            self.markers[i] = 'x'
        for i in self.p_2:
            self.markers[i] = 'o'
        # print(self.markers)

    def update_p1(self, pos: int):
        self.p_1.append(pos)

    def update_p2(self, pos: int):
        self.p_2.append(pos)

    def print_grid(self):
        self.update_markers()
        h_grid = "---|---|---"

        line_1 = f" {self.markers[1]} | {self.markers[2]} | {self.markers[3]} "
        line_2 = f" {self.markers[4]} | {self.markers[5]} | {self.markers[6]} "
        line_3 = f" {self.markers[7]} | {self.markers[8]} | {self.markers[9]} "

        grid = f"\n{line_1} \n{h_grid} \n{line_2} \n{h_grid} \n{line_3} \n"
        print(grid)

    def check_for_winner(self):
        winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        p1_wins = False
        p2_wins = False

        for comb in winning_combinations:
            # Checks to see if one of the combinations is a subset of the players markers
            if set(comb) <= set(self.p_1):
                p1_wins = True
                self.game_over = True
                print("\nAyy!! player_1 wins \n")
            if set(comb) <= set(self.p_2):
                p2_wins = True
                self.game_over = True
                print("\nYay!! player_2 wins \n")


def run_game():
    game = TicTacToe()
    game.start_game()
    print(game.welcome_rules)
    game.print_guide()

    while not game.game_over:
        game.print_grid()
        game.check_for_winner()

        if not game.game_over:
            game.collect_input()


# Start Game
end_game = False

while not end_game:
    run_game()
    replay = input("Thanks for Playing. Type 'Y' to Play Again and 'N' to quit. -->> ").title()
    if replay == 'Y':
        end_game = False
    else:
        end_game = True


