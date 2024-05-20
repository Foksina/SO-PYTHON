import random
PLAYER_MARK = 1
AI_MARK = 2

def ai_move(board):
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

    print("This position is not empty!")

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
