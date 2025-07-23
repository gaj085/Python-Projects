# WAP TO PLAY TIC-TAC TOE WITH COMPUTER
import random
Val = []
def General():
    global Val
    Val = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("+---+---+---+")
    print("|", Val[0], "|", Val[1], "|", Val[2], "|")
    print("+---+---+---+")
    print("|", Val[3], "|", Val[4], "|", Val[5], "|")
    print("+---+---+---+")
    print("|", Val[6], "|", Val[7], "|", Val[8], "|")
    print("+---+---+---+")
    
print("General Layout is:")
General()


Choice_P = input("\nEnter your choice[X or O]: ")
while True:
    if Choice_P.upper() in ['O', 'X']:
        break
    else:
        print("Invalid response...")
        Choice_P = input("Please try again...\nEnter your choice[X or O]: ")
        print()
        
if Choice_P.lower() == 'x':
    Choice_C = 'O'
else:
    Choice_C = 'X'


def Game():
    print()
    print("+---+---+---+")
    print("|", Val[0], "|", Val[1], "|", Val[2], "|")
    print("+---+---+---+")
    print("|", Val[3], "|", Val[4], "|", Val[5], "|")
    print("+---+---+---+")
    print("|", Val[6], "|", Val[7], "|", Val[8], "|")
    print("+---+---+---+")
    print()


toss = random.randint(1, 2)
choice = input("\nToss Begins...\nEnter your choice\nHeads(H) or Tails(T): ")
while True:
    if choice.upper() in ['H', 'T']:
        break
    else:
        print("Invalid response...")
        choice = input("Please try again...\nEnter your choice\nHeads(H) or Tails(T)")
        print()
     
        
