import random
import sys
import logo as l
import os

def clear_console():        # For clear the consol
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix-like systems (Linux, macOS)
    else:
        _ = os.system('clear')

def start():            #  To start the program
    clear_console()
    # print("Welcome to the unbeatable Tic Tac Toe")
    # print("The board's index values are: ")
    print(l.logo)
    print(l.instruction)
    # print("0|1|2")                # These lines now moved in the logo.py file
    # print("3|4|5")
    # print("6|7|8")
    # print("You are X's and AI is O's ")
    want = input("Do you want to start? Type 'Y' for yes and 'E' for exit : ").lower()
    if want == "y":
        print_board(turn, board, aiturn)
    elif want == "e":
        end()
    else:
        print("Invalid input")
        start()

board = ["_","_","_","_","_","_"," "," "," "] #Board horizontal and vertical lines
pairs = ([0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]) #Win Pairs
corner = [0,2,6,8] #corner is used for the AI to let it pick random corner.
sides = [1,3,5,7] # sides of the board

turn = "PLAYER"

aiturn = 0 #number of turn of ai

def print_board(turn, board, aiturn): #to print the board and start the next turn
    clear_console()
    print(l.logo)
    print(l.instruction)
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("Turn :" + str(turn))
    if turn == 0: #For first move
        player_move(turn, board, aiturn)
    if turn == "AI": #if ai_move
        aiturn += 1
        ai_move(turn, board, aiturn, corner)
    if turn == "PLAYER": #if player_move
        player_move(turn, board, aiturn)

def player_move(turn, board, aiturn):
    choice = input("Enter your move (1-9): ")
    if choice.isdigit() == False:
        print("Input should be an integer")
        player_move(turn, board, aiturn)
    if int(choice)-1 < 0 or int(choice)-1 > 8:
        print("Input should be in range (1 <= input <= 9)")
        player_move(turn, board, aiturn)
    if board[int(choice)-1] == "O" or board[int(choice)-1] == "X":
        print("This space is already taken, choose another one please")
        player_move(turn, board, aiturn)
    else:
        board[int(choice)-1] = "X" # update board when player's move have done.
        
    turn = "AI" # change turn to AI, now its ai_move
    check_win(turn, board, aiturn)

result = ""

def check_win(turn, board, aiturn):
    global result
    for n in pairs: 
        first = board[n[0]]
        second = board[n[1]]
        third = board[n[2]]
        if first == second and second == third: #Check XXX and OOO are formed or not
            if first == "O":
                result = "You lose! AI win"
                end() #To stop the game
            if first == "X": # This instruction will never run because this program is write for unbeatable Tic Tac Toe
                result = "You win!"
                end() #To stop the game
        else:
            filled_space =0
            for x in range(8):
                if board[x] != " " and board[x] != "_":
                    filled_space +=1
                if filled_space == 8:
                    result = "It's draw! You can't win."
                    end() #To stop the game
    #If game is not completed yet, then move to the next turn by calling print_board method
    print_board(turn, board, aiturn)

def end(): #To end the game and print final board
    clear_console()
    print(l.logo)
    print(l.instruction)
    print(result)
    print ("Thank you! Here is the final board.")
    print (board[0] + "|" + board[1] + "|" + board[2])
    print (board[3] + "|" + board[4] + "|" + board[5])
    print (board[6] + "|" + board[7] + "|" + board[8])
    sys.exit(0)

