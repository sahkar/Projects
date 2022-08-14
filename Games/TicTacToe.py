import random

board = [[[" "],[" "],[" "]],[[" "],[" "],[" "]],[[" "],[" "],[" "]]]
choices = []
for i in range(0,3):
    for j in range(0,3):
        choices.append((i,j))
finished = False


def pick_choice_comp(board,choices):
    for c in (choices):
        board[c[0]][c[1]] = ["X"]
        if check_winner(board,"O") == "O is the winner":
            comp_coord = c
            choices.remove(comp_coord)
            return comp_coord
        elif check_winner(board,"X") == "X is the winner":
            comp_coord = c
            choices.remove(comp_coord)
            return comp_coord
        board[c[0]][c[1]] = [" "]
        
    else:
        comp_coord = random.choice(choices)
        board[comp_coord[0]][comp_coord[1]] = ["X"]
        choices.remove(comp_coord)
        return comp_coord
        
        

def pick_choice_user(choices):
    user_coord = input("Enter an coordiante point to fill (pick between (0,0) to (2,2)): ")
    user_coord = user_coord.split(',')
    for x,y in enumerate(user_coord):
        user_coord[x] = int(y)
    user_coord = tuple(user_coord)
    if user_coord[0] <0 or user_coord[1] > 2:
        return "coordinate out of range"
    elif user_coord not in choices:
        return "please pick an empty location"
    else:
        choices.remove(user_coord)
        return user_coord
 

def check_winner(board,player):
    for r in range(len(board)):
        if board[r][0] == board[r][1] == board[r][2] == [player]:
            return player + " is the winner"
        elif board[0][r] == board[1][r] == board[r][2] == [player]:
            return player + " is the winner"
        elif board[0][0] == board[1][1] == board[2][2] == [player]:
            return player + " is the winner"
        elif board[2][0] == board[1][1] == board[0][2] == [player]:
            return player + " is the winner"
    else:
        return ""
            
def check_finished(board):
    for row in board:
        for element in row:
            if (element[0]) == " ":
                finished = False
                return finished
            else:
                finished = True
    return finished
        
while True:
    print("\nComputer's Turn:")
    cont = input("Press any key to continue:")
    comp_coord = pick_choice_comp(board,choices)
    for a in board:
        print(a)
    comp_check = (check_winner(board,"X"))
    if comp_check != "":
        print(comp_check)
        break

    get_finished = check_finished(board)
    if get_finished == True:
        print("Game Over. Tie")
        break

    print("Your turn")
    try:
        user_coord = pick_choice_user(choices)
        board[user_coord[0]][user_coord[1]] = ["O"]
        
        for b in board:
            print(b)
        
        user_check = (check_winner(board,"O"))
        if user_check != "":
            print(user_check)
            break

        get_finished = check_finished(board)
        if get_finished == True:
            print("Game Over. Tie")
            break
    except:
        print("Not a valid coordinate")
        quit()

