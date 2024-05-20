# 1 - użytkownik
# 2 - PC
import random
def ai_move(board):
    x_pc_move = random.randint(0,5)
    y_pc_move = random.randint(0,5)

    while not board.markSpot(False, x_pc_move, y_pc_move):
        x_pc_move = random.randint(0,5)
        y_pc_move = random.randint(0,5)

    board.markSpot(False, x_pc_move, y_pc_move)
    return board

def get_user_move(board):
    print("Your turn!")
    while True:
        x_move = input("X: ")
        if(x_move >=0 and x_move <5):
            break
        else:
            print("x should be between 0 and 5")
    
    while True:
        y_move = input("Y: ")
        if(y_move >=0 and y_move <5):
            break
        else:
            print("y should be between 0 and 5")

    print("This position is not empty!")

    while board.markSpot(True, x_move, y_move) == False:
        print("Try again!")
        while True:
            x_move = input("X: ")
            if(x_move >=0 and x_move <5):
                break
            else:
                print("x should be between 0 and 5")
    
        while True:
            y_move = input("Y: ")
            if(y_move >=0 and y_move <5):
                break
            else:
                print("y should be between 0 and 5")

        print("This position is not empty!")    
    
    board.markSpot(True, x_move, y_move)
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
