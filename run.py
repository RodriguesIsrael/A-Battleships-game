from random import randrange


def check_ok(boat,taken):
    """ checks to see if its a valid number"""

    for i in range(len(boat)):
        num = boat[i]
        if num in taken:
            boat = [-1]
            break
        elif num < 0 or num > 99: 
            boat = [-1]
            break       
        elif num % 10 == 9 and i < len(boat) - 1 : # to avoid number out of range
            if boat[i+1] % 10 == 0:
                boat = [-1]
                break

    return boat

def check_boat(b,start,ristung,taken):
    """ checkes the boat   direction """ 

    boat = []
    if ristung  == 1:
        for i in range(b):
            boat.append(start - i*10)
            boat =check_ok(boat,taken )
    elif ristung  == 2:
        for i in range(b):
            boat.append(start + i)
            boat = check_ok(boat,taken)
    elif ristung  == 3:
        for i in range(b):
            boat .append(start + i*10)
            boat =check_ok(boat,taken)
    elif ristung == 4:
        for i in range(b):
            boat.append(start - i)
            boat = check_ok(boat,taken)
    return boat

def create_boats():
    """ added a new fuction to create boat"""

    taken = []
    ships = []
    boats = [5,4,3,3,2,2]
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1,4)
            # print(b,boat_start, boat_direction)
            boat = check_boat(b, boat_start, boat_direction,taken)
        ships.append(boat)
        taken  = taken + boat
        #print(ships)
        
    return ships,taken

def show_board_computer(taken):
    """creating a board for the batllesheep from schratch"""
    print ("            battleships  ")
    print("   0  1  2  3  4  5  6  7  8  9")
         #numbers of rows

    place = 0
    for x in range(10):
        #number of collomns 
        row = ""
        for y in range(10):
            ch = " - "
            if place in taken:
                ch = " O "
            row = row + ch
            place = place + 1
        print(x, " ", row)

def get_shot_comp(guesses,tactics):
    
    """shots from the computer"""

    ok = "n"
    while ok == "n":
        try:
            if len(tactics) > 0:
                shot = tactcs[0]
            else:
                shot = randrange(99)
            if shot not in guesses:
                ok = "y"
                guesses.append(shot)
                break
        except:
            print(" incorrect entry - please enter again")

    return shot,guesses

def show_board(hit,miss,finish):
    """creating a batllesheep from schratch"""
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
                ch = " X "
            elif place in hit:
                ch =  " o "
            elif place in finish:
                ch =  " O " 

            row = row + ch
            place = place + 1
            
        print(x," ",row)

def check_shot(shot,ships,hit,miss,finish):
    """checks the shots  that are given"""
    missed = 0
    for i in range(len(ships)):
        if shot in ships[i]:
            ships[i].remove(shot)
            if len(ships[i]) > 0:
                hit.append(shot)
                missed = 1
            else:
                finish.append(shot)
                missed = 2
    if missed == 0:
        miss.append(shot) # appends the missed shot
                

    return ships,hit, miss, finish,missed
    
def calculate_tacts(shot,tactics):

    if len(tactics) < 1:
        temp = []
hit = []
miss = []
finish = []
guesses = []
ships,taken = create_boats()
show_board_computer(taken)
tactics = []

for i in range(8): # ranges the shots
    shot, guesses = get_shot_comp(guesses,tactics)
    ships ,hit, miss,finish,missed = check_shot(shot, ships, hit, miss, finish)
    show_board(hit, miss, finish)
    if missed == 1:
        tactics.append(shot)
        tactics = calculate_tacts(shot,tactics)
    elif missed == 2:
        tactics = []
      
 
    


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