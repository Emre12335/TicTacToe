print("\n")
print("welcome to tic-tac-toe".upper(),end="\n\n")
l = ["_","_","_","_","_","_","_","_","_"]
tic_tac_toe_str = f"{l[0]}|{l[1]}|{l[2]}\n{l[3]}|{l[4]}|{l[5]}\n{l[6]}|{l[7]}|{l[8]}"
tic_tac_toe_positions = f"{1}|{2}|{3}\n{4}|{5}|{6}\n{7}|{8}|{9}"
print(tic_tac_toe_str,end="\t\t\t\t")
print("This is the board nothing passed so they all  None",end="\n\n")
print(tic_tac_toe_positions,end="\t\t\t\t")
print("These are numbers of locations you should input the number you want to attempt your sign in right place",end="\n\n")
print()
print()
print("First we have to get your names and sides(X or O) which you would like to play with".upper())
print("""Player_1 will decide Player_2\'s side automatically and will start the gane first 
person who want to be more advantaged should get Player_1""")
print("\t")
while True:
    try:
        Player_1 = input("Player_1,please write the name you want to be called:")
        Player_2 = input("Player_2,please write the name you want to be called:")
        if len(Player_1) > 0 and len(Player_2) > 0 and Player_1.upper() != Player_2.upper():
            break
        else:
            raise ValueError
    except ValueError:
        print()
        print("Player_1\'s name and Player_2\'s name can't be same")
        print("And Neither of the players name can be blank space")
        print("Please rewrite the players names")
print()
Value_of_Player_2 = None
while True:
    try:
        Value_of_Player_1 = input(f"{Player_1},Please choice your side;you should input: X or O :").upper().strip()
        if Value_of_Player_1 == "X" or Value_of_Player_1 == "O":
            pass
        else:
            raise ValueError
    except ValueError:
        print()
        print("Please check what you have written,Value_of_Player_1 either can be X or O")
    else:
        if Value_of_Player_1 == "X":
            Value_of_Player_2 = "O"
            break
        elif Value_of_Player_1 == "O":
            Value_of_Player_2 = "X"
            break
print()
possibility_1_h = False
possibility_2_v = False
possibility_3_d = False
print(tic_tac_toe_str)
while True:
    print(f"{Player_1} your turn")
    while True:
        try:
            player_1_ch = int(input("Please write a number:"))
            print("\n")
            if l[player_1_ch-1] == "_" and player_1_ch > 0:
                l[player_1_ch-1] = Value_of_Player_1
                tic_tac_toe_str = f"{l[0]}|{l[1]}|{l[2]}\n{l[3]}|{l[4]}|{l[5]}\n{l[6]}|{l[7]}|{l[8]}"
                print(tic_tac_toe_str)
                break
            elif player_1_ch <= 0:
                print()
                print("!!!Your number have to be between 1-9(1 and 9 included)!!!")
                print("!!!Otherwise,We can't continue!!!")
                print(tic_tac_toe_str)
                print(f"{Player_1} your turn")
            else:
                print("Please input a position which is not attempted")
                print(tic_tac_toe_str)
                print(f"{Player_1} your turn")
        except IndexError:
            print()
            print("!!!Your number have to be between 1-9(1 and 9 included)!!!")
            print("!!!Otherwise,We can't continue!!!")
            print(tic_tac_toe_str)
            print(f"{Player_1} your turn")
        except ValueError:
            print()
            print("!!!You should input a number(decimal numbers are unacceptable)!!!")
            print("!!!Otherwise,We can't continue!!!")
            print(tic_tac_toe_str)
            print(f"{Player_1} your turn")
    if l[0] == l[1] == l[2] == Value_of_Player_1 or l[3] == l[4] == l[5] == Value_of_Player_1 or l[6] == l[7] == l[8] == Value_of_Player_1:
        possibility_1_h = True
        print("\'Horizontal\'")
    if  l[0] == l[3] == l[6] == Value_of_Player_1 or l[1] == l[4] == l[7] == Value_of_Player_1 or l[2] == l[5] == l[8] == Value_of_Player_1:
        possibility_2_v = True
        print("\'Vertical\'")
    if  l[0] == l[4] == l[8] == Value_of_Player_1 or l[2] == l[4] == l[6] == Value_of_Player_1:
        possibility_3_d = True
        print("\'Diagonal\'")
    if possibility_1_h or possibility_2_v or possibility_3_d:
        print(f"{Player_1} WON:GAME OVER")
        break
    if "_" not in l:
        print("Draw:No move can be made,Do you wanna get revenge")
        break
    print(f"{Player_2} your turn")
    while True:
        try:
            player_2_ch = int(input("Please write a number:"))
            print("\n")
            if l[player_2_ch-1] == "_" and player_2_ch > 0:
                l[player_2_ch-1] = Value_of_Player_2
                tic_tac_toe_str = f"{l[0]}|{l[1]}|{l[2]}\n{l[3]}|{l[4]}|{l[5]}\n{l[6]}|{l[7]}|{l[8]}"
                print(tic_tac_toe_str)
                break
            elif player_2_ch <= 0:
                print()
                print("!!!Your number have to be between 1-9(1 and 9 included)!!!")
                print("!!!Otherwise,We can't continue!!!")
                print(tic_tac_toe_str)
                print(f"{Player_2} your turn")
            else:
                print("Please input a position which is not attempted")
                print(tic_tac_toe_str)
                print(f"{Player_2} your turn")
        except IndexError:
            print()
            print("!!!Your number have to be between 1-9(1 and 9 included)!!!")
            print("!!!Otherwise,We can't continue!!!")
            print(tic_tac_toe_str)
            print(f"{Player_2} your turn")
        except ValueError:
            print()
            print("!!!You should input a number(decimal numbers are unacceptable)!!!")
            print("!!!Otherwise,We can't continue!!!")
            print(tic_tac_toe_str)
            print(f"{Player_2} your turn")
    if l[0] == l[1] == l[2] == Value_of_Player_2 or l[3] == l[4] == l[5] == Value_of_Player_2 or l[6] == l[7] == l[8] == Value_of_Player_2:
        possibility_1_h = True
        print("\'Horizontal\'")
    if  l[0] == l[3] == l[6] == Value_of_Player_2 or l[1] == l[4] == l[7] == Value_of_Player_2 or l[2] == l[5] == l[8] == Value_of_Player_2:
        possibility_2_v = True
        print("\'Vertical\'")
    if  l[0] == l[4] == l[8] == Value_of_Player_2 or l[2] == l[4] == l[6] == Value_of_Player_2:
        possibility_3_d = True
        print("\'Diagonal\'")
    if possibility_1_h or possibility_2_v or possibility_3_d:
        print(f"{Player_2} WON:GAME OVER")
        break
    if "_" not in l:
        print("Draw:No move can be made,Do you wanna get revenge")
        break