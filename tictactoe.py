# tictactoe


#sets up an empty board


from cmath import inf
import random

class Board:
    def __init__(self):
        self.current_winner = None
        self.board = [' ' for i in range(9)]
      #  self.board = ['O', 'X', 'O', ' ', 'X', ' ', ' ', ' ', ' ']
    def print_board(self):
        row1 = self.board[:3]
        row2 = self.board[3:6]
        row3 = self.board[6:]

        for row in [row1, row2, row3]:
            print('|'+'|'.join(row) + '|')
    
    def draw_move(self, position, letter):
        board_index = position
        self.board[board_index] = letter
        # [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def check_board(self, position):
        if self.board[position] != ' ':
            return False
        else:
            return True

    def check_winner(self):
        # check each row
        if self.board[:3]  == ['X']*3 or self.board[3: 6]  == ['X']*3 or self.board[6:]  == ['X']*3: 
            self.current_winner = 'X'
            return True 
        # check each column
        elif self.board[0: 9: 3]  == ['X']*3 or self.board[1: 9: 3]  == ['X']*3 or self.board[2: 9: 3]  == ['X']*3: 
            self.current_winner = 'X'
            return True 
        #check diagonals
        elif self.board[0: 9: 4] == ['X']*3 or self.board[2: 7: 2] == ['X']*3:
            self.current_winner = 'X'
            return True 
        # check each row
        elif self.board[:3]  == ['O']*3 or self.board[3: 6]  == ['O']*3 or self.board[6:]  == ['O']*3: 
            self.current_winner = 'O'
            return True 
         # check each column
        elif self.board[0: 9: 3]  == ['O']*3 or self.board[1: 9: 3]  == ['O']*3 or self.board[2: 9: 3]  == ['O']*3: 
            self.current_winner = 'O'
            return True 
            #check diagonals
        elif self.board[0: 9: 4] == ['O']*3 or self.board[2: 7: 2] == ['O']*3:
            self.current_winner = 'O'
            return True 
        else:
            return False

# sets up the players
class Player:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, board):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
            super().__init__(letter)

    def get_move(self, board):
        move = int(input(f"{self.letter}'s turn. where would you like to go? (1-9): ")) - 1

        while not board.check_board(move):
            print('that is an invalid position.')
            move = int(input(f"{self.letter}'s turn. where would you like to go? (1-9): ")) - 1

        return move

class RandomPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, board):
        print(self.letter + "'s turn.")
        move = random.randrange(0, 9)
        while not board.check_board(move):
            move = random.randrange(0, 9)

        return move
        
class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def minimax(self, board, last_move, current_player):  

        # figuring out who to maximize and who to minimize
        max_player = self.letter
        if current_player == 'X' :
            other_player = 'O'
        else:
            other_player = 'X'
        
        # checking if the state is a terminal state 
            # winning
        if board.check_winner() == True:
            if board.current_winner == max_player :
                score = 1
                conditions = {'position' : last_move, 'score' : score}
                return conditions
            else : 
                score = -1
                conditions = {'position' : last_move, 'score' : score}
                return conditions
            # return the position and the score of -1/1
            
            # tying
        elif not board.board.__contains__(' '): 
            score = 0 
            conditions = {'position' : last_move, 'score' : score}
            return conditions
            # return the position and the score of 0

        if current_player == max_player:
            best = {'position': None, 'score': -float(inf)}
        else: 
            best = {'position': None, 'score': float(inf)}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        for i in range(9):
            if board.board[i] != ' ':
                pass 
            else:
                board.board[i] = current_player
                last_move = i 

                conditions = self.minimax(board, last_move, other_player)

                if current_player == max_player :
                    if conditions['score'] > best['score']:
                        best = conditions
                        best['position'] = i

                else: 
                    if conditions['score'] < best['score']:
                        best = conditions
                        best['position'] = i

                board.board[i] = ' '
                board.current_winner = None

        return best
             
    
    def get_move(self, board):
        if board == [' ']*9:
            return 5 
        else:
            return self.minimax(board, None, self.letter)['position']

        
def play(board, player1, player2):

    player_counter = 0 

    while player_counter < 9 and board.check_winner() == False:
        
        if player_counter % 2 == 0:
            current_player = player1
        else:
            current_player = player2
    
        move_position = current_player.get_move(board)
        board.draw_move(move_position, current_player.letter)
        board.print_board()


        player_counter += 1

    print('Game over.')
    board.check_winner()
    print(board.current_winner, 'won')

# plays the game        

def play_1000_times(board, player1, player2):
    
    player_1_score = 0
    player_2_score = 0
    ties = 0
    player_counter = 0 

    for i in range(1000): 
        while player_counter < 9 and board.check_winner() == False:
            
            if player_counter % 2 == 0:
                current_player = player1
            else:
                current_player = player2

            move_position = current_player.get_move(board)
            board.draw_move(move_position, current_player.letter)
            player_counter += 1
        
        if board.current_winner == 'X': 
            player_1_score += 1

        elif board.current_winner == 'O':
            player_2_score += 1

        else: 
            ties += 1

    print('X won: ' , player_1_score)
    print('O won: ' , player_2_score)
    print('tied: ' , ties)

        






# the values to pass in the methods        
b = Board()
b.print_board()
player1 = AIPlayer("X")
player2 = AIPlayer("O")

# play the game

play_1000_times(b, player1, player2)

