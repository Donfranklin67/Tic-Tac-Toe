import time

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1
name1 = input("Input first player's name: ")
name2 = input("Input second player's name: ")

########win Flags##########
Win = 1
Draw = -1
Running = 0
Stop = 1
###########################
Game = Running
Mark = 'X'


# This Function Draws Game Board
def play_board():
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("___|___|___")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("___|___|___")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")


# This Function Checks position is empty or not
def check_placement(x):
    if board[x] == ' ':
        return True
    else:
        return False


# This Function Checks player has won or not
def CheckWin():
    global Game
    # Horizontal winning condition
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        Game = Win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        Game = Win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        Game = Win
        # Vertical Winning Condition
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        Game = Win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        Game = Win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        Game = Win
        # Diagonal Winning Condition
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        Game = Win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        Game = Win
        # Match Tie or Draw Condition
    elif \
            board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[
                6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        Game = Draw
    else:
        Game = Running


print("""
  _______         ______              ______         
 /_  __(_)____   /_  __/___ ______   /_  __/___  ___ 
  / / / / ___/    / / / __ `/ ___/    / / / __ \/ _ /
 / / / / /__     / / / /_/ / /__     / / / /_/ /  __/
/_/ /_/\___/    /_/  \__,_/\___/    /_/  \____/\___/   \n\n""")

print(f"{name1} [X] --- {name2} [O]\n")
print()
print("Loading...")
time.sleep(3)
while Game == Running:
    play_board()
    if player % 2 != 0:
        print(f"{name1}'s chance")
        Mark = 'X'
    else:
        print(f"{name2}'s chance")
        Mark = 'O'
    choice = int(input("Enter the position between [1-9] where you want to mark : "))
    if check_placement(choice):
        board[choice] = Mark
        player += 1
        CheckWin()

play_board()
if Game == Draw:
    print("Game Draw")
elif Game == Win:
    player -= 1
    if player % 2 != 0:
        print(f"{name1} Won!!!")
    else:
        print(f"{name2} Won!!!")
