import random
from studentA import get_index
PLAYER_MARK = 1
AI_MARK = 2

def ai_move(board):
    #1. Check horizontal 
    for y in range(0, 5):
        for x in range(0,3):
            if board[get_index(x, y)] == PLAYER_MARK and \
            board[get_index(x+1, y)] == PLAYER_MARK and board[get_index(x+2, y)]==0:
                board[get_index(x+2, y)] = AI_MARK
                return board
            elif board[get_index(x, y)] == PLAYER_MARK and \
            board[get_index(x+2, y)] == PLAYER_MARK and board[get_index(x+1, y)]==0:
                board[get_index(x+1, y)] = AI_MARK
                return board
            elif board[get_index(x+1, y)] == PLAYER_MARK and \
            board[get_index(x+2, y)] == PLAYER_MARK and board[get_index(x, y)]==0:
                board[get_index(x, y)] = AI_MARK
                return board
    #2. Check vertical
    for x in range(0, 5):
        for y in range(0, 3):
            if board[get_index(x, y)] == PLAYER_MARK and \
            board[get_index(x, y+1)] == PLAYER_MARK and board[get_index(x, y+2)]==0:
                board[get_index(x, y+2)] = AI_MARK
                return board
            elif board[get_index(x, y)] == PLAYER_MARK and \
            board[get_index(x, y+2)] == PLAYER_MARK and board[get_index(x, y+1)]==0:
                board[get_index(x, y+1)] = AI_MARK
                return board
            elif board[get_index(x, y+1)] == PLAYER_MARK and \
            board[get_index(x, y+2)] == PLAYER_MARK and board[get_index(x, y)]==0:
                board[get_index(x, y)] = AI_MARK
                return board

    #3. Check \ axis
    for y in range(0, 3):
        for x in range(0,3):
            if board[get_index(x, y)] == PLAYER_MARK and \
            board[get_index(x+1, y+1)] == PLAYER_MARK and board[get_index(x+2, y+2)]==0:
                board[get_index(x+2, y+2)] = AI_MARK
                return board
            elif board[get_index(x, y)] == PLAYER_MARK and \
            board[get_index(x+2, y+2)] == PLAYER_MARK and board[get_index(x+1, y+1)]==0:
                board[get_index(x+1, y+1)] = AI_MARK
                return board
            elif board[get_index(x+1, y+1)] == PLAYER_MARK and \
            board[get_index(x+2, y+2)] == PLAYER_MARK and board[get_index(x+2, y+2)]==0:
                board[get_index(x, y)] = AI_MARK
                return board

    #4. Check / axis
    for y in range(3, 5):
        for x in range(3,5):
            if board[get_index(x, y)] == PLAYER_MARK and \
            board[get_index(x-1, y-1)] == PLAYER_MARK and board[get_index(x-2, y-2)]==0:
                board[get_index(x-2, y-2)] = AI_MARK
                return board
            elif board[get_index(x, y)] == PLAYER_MARK and \
            board[get_index(x-2, y-2)] == PLAYER_MARK and board[get_index(x-1, y-1)]==0:
                board[get_index(x-1, y-1)] = AI_MARK
                return board
            elif board[get_index(x-1, y-1)] == PLAYER_MARK and \
            board[get_index(x-2, y-2)] == PLAYER_MARK and board[get_index(x, y)]==0:
                board[get_index(x, y)] = AI_MARK
                return board
    
    x_pc_move = random.randint(0,4)
    y_pc_move = random.randint(0,4)

    while board[5 * y_pc_move + x_pc_move] != 0:
        x_pc_move = random.randint(0,4)
        y_pc_move = random.randint(0,4)

    board[5 * y_pc_move + x_pc_move] = AI_MARK
    return board


def get_user_move(board):
    print("Your turn!")
    while True:
        x_move = input("X: ")
        if(int(x_move) >=0 and int(x_move) <5):
            break
        else:
            print("x should be between 0 and 5")
    
    while True:
        y_move = input("Y: ")
        if(int(y_move) >=0 and int(y_move) <5):
            break
        else:
            print("y should be between 0 and 5")

    while board[int(y_move)*5+int(x_move)] != 0:
        print("Try again!")
        while True:
            x_move = input("X: ")
            if(int(x_move) >=0 and int(x_move) <5):
                break
            else:
                print("x should be between 0 and 5")
    
        while True:
            y_move = input("Y: ")
            if(int(y_move) >=0 and int(y_move) <5):
                break
            else:
                print("y should be between 0 and 5")

        print("This position is not empty!")    
    
    board[int(y_move)*5+int(x_move)] = PLAYER_MARK
    return board

def is_player_starting():
    print("Do you want to start? T/F")
    while(True):
        choice = input("Your choice: ")
        if(choice == 'T'):
            return True
        elif (choice == 'F'):
            return False
        else:
            print('Try again!')
