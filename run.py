from random import randrange

import random 


def check_ok(boat,taken):
    """ checks to see if its a valid number"""
    boat.sort()
    for i in range(len(boat)):
        num = boat[i]
        if num in taken:
            boat = [-1]
            break
        elif num < 0 or num > 99: 
            boat = [-1]
            break       
        elif num % 10 == 9 and i < len(boat)-1: # to avoid number out of range
            if boat[i+1] % 10 == 0:
                boat = [-1]
                break
        if i != 0:
            if boat[i] != boat[i-1]+1 and boat[i] != boat[i-1]+10:
                boat = [-1]
                break
            
    return boat

def get_ship(long,taken):
    
    ok = True
    while ok:
        ship = []
        #ask the user to enter 
        print("enter your ship of length ",long)
        for i in range(long):
            boat_num = input("please enter a number")
            ship.append(int(boat_num))
        #check that ship
        ship = check_ok(ship,taken)
        if ship[0] != -1:
            taken = taken + ship
            break
        else:
            print("error - please try again")

    return ship

def creates_ships(): #taken,boats
    taken = []
    ships = []
    boats = [5,4,3,3,2,2]

    for boat in boats:
        ship = get_ship(boat,taken)
        ships.append(ship)

    return ships #, taken

ships = creates_ships() #(taken, boats)
print(ships)

#before game
hit = []
miss = []
guesses = []
missed = 0

"""
def check_boat(b,start,ristung,taken):
    # checkes the boat   direction  

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

def create_boats(taken,boats):
    #added a new fuction to create boat

    #taken = []
    ships = []
    #boats = [5,4,3,3,2,2]
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
    #creating a board for the batllesheep from schratch
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
    
    #shots from the computer

    ok = "n"
    while ok == "n":
        try:
            if len(tactics) > 0:
                shot = tactics[0]
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
    #creating a batllesheep from schratch
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
    #checks the shots  that are given
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
    
def calculate_tacts(shot,tactics, guesses,hit):
    #creates a tactic shot 
    temp =[]
    if len(tactics) < 1:
        temp = [shot-1, shot +1, shot-10, shot+10]
    else:
        if shot -1 in hit:
            if shot-2 in hit: #condition that runs if we got more then two hits together
                temp = [shot-3,shot+1]
            else:
                temp = [shot-2,shot+1]
        elif shot+1 in hit:
            if shot-2 in hit:
                temp = [shot +3,shot-1]
            else:
                temp = [shot+2,shot-1]
        elif shot-10 in hit:
            if shot-2 in hit:
                temp = [shot-30,shot+10]
            else:
                temp = [shot-20,shot+10]
        elif shot+10 in hit:
            if shot-2 in hit:
                temp = [shot+30,shot-10]
            else:
                temp = [shot+20,shot-10]
        #tatics longer
    canditate = []

    for i in range(len(temp)):
        if temp[i] not in guesses and temp[i] < 100 and temp[i] > -1:
            canditate.append(temp[i])
    random.shuffle(canditate)

    return canditate

def checks_if_empty_2(list_of_lists):
    #ckecks if the sheep is ampty
    return all ([not elem  for elem in list_of_lists])

#ships = creates_ships()
#print(ships)

#before game
hit1 = []
miss1 = []
finish1 = []
guesses1 = []
missed1 = 0
# game amount of ships
#computer creates a board for player 1
tactics1 = []

taken1 = []
taken2 = []
hit2 = []
miss2 = []
finish2 = []
guesses2 = []
missed2 = 0
tactics2 = []
battleships = [8]
#game amount of ships
#computer creates a board for player 1
ships1,taken1 = create_boats(taken1,batlleships)
#user creates the board for player 2 - show board

#show_board_computer(taken)
ships2, taken2 = creates_ships(taken2,battleships)
show_board_computer(taken2)
#loop
for i in range(80): # ranges the shots

#player shoots 
    guesses1 = hit1 + miss1 + finish1 
    shot1 = get_shot(guesses1)
    ships1,hit1,miss1,finish1 = check_shot(shot,ships1,hit1,miss1,finish1)
    show_board(hit1,miss1,finish1)
#repeat until ships empty
    if  checks_if_empty_2(ships1):
        print("end of game - winner in " ,i,"movies")
        break

#computer shoots
# repeat until ships empty


    shot2, guesses2 = get_shot_comp(guesses2,tactics2)
    ships2 ,hit2, miss2,finish2,missed2 = check_shot(shot2, ships2, hit2, miss2, finish2)
    show_board(hit2,miss2,finish2)
    if missed2 == 1:
        tactics = calculate_tacts(shot2,tactics2,guesses2,hit2)
    elif missed2 == 2:
        tactics = []
    elif len(tactics2) > 0:
        tactics.pop(0)

    if  checks_if_empty_2(ships2):
        print("end of game -computer wins" ,i,"movies")
        break

#show_board_computer(taken)
#show_board(hit,miss,finish)
    


  
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