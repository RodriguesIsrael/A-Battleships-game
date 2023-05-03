def get_shot():
    """ask the user to input a radom number"""
    ok = "n"
    while ok == "n":
        shot = input("please enter yur guess")
        shot = int(shot)
        if shot < 0 or shot > 99:
            print("incorrect number, please try again")
        else:
            ok = "y"
            break    
    return shot 

     
    
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
                ch = " x "
            elif place in hit:
                ch =  " o "
            elif place in finish:
                ch =  " O " 

            row = row + ch
            place = place + 1
        print(x,row)

hit = [21,22]
miss = [20,24,12,13]
finish = [23]

get_shot()
show_board(hit, miss, finish)  
  

