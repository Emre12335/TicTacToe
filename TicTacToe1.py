
print("welcome to tic-tac-toe".upper(),end="\n\n")
l = ["_","_","_","_","_","_","_","_","_"]
tic_tac_toe_str = f"{l[0]}|{l[1]}|{l[2]}\n{l[3]}|{l[4]}|{l[5]}\n{l[6]}|{l[7]}|{l[8]}"
tic_tac_toe_positions = f"{1}|{2}|{3}\n{4}|{5}|{6}\n{7}|{8}|{9}"
print(tic_tac_toe_str,end="\t\t\t\t")
print("This is the board nothing passed so they all  None",end="\n\n")
print(tic_tac_toe_positions,end="\t\t\t\t")
print("These are numbers of locations you should input the number you want to attempt your sign in right place",end="\n\n")


possibility_1_h = False
possibility_2_v = False
possibility_3_d = False
print(tic_tac_toe_str)
while True:
        print("Player_1 your turn")
        while True:
            try:
                player_1_ch = int(input("Please write a number:"))
                print("\n")
                if l[player_1_ch-1] == "_" and player_1_ch > 0:
                    l[player_1_ch-1] = "X"
                    tic_tac_toe_str = f"{l[0]}|{l[1]}|{l[2]}\n{l[3]}|{l[4]}|{l[5]}\n{l[6]}|{l[7]}|{l[8]}"
                    print(tic_tac_toe_str)
                    break
                elif player_1_ch <= 0:
                    print()
                    print("!!!Your number have to be between 1-9(1 and 9 included)!!!")
                    print("!!!Otherwise,We can't continue!!!")
                    print(tic_tac_toe_str)
                    print("Player_1 your turn")
                else:
                    print("Please input a position which is not attempted")
                    print(tic_tac_toe_str)
                    print("Player_1 your turn")
            except IndexError:
                print()
                print("!!!Your number have to be between 1-9(1 and 9 included)!!!")
                print("!!!Otherwise,We can't continue!!!")
                print(tic_tac_toe_str)
                print("Player_1 your turn")
            except ValueError:
                print()
                print("!!!You should input a number(decimal numbers are unacceptable)!!!")
                print("!!!Otherwise,We can't continue!!!")
                print(tic_tac_toe_str)
                print("Player_1 your turn")
        if l[0] == l[1] == l[2] == "X" or l[3] == l[4] == l[5] == "X" or l[6] == l[7] == l[8] == "X":
            possibility_1_h = True
            print("\'Horizontal\'")
        if  l[0] == l[3] == l[6] == "X" or l[1] == l[4] == l[7] == "X" or l[2] == l[5] == l[8] == "X":
            possibility_2_v = True
            print("\'Vertical\'")
        if  l[0] == l[4] == l[8] == "X" or l[2] == l[4] == l[6] == "X":
            possibility_3_d = True
            print("\'Diagonal\'")
        if possibility_1_h or possibility_2_v or possibility_3_d:
            print("Player_1 WON:GAME OVER")
            break
        if "_" not in l:
            print("Draw:No move can be made,Do you wanna get revenge")
            break
        print("Player_2 your turn")
        while True:
            try:
                player_2_ch = int(input("Please write a number:"))
                print("\n")
                if l[player_2_ch-1] == "_" and player_2_ch > 0:
                    l[player_2_ch-1] = "O"
                    tic_tac_toe_str = f"{l[0]}|{l[1]}|{l[2]}\n{l[3]}|{l[4]}|{l[5]}\n{l[6]}|{l[7]}|{l[8]}"
                    print(tic_tac_toe_str)
                    break
                elif player_2_ch <= 0:
                    print()
                    print("!!!Your number have to be between 1-9(1 and 9 included)!!!")
                    print("!!!Otherwise,We can't continue!!!")
                    print(tic_tac_toe_str)
                    print("Player_2 your turn")
                else:
                    print("Please input a position which is not attempted")
                    print(tic_tac_toe_str)
                    print("Player_2 your turn")
            except IndexError:
                print()
                print("!!!Your number have to be between 1-9(1 and 9 included)!!!")
                print("!!!Otherwise,We can't continue!!!")
                print(tic_tac_toe_str)
                print("Player_2 your turn")
            except ValueError:
                print()
                print("!!!You should input a number(decimal numbers are unacceptable)!!!")
                print("!!!Otherwise,We can't continue!!!")
                print(tic_tac_toe_str)
                print("Player_2 your turn")
        if l[0] == l[1] == l[2] == "O" or l[3] == l[4] == l[5] == "O" or l[6] == l[7] == l[8] == "O":
            possibility_1_h = True
            print("\'Horizontal\'")
        if  l[0] == l[3] == l[6] == "O" or l[1] == l[4] == l[7] == "O" or l[2] == l[5] == l[8] == "O":
            possibility_2_v = True
            print("\'Vertical\'")
        if  l[0] == l[4] == l[8] == "O" or l[2] == l[4] == l[6] == "O":
            possibility_3_d = True
            print("\'Diagonal\'")
        if possibility_1_h or possibility_2_v or possibility_3_d:
            print("Player_2 WON:GAME OVER")
            break
        if "_" not in l:
            print("Draw:No move can be made,Do you wanna get revenge")
            break