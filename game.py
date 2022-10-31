import math
import time
from players import HumanPlayer, ComputerPlayerSmart, ComputerPlayerRandom

gameCount = 0
xWins = 0
oWins = 0
ties = 0

class TTT():

    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' | ')

    @staticmethod
    def print_board_numbers():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' | ')

    def move(self, square, letter):

        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter

            return True
        return False

    def winner(self, square, letter):
        global gameCount
        global xWins
        global oWins
        global ties

        row_ind = math.floor(square / 3)
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([s == letter for s in row]):
            return True

        col_ind = square % 3
        column =  [self.board[col_ind + i * 3] for i in range(3)]
        if all([s == letter for s in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def squares_empty(self):
        return ' ' in self.board

    def number_of_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']


def play(game, x_player, o_player, print_game = True):
    global gameCount
    global xWins
    global oWins
    global ties


    if print_game:
        game.print_board_numbers()

    letter = 'X'

    while game.squares_empty():
        if letter == 'O':
            square = o_player.get_move(game)

        else:
            square = x_player.get_move(game)

        if game.move(square, letter):
            if print_game:
                print(letter + ' makes a move to {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + " wins the game!")
                    if letter == 'X':
                        xWins = xWins + 1
                        gameCount = gameCount + 1
                    if letter == 'O':
                        oWins = oWins + 1
                        gameCount = gameCount + 1
                    print(f"X has won {xWins} game(s), O has won {oWins} game(s), with {ties} ties.")

                return letter
            letter = 'O' if letter == 'X' else "X"

        time.sleep(.8)

    if print_game:
        print('Players have tied!')
        ties = ties + 1
        print(f"X has won {xWins} game(s), O has won {oWins} game(s), with {ties} ties.")

if __name__  == '__main__':
    player1 = int(input("Please decide if X's player should be Human (1), a silly computer (2), or a smart computer (3: >>)"))
    if player1 == 1:
        x_player = HumanPlayer('X')
    elif player1 == 2:
        x_player = ComputerPlayerRandom('X')
    else:
        x_player = ComputerPlayerSmart('X')

    player2 = int(input("Now decide if O's player should be Human (1), a silly computer (2) or a smart computer (3): >>"))
    if player2 == 1:
        o_player = HumanPlayer('O')
    elif player2 == 2:
        o_player = ComputerPlayerRandom('O')
    else:
        o_player = ComputerPlayerSmart('O')

    t = TTT()


    if player1 == 3 or player1 == 2:
        if player2 == 3 or player1 == 2:
                while True:
                    time.sleep(2.5)
                    t = TTT()
                    play(t, x_player, o_player, print_game = True)
    else:
        play(t, x_player, o_player, print_game = True)
