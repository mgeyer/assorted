import random
from copy import deepcopy

class TicTacToe:
    board = None
    number_of_players = None
    currentPlayer = 'O'
    nextPlayer = 'X'
    player_symbol = None
    AI = None

    def __init__(self):
        self.board = TicTacToeBoard()
        self.AI = TicTacToeAI()
        self.number_of_players = int(raw_input('Number of Players: '))
        while self.number_of_players not in (0, 1, 2):
            self.number_of_players = int(raw_input('Please Pick a Number between 0 and 2: '))
        if self.number_of_players == 1:
            self.player_symbol = raw_input('Please Pick O or X (O starts): ').upper()
            while self.player_symbol not in ('X', 'O'):
                self.player_symbol = raw_input('Choose either O or X: ').upper()
        self.board.printBoard()
        self.run()

    def run(self):
        board_status = 0
        while board_status == 0:
            is_computer = False
            if self.number_of_players == 0 or (self.number_of_players == 1 and self.currentPlayer != self.player_symbol):
                is_computer = True
            print "It is player %s's turn!" % self.currentPlayer
            succesful_move = False
            while not succesful_move:
                if is_computer:
                    move = self.AI.makeMove(self.board, self.currentPlayer, self.nextPlayer)
                    row = move[0]
                    col = move[1]
                else:
                    row = int(raw_input('Row:'))
                    col = int(raw_input('Column:'))
                succesful_move = self.board.place(row, col, self.currentPlayer)
            board_status = self.board.isSolved()
            self.board.printBoard()
            if board_status == 0:
                currentPlayer = 'X' if self.currentPlayer is 'O' else 'O' 
                self.nextPlayer = self.currentPlayer
                self.currentPlayer = currentPlayer
        if board_status == 2:
            print "The Game is Done Player %s has Won!" % self.currentPlayer
        else:
            print "The Game is a Draw!"


class TicTacToeBoard:
    arrayBoard = None
    tilesPlaced = 0

    def __init__(self, board=None):
        if board:
            self.arrayBoard = board
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] != ' ':
                        self.tilesPlaced += 1
        else:
            self.arrayBoard = [[' ' for i in range(3)] for j in range(3)]

    def printBoard(self):
        for i in range(len(self.arrayBoard)):
            row = self.arrayBoard[i]
            print " %s | %s | %s " % (row[0], row[1], row[2])
            if i < 2:
                print "-----------"

    '''
        Returns 0 if not solved
        Returns 1 if full
        Returns 2 if completed
    '''
    def isSolved(self):
        #Check each row and column to see if all 3 are the same
        for i in range(3):
            if self.arrayBoard[i][0] == self.arrayBoard[i][1] == self.arrayBoard[i][2] != ' ':
                return 2
            if self.arrayBoard[0][i] == self.arrayBoard[1][i] == self.arrayBoard[2][i] != ' ':
                return 2

        #Check both Diagonals
        if self.arrayBoard[0][0] == self.arrayBoard[1][1] == self.arrayBoard[2][2] != ' ':
            return 2
        if self.arrayBoard[0][2] == self.arrayBoard[1][1] == self.arrayBoard[2][0] != ' ':
            return 2

        # Check if all tiles are filled
        if self.tilesPlaced == 9:
            return 1

        return 0

    def place(self, row, col, val):
        #Check if the array bounds are fine
        if row > 2 or col > 2:
            print "Values are out of bounds, row and column must be less than 3!"
            return False

        # Make sure that the field isn't already filled
        elif self.arrayBoard[row][col] is not ' ':
            print "This field has already been filled in, please pick another!"
            return False

        # Else fill in value and return True
        else:
            self.arrayBoard[row][col] = val
            self.tilesPlaced += 1
            return True

    def getAvailableTiles(self):
        available = []
        for i in range(3):
            for j in range(3):
                if self.arrayBoard[i][j] == ' ':
                    available.append([i, j])
        return available

class TicTacToeAI:
    random = False

    def makeMove(self, board, player_symbol, opponent_symbol):
        bestMove = None
        if self.random:
            possible_moves = board.getAvailableTiles()
            bestMove = possible_moves[random.randint(0, len(possible_moves) - 1)]
        else:
            possible_moves = board.getAvailableTiles()
            bestScore = -2
            bestMove = None
            for move in possible_moves:
                score = self.miniMax(player_symbol, opponent_symbol, False, board)
                if score > bestScore:
                    bestScore = score
                    bestMove = move
        return bestMove

    def miniMax(self, player_symbol, opponent_symbol, opponent, board):
        if board.isSolved() == 2:
            if opponent:
                return 1
            else:
                return -1
        if board.isSolved() == 1:
            return 0
        if not opponent:
            bestScore = -2
            for move in board.getAvailableTiles():
                temp_board = TicTacToeBoard(deepcopy(board.arrayBoard))
                temp_board.place(move[0], move[1], player_symbol)
                score = self.miniMax(player_symbol, opponent_symbol, True, temp_board)
                if score > bestScore:
                    bestScore = score
            return bestScore
        else:
            worstScore = 2
            for move in board.getAvailableTiles():
                temp_board = TicTacToeBoard(deepcopy(board.arrayBoard))
                temp_board.place(move[0], move[1], opponent_symbol)
                score = self.miniMax(player_symbol, opponent_symbol, False, temp_board)
                if score < worstScore:
                    worstScore = score
            return worstScore
'''
x = TicTacToeBoard()

y = TicTacToeBoard(deepcopy(x.arrayBoard))

y.place(0, 1, 'Y')

x.printBoard()

y.printBoard()
'''
TicTacToe()
