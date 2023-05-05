from random import randrange

boat_start = randrange(99)
print(boat_start)

"""   
def get_shot(guesses):
    
    ask the user to input a radom number
    ok = "n"
    while ok == "n":
        try:
            shot = input("please enter your guess ")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print(" incorrect number, please try again")
            elif shot in guesses:
                print("incorrect number, please try again")
            else:
                ok = "y"
                break
        except:
            print(" incorrect entry - please enter again")

    return shot 
    
def show_boat(hit,miss,finish):
    creating a batllesheep from schratch
    print ("            battleships  ")
    print("   0  1  2  3  4  5  6  7  8  9")
         #numbers of rows

    place = 0
    for x in range(10):
        #number of collomns 
        row = ""
        for y in range(10):
            ch = " - "
            if place in miss:
                ch = " x "
            elif place in hit:
                ch =  " o "
            elif place in finish:
                ch =  " O " 

            row = row + ch
            place = place + 1
        print(x,row)

def check_shot(shot,boat1,boat2,hit,miss,finish):
    checks the shots  that are given 

    if shot in boat1:
        boat1.remove(shot)
        if len(boat1) > 0:
            hit.append(shot)
        else:
            finish.append(shot)
    elif shot in boat2:
        boat2.remove(shot)
        if len(boat2) > 0:
            hit.append(shot)
        else:
            finish.append(shot)
    else:
         miss.append(shot)

    return boat1,boat2,hit, miss, finish     

boat1 = [6,16,26]
boat2 = [45,46,47]

hit = []
miss = []
finish = []

for i in range(10):
    guesses = hit + miss + finish
    shot = get_shot(guesses)
    boat1,boat2,hit,miss,comp = check_shot(shot,boat1, boat2,hit,miss,finish)
    show_board(hit, miss, finish)

    if len(boat1) < 1 and len(boat2) < 1: # Called when the game is won
        print("you've  won")
print("finished")  """