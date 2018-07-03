X = 1
O = -1
tokenToChar = {}
tokenToChar[X] = "X"
tokenToChar[O] = "O"
tokenToChar[0] = " "

def evalBoard(board):

    diag1Val = 0
    diag2Val = 0
    for i in range(3):
        rowVal = 0
        colVal = 0
        for j in range(3):
            rowVal += board[(i,j)]
            colVal += board[(j,i)]
            
        if abs(rowVal) == 3:
            return rowVal//3
        
        if abs(colVal) == 3:
            return colVal//3
        
        diag1Val += board[(i,i)]
        diag2Val += board[(i,2-i)]
        
    if abs(diag1Val) == 3:
        return diag1Val//3
    
    if abs(diag2Val) == 3:
        return diag2Val//3
    
    return 0  
 
def printBoard(board):   
    for i in range(3):
        print("|",end="")
        for j in range(3):
            print(tokenToChar[board[(i,j)]]+"|",end="")
        print('\n-------')


def main():
    row1 = "X _ O".split() #input("Please enter the first row of the board : ").split()
    row2 = "X X O".split() #input("Please enter the second row of the board: ").split()
    row3 = "O O X".split() #input("Please enter the third row of the board : ").split()
    board = {}
    
    for i in range(len(row1)):
        if row1[i] == "X": 
            board[(0,i)] = X
        elif row1[i] == "O":
            board[(0,i)] = O    
        else:
            board[(0,i)] = 0

    for i in range(len(row2)):
        if row2[i] == "X": 
            board[(1,i)] = X
        elif row2[i] == "O":
            board[(1,i)] = O    
        else:
            board[(1,i)] = 0  
            
    for i in range(len(row3)):
        if row3[i] == "X": 
            board[(2,i)] = X
        elif row3[i] == "O":
            board[(2,i)] = O    
        else:
            board[(2,i)] = 0 
            
    printBoard(board)
    print(evalBoard(board))
    
    
if __name__ == "__main__":
    main()