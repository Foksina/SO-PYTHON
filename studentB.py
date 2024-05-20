def ai_move(board):
    pass

def get_user_move(board):
    pass

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
