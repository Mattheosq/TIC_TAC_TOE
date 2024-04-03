from random import randrange

board =[["_" for i in range(3)] for j in range(3)]
player = ""
enemy = ""
counter = 1
first_turn = True


for row in board:
    for index in range(len(row)):
        row[index] = counter
        counter += 1
counter = 0
# functions
    
def choose_sign():
    global player, enemy
    while True:
        player = input("Choose your sign. Input \"o\" or \"x\": ")
        if player == "o" or player == "x":
            print("You play as " + player + "\n")
            if player == "o":
                enemy = "x"
            else:
                enemy = "o"
            break
        else:
            print("Wrong input")
            
def board_sketch(enemy_turn):
    if enemy_turn: print("Enemy's turn")
    print(f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+
    
                    """)

def set_position(enemy_turn):
    global first_turn
    if enemy_turn:
        if first_turn:
            board[1][1] = enemy
            first_turn = False
        else:
           while True:
               pos = randrange(1,10)
               for row in board:
                   for index in range(len(row)):
                       if row[index] == pos:
                           row[index] = enemy
                           return #forces exit from function
            
    else:
        print("Your turn")
        while True:
            pos = int(input("Enter a number(1-9): "))
            if pos >= 1 and  pos <= 9:
                for row in board:
                    for index in range(len(row)):
                        if row[index] == pos:
                            row[index] = player
                            return
                print("Field is already marked")
            else:
                print("Wrong input data. Try again.")
                
def check_status(enemy_turn):
    #row win check
    for row in board:
        counter = 0
        for index in range(len(row)-1):
            if row[index] == row[index+1]:
                counter += 1
        if counter == 2:
            if enemy_turn:
                return 3
            else:
                return 2
            
    #column win check
    transposed_board = [[board[i][j] for i in range(3)] for j in range(3)]
    for column in transposed_board:
        counter = 0
        for index in range(len(column)-1):
            if column[index] == column[index+1]:
                counter += 1
        if counter == 2:
            if enemy_turn:
                return 3
            else:
                return 2
    #diagonally win check
    for row in range(len(board)-2):
        for col in range(len(board)-2):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2]:
                if enemy_turn:
                    return 3
                else:
                    return 2
            if board[row][col+(len(board)-1)] == board[row+1][col+(len(board)-1)-1] == board[row+2][col+(len(board)-1)-2]:
                if enemy_turn:
                    return 3
                else:
                    return 2
        
    
    #continue
    return 0
    
    
    
                
        
def tic_toc():
    choose_sign()
    enemy_turn = True
    i = 0
    while i < 9:
        print("Turn "+str(i+1))
        set_position(enemy_turn) # sets adequate sign
        board_sketch(enemy_turn)
        status = check_status(enemy_turn) # 0 - continue, 2 - player win, 3 - computer win
        if status == 0:
            enemy_turn = not enemy_turn
        elif status == 2:
            print("Game result: PLAYER WINS")
            return
        elif status == 3:
            print("Game result: COMPUTER WINS")
            return
        i += 1
    else:
        print("Game result: TIE")
        
        
tic_toc()
        



