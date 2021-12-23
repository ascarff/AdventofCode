with open('4-input.txt','r') as f:
    lines = f.read().splitlines()
    n_boards = int((len(lines)-1)/6)
    
    ### Taking in the data and putting it in a 3d list.
    
    boards = [[['#' for col in range(5)] for col in range(5)] for col in range(n_boards)]
    
    board = 0
    sub_board = 0
    for i,line in enumerate(lines):
        if i==0: 
            input = line.split(',')
            continue
        if i==1: continue
        if not line:
            board+=1
            sub_board=0
        else:
            line_list=line.split()
            for j in range(5):
                boards[board][sub_board][j]=line_list[j]
            sub_board+=1
    

    def find_winning_board():
        "This function finds the first board to get bingo and returns the winning board number and the last number called."
        for i in input:
            print("i =", i)
            for n_board,board in enumerate(boards):
                for row in range(5):
                    for col in range(5):
                        if int(board[row][col])==int(i):
                            board[row][col]= -999
                            if board[row][0]==board[row][1]==board[row][2]==board[row][3]==board[row][4]==-999:
                                print("Board", n_board, "is the winner. Bingo on row", row)
                                winning_board=n_board
                                winning_num=i
                                return(winning_board, winning_num)
                            elif board[0][col]==board[1][col]==board[2][col]==board[3][col]==board[4][col]==-999:
                                print("Board", n_board, "is the winner. Bingo on col", col)
                                winning_board=n_board
                                winning_num=i
                                return(winning_board, winning_num)
                            else: continue

    winning_board, winning_num=find_winning_board()

    total_remaining = 0
    for row in range(5):
        for col in range(5):
            if boards[winning_board][row][col]!=-999:
                total_remaining+=int(boards[winning_board][row][col])
    
    final_score=int(total_remaining)*int(winning_num)
    print("Total remaining =", total_remaining, ". Winning number =", winning_num, ". Final score =", final_score)
    