T = []
def turn_comp():
    global comp
    global T
    
    comp = random.randint(1, 9)
    
    if Val[0] == Choice_P.upper() and Val[1] == Choice_P.upper():
        if 3 not in T:
            comp = 3
    elif Val[0] == Choice_P.upper() and Val[2] == Choice_P.upper():
        if 2 not in T:
            comp = 2
    elif Val[0] == Choice_P.upper() and Val[3] == Choice_P.upper():
        if 7 not in T:
            comp = 7
    elif Val[0] == Choice_P.upper() and Val[4] == Choice_P.upper():
        if 9 not in T:
            comp = 9
    elif Val[0] == Choice_P.upper() and Val[6] == Choice_P.upper():
        if 4 not in T:
            comp = 4
    elif Val[0] == Choice_P.upper() and Val[8] == Choice_P.upper():
        if 5 not in T:
            comp = 5
    elif Val[1] == Choice_P.upper() and Val[2] == Choice_P.upper():
        if 1 not in T:
            comp = 1
    elif Val[1] == Choice_P.upper() and Val[4] == Choice_P.upper():
        if 8 not in T:
            comp = 8
    elif Val[1] == Choice_P.upper() and Val[7] == Choice_P.upper():
        if 5 not in T:
            comp = 5
    elif Val[2] == Choice_P.upper() and Val[5] == Choice_P.upper():
        if 9 not in T:
            comp = 9
    elif Val[2] == Choice_P.upper() and Val[4] == Choice_P.upper():
        if 7 not in T:
            comp = 7
    elif Val[2] == Choice_P.upper() and Val[6] == Choice_P.upper():
        if 5 not in T:
            comp = 5
    elif Val[2] == Choice_P.upper() and Val[8] == Choice_P.upper():
        if 6 not in T:
            comp = 6
    elif Val[3] == Choice_P.upper() and Val[0] == Choice_P.upper():
        if 7 not in T:
            comp = 7
    elif Val[3] == Choice_P.upper() and Val[4] == Choice_P.upper():
        if 6 not in T:
            comp = 6
    elif Val[3] == Choice_P.upper() and Val[5] == Choice_P.upper():
        if 5 not in T:
            comp = 5
    elif Val[3] == Choice_P.upper() and Val[6] == Choice_P.upper():
        if 1 not in T:
            comp = 1
    elif Val[4] == Choice_P.upper() and Val[5] == Choice_P.upper():
        if 4 not in T:
            comp = 4
    elif Val[4] == Choice_P.upper() and Val[6] == Choice_P.upper():
        if 3 not in T:
            comp = 3
    elif Val[4] == Choice_P.upper() and Val[7] == Choice_P.upper():
        if 2 not in T:
            comp = 2
    elif Val[4] == Choice_P.upper() and Val[8] == Choice_P.upper():
        if 1 not in T:
            comp = 1
    elif Val[5] == Choice_P.upper() and Val[8] == Choice_P.upper():
        if 3 not in T:
            comp = 3
    elif Val[6] == Choice_P.upper() and Val[7] == Choice_P.upper():
        if 9 not in T:
            comp = 9
    elif Val[6] == Choice_P.upper() and Val[8] == Choice_P.upper():
        if 8 not in T:
            comp = 8
    elif Val[7] == Choice_P.upper() and Val[8] == Choice_P.upper():
        if 7 not in T:
            comp = 7
    
    
    elif Val[0] == Choice_C and Val[1] == Choice_C:
        if 3 not in T:
            comp = 3
    elif Val[0] == Choice_C and Val[2] == Choice_C:
        if 2 not in T:
            comp = 2
    elif Val[0] == Choice_C and Val[3] == Choice_C:
        if 7 not in T:
            comp = 7
    elif Val[0] == Choice_C and Val[4] == Choice_C:
        if 9 not in T:
            comp = 9
    elif Val[0] == Choice_C and Val[6] == Choice_C:
        if 4 not in T:
            comp = 4
    elif Val[0] == Choice_C and Val[8] == Choice_C:
        if 5 not in T:
            comp = 5
    elif Val[1] == Choice_C and Val[2] == Choice_C:
        if 1 not in T:
            comp = 1
    elif Val[1] == Choice_C and Val[4] == Choice_C:
        if 8 not in T:
            comp = 8
    elif Val[1] == Choice_C and Val[7] == Choice_C:
        if 5 not in T:
            comp = 5
    elif Val[2] == Choice_C and Val[5] == Choice_C:
        if 9 not in T:
            comp = 9
    elif Val[2] == Choice_C and Val[4] == Choice_C:
        if 7 not in T:
            comp = 7
    elif Val[2] == Choice_C and Val[6] == Choice_C:
        if 5 not in T:
            comp = 5
    elif Val[2] == Choice_C and Val[8] == Choice_C:
        if 6 not in T:
            comp = 6
    elif Val[3] == Choice_C and Val[0] == Choice_C:
        if 7 not in T:
            comp = 7
    elif Val[3] == Choice_C and Val[4] == Choice_C:
        if 6 not in T:
            comp = 6
    elif Val[3] == Choice_C and Val[5] == Choice_C:
        if 5 not in T:
            comp = 5
    elif Val[3] == Choice_C and Val[6] == Choice_C:
        if 1 not in T:
            comp = 1
    elif Val[4] == Choice_C and Val[5] == Choice_C:
        if 4 not in T:
            comp = 4
    elif Val[4] == Choice_C and Val[6] == Choice_C:
        if 3 not in T:
            comp = 3
    elif Val[4] == Choice_C and Val[7] == Choice_C:
        if 2 not in T:
            comp = 2
    elif Val[4] == Choice_C and Val[8] == Choice_C:
        if 1 not in T:
            comp = 1
    elif Val[5] == Choice_C and Val[8] == Choice_C:
        if 3 not in T:
            comp = 3
    elif Val[6] == Choice_C and Val[7] == Choice_C:
        if 9 not in T:
            comp = 9
    elif Val[6] == Choice_C and Val[8] == Choice_C:
        if 8 not in T:
            comp = 8
    elif Val[7] == Choice_C and Val[8] == Choice_C:
        if 7 not in T:
            comp = 7
        

    while True:
        if comp not in T:
            break
        else:
            comp = random.randint(1, 9)
            
    T += [comp]


def turn_player():
    global player
    global T
    
    player = int(input("Enter position you want to fill: "))
    while True:
        if player in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            break
        else:
            print("\nThe number has be between 1-9\nTry again...")
            player = int(input("Enter position you want to fill: "))
    while True:
        if player not in T:
            break
        else:
            print("Position already filled...")
            player = int(input("\nEnter new position: "))
    T += [player]


