# Tic-Tac-Toe
import random


def print_board(board):
   for x in range(0, 3):
       print(' | ', end="")
       for y in range(0, 3):
           print(board[x][y] + ' | ', end="")
       if x < 2:
           print('\n-+---+---+---+-')
   print()


def player_letter():
   letter = input("Would you like to be 'X' or 'O': ")
   while not (letter == "X" or letter == "O"):
       print("Invalid Symbol")
   return letter


def opponent_letter(letter):
   if letter == 'X':
       return 'O'
   else:
       return 'X'


def player_move(board, letter):
   while True:
       row = int(input("What row would you like to make your move on? "))
       col = int(input("What column would you like to make your move on? "))
       if row not in range(0, 3) or int(col) not in range(0, 3):
           print("Invalid input")
           continue
       if board[row][col] != " ":
           print("Position", (row, col), "is occupied. Try again.")
           continue
       break
   move(board, letter, row, col)


def random_position(board):
   while True:
       row = random.randint(0, 2)
       col = random.randint(0, 2)
       if board[row][col] != " ":
           continue
       else:
           return (row, col)


def free(board, row, col):
   return board[row][col] == ' '


def move(board, letter, row, col):
   board[row][col] = letter


def cancel(board, row, col):
   board[row][col] = ' '


def win_position(board, letter, block):
   for x in range(0, 3):
       for y in range(0, 3):
           if not free(board, x, y):
               continue
           move(board, letter, x, y)
           if win_check(board, letter):
               print("Computer moved to position(", x, ",", y, ")")
               if block:
                   letter_1 = opponent_letter(letter)
                   move(board, letter_1, x, y)
               return True
           cancel(board, x, y)
   return False


def computer_move(board,letter):
   if win_position(board, letter, False):
       return
   player_letter = opponent_letter(letter)
   if win_position(board, player_letter, True):
       return
   elif board[1][1]==" ":
       move(board, letter, 1, 1)
       print("Computer moved to position (1,1)")
   else:
       position = random_position(board)
       move(board, letter, position[0], position[1])
       print("Computer moved to position", position)


def board_full(board):
   for x in range(0, 3):
       for y in range(0, 3):
           if board[x][y] == " ":
               return False
   return True


def win_check(board, letter):
   for x in range(0, 3):
       won = True
       for y in range(0, 3):
           if board[x][y] != letter:
               won = False
               break
       if won:
           return True
   for y in range(0, 3):
       won = True
       for x in range(0, 3):
           if board[x][y] != letter:
               won = False
               break
       if won:
           return True
   won = True
   for x in range(0, 3):
       if board[x][x] != letter:
           won = False
           break
   if won:
       return True
   won = True
   for x in range(0, 3):
       if board[x][2 - x] != letter:
           won = False
           break
   if won:
       return True
   return False

def random_turn():
   turn_lst = ["computer", "player"]
   return random.choice(turn_lst)


def next_turn(turn):
   if turn == "player":
       return "computer"
   else:
       return "player"


def game():
   board = [[' '] * 3 for x in range(0, 3)]
   symbol = player_letter()
   turn = random_turn()
   print("The", turn, "goes first")
   while True:
       if board_full(board):
           print_board(board)
           print("The game is tied!")
           return
       if turn == "player":
           letter = symbol
           print_board(board)
           player_move(board, letter)
       else:
           letter = opponent_letter(symbol)
           computer_move(board, letter)
       if win_check(board, letter):
           print_board(board)
           print(turn, "won the game!")
           break
       turn = next_turn(turn)


def play():
   replay = "Yes"
   while replay == "Yes":
       game()
       replay = input("Would you like to play again (Yes or No): ")
   print("Thanks for Playing!")


play()
