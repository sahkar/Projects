from random import randint

# password = "brookvale"
# while(True):
#     p2  = input("please enter password \n")
#     if( p2 == password):
#         print("Welcome")
#         break
#     else:
#         print("try again")
        
ghost_game_ask = input("Would you like to play Ghost Game \n")

if ghost_game_ask == "yes" or  ghost_game_ask == "y": 
    staying_alive = True
else:
    quit()


score = 0
while staying_alive:
    ghost_door = randint (1, 4)
    door = input('Pick a number from 1 to 4: ')
    door_num = 0
    try:
        door_num = int(door)
    except:
        print("invalid number")

    if(door_num < 1 or door_num > 4):
        continue
    if door_num == ghost_door:
        print("Died")
        staying_alive = False
        print ("game over")
        print ("score: " + str(score))
    
    else:
        print("stayed alive")
        score = score +1

    
    ask = input ("Would you like to play again \n")
    if (ask == "yes" or ask == "y"):
        staying_alive = True
    else:
        quit ()