kill = False
W = None
Tie = None
def Check():
    global kill
    global W
    global Tie
    if [Val[0], Val[1], Val[2]] == ['X', 'X', 'X']:
        if Choice_C == 'X':
            W = False
        else:
            W = True
        kill = True
    elif [Val[3], Val[4], Val[5]] == ['X', 'X', 'X']:
        if Choice_C == 'X':
            W = False
        else:
            W = True
        kill = True
    elif [Val[6], Val[7], Val[8]] == ['X', 'X', 'X']:
        if Choice_C == 'X':
            W = False
        else:
            W = True
        kill = True
    elif [Val[0], Val[3], Val[6]] == ['X', 'X', 'X']:
        if Choice_C == 'X':
            W = False
        else:
            W = True
        kill = True
    elif [Val[1], Val[4], Val[7]] == ['X', 'X', 'X']:
        if Choice_C == 'X':
            W = False
        else:
            W = True
        kill = True
    elif [Val[2], Val[5], Val[8]] == ['X', 'X', 'X']:
        if Choice_C == 'X':
            W = False
        else:
            W = True
        kill = True
    elif [Val[0], Val[4], Val[8]] == ['X', 'X', 'X']:
        if Choice_C == 'X':
            W = False
        else:
            W = True
        kill = True
    elif [Val[2], Val[4], Val[6]] == ['X', 'X', 'X']:
        if Choice_C == 'X':
            W = False
        else:
            W = True
        kill = True
    elif [Val[0], Val[1], Val[2]] == ['O', 'O', 'O']:
        if Choice_C == 'O':
            W = False
        else:
            W = True
        kill = True
    elif [Val[3], Val[4], Val[5]] == ['O', 'O', 'O']:
        if Choice_C == 'O':
            W = False
        else:
            W = True
        kill = True
    elif [Val[6], Val[7], Val[8]] == ['O', 'O', 'O']:
        if Choice_C == 'O':
            W = False
        else:
            W = True
        kill = True
    elif [Val[0], Val[4], Val[8]] == ['O', 'O', 'O']:
        if Choice_C == 'O':
            W = False
        else:
            W = True
        kill = True
    elif [Val[2], Val[4], Val[6]] == ['O', 'O', 'O']:
        if Choice_C == 'O':
            W = False
        else:
            W = True
        kill = True
    elif [Val[0], Val[3], Val[6]] == ['O', 'O', 'O']:
        if Choice_C == 'O':
            W = False
        else:
            W = True
        kill = True
    elif [Val[1], Val[4], Val[7]] == ['O', 'O', 'O']:
        if Choice_C == 'O':
            W = False
        else:
            W = True
        kill = True
    elif [Val[2], Val[5], Val[8]] == ['O', 'O', 'O']:
        if Choice_C == 'O':
            W = False
        else:
            W = True
        kill = True
    else:
        counter = 0
        for i in range(1, 10):
            if i in Val:
                counter += 1
                break
        if counter == 0:
            Tie = True
            kill = True


if toss == 1:
    if choice.upper() == 'H':
        print("\nIt's Tails")
    elif choice.upper() == 'T':
        print("\nIt's Heads")
    print("Computer wins the toss...\nIt will start the game...")
    turn_comp()
    Val[comp - 1] = Choice_C
    Game()
    while True:
        print("Your turn...\n")
        turn_player()
        Val[player - 1] = Choice_P.upper()
        Check()
        if kill == True:
            break
        Game()
        print("Computer's turn...\n")
        turn_comp()
        Val[comp-1] = Choice_C
        Check()
        if kill == True:
            break
        Game()
else:
    if choice.upper() == 'T':
        print("\nIt's Tails")
    elif choice.upper() == 'H':
        print("\nIt's Heads")
    print("You won the toss...\nYou start...")
    turn_player()
    Val[player - 1] = Choice_P.upper()
    Game()
    while kill == False:
        print("Computer's turn...\n")
        turn_comp()
        Val[comp - 1] = Choice_C
        Check()
        if kill == True:
            break
        Game()
        print("Your turn...\n")
        turn_player()
        Val[player - 1] = Choice_P.upper()
        Check()
        if kill == True:
            break
        Game()
Game()
if W == True:
    print("\nCongratulations!!\nYou Win...")
elif W == False:
    print("\nYou Lose!!\nComputer Wins...")
elif Tie == True:
    print("It's a Tie...")