def ai_move(turn, board, aiturn, corner):
    already_moved = False

    def corner_choice(corner, board, already_moved):        #For corner choice [0, 2, 6, 8]
        best_choices = []
        if not already_moved:
            for n in corner:
                if board[n] == " " or board[n] == "_":
                    best_choices.append(n)
            if best_choices == []:
                side_move(sides, board, already_moved)
            else:
                board[random.choice(best_choices)] = "O"

    def side_move(sides, board, already_moved):         #Add side_move method for side move sides are [1, 3, 5, 7]
        best_choices = []
        if not already_moved:
            for n in sides:
                if board[n] == " " or board[n] == "_":
                    best_choices.append(n)
            if best_choices == []:
                corner_choice(corner, board, already_moved)
            else:
                board[random.choice(best_choices)] = "O"

    if aiturn == 1: # If it is a first move of ai
        if board[4] != "X": #to check whether that middle space is already moved by the player or not if not that taken by the ai, or if taken by the player then ai have to move corner move
            board[4] = "O" #Middle move by ai
            already_moved = True
        else:
            corner_choice(corner, board, already_moved)
            already_moved = True
    else: # To check if there is any winning or lose condition
        for n in pairs: #Offensive
            if board[n[0]] == "O" and board[n[1]] == "O" and board[n[2]] != "X":
                board[n[2]] = "O"
                already_moved = True
                break
            if board[n[0]] == "O" and board[n[2]] == "O" and board[n[1]] != "X":
                board[n[1]] = "O"
                already_moved = True
                break
            if board[n[1]] == "O" and board[n[2]] == "O" and board[n[0]] != "X":
                board[n[0]] = "O"
                already_moved = True
                break
            
        for n in pairs: #Defensive
            if already_moved == False:
                if board[n[0]] == "X" and board[n[1]] == "X" and board[n[2]] != "O":
                    board[n[2]] = "O"
                    already_moved = True
                    break
                if board[n[0]] == "X" and board[n[2]] == "X" and board[n[1]] != "O":
                    board[n[1]] = "O"
                    already_moved = True
                    break
                if board[n[1]] == "X" and board[n[2]] == "X" and board[n[0]] != "O":
                    board[n[0]] = "O"
                    already_moved = True
                    break

    if not already_moved:
        player_side_moved = []
        for n in sides:
            if board[n] == "X":
                player_side_moved.append(n)

        if aiturn == 2 and len(player_side_moved) == 1:             #I add this if statement because here is one special case where ai will lose.
            if board[1] == "X" and board[6] == "X":                 # _|P|_
                board[0] = "O"                                      # _|A|_
            elif board[1] == "X"   and board[8] == "X":             # P| |A
                board[0] = "O"                                      # To prevent this condition occured
            elif board[5] == "X" and board[0] == "X":
                board[2] = "O"
            elif board[5] == "X" and board[6] == "X":
                board[2] = "O"
            elif board[7] == "X" and board[0] == "X":
                board[6] = "O"
            elif board[7] == "X" and board[2] == "X":
                board[6] = "O"
            elif board[3] == "X" and board[2] == "X":
                board[0] = "O"
            elif board[3] == "X" and board[8] == "X":
                board[0] = "O"
            else:
                corner_choice(corner, board, already_moved)

        elif aiturn == 2 and len(player_side_moved) == 2:             #I add this if statement because here is one special case where ai will lose.
            if board[7] == "X" and board[5] == "X":                 # A|_|_
                board[2] = "O"                                      # _|A|P
            elif board[7] == "X"   and board[3] == "X":             #  |P| 
                board[0] = "O"                                      # To prevent this condition occured
            elif board[1] == "X" and board[5] == "X":
                board[0] = "O"
            elif board[1] == "X" and board[3] == "X":
                board[6] = "O"
            else:
                corner_choice(corner, board, already_moved)

        elif aiturn == 2 and board[4] == "X":
            corner_choice(corner, board, already_moved)
        else:
            # sides = [1,3,5,7]      # moved to the global
            player_sides = 0                # _|P|P         <-- where P: Player and A: AI
            for n in sides:                 # P|A|_         Else instruction is for check side spaces then move side_move method
                if board[n] == "X":         # A| | 
                    player_sides += 1
            if player_sides >= 1:
                corner_choice(corner, board, already_moved)
            else:
                side_move(sides, board, already_moved)
                # best_choices = []                     #  lines 182 to 188 moved to the side_move method
                # for n in sides:
                #     best_choices.append(n)
                # if best_choices == []:
                #     corner_choice(corner, board, already_moved)
                # else:
                #     board[random.choice(best_choices)] = "O"

    turn = "PLAYER"
    check_win(turn , board, aiturn)

# print_board(turn, board, aiturn)              # Update a start method in the program, now program start with the start method
start()