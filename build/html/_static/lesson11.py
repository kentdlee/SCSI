X = 1
O = -1
tokenToChar = {}
tokenToChar[X] = "X"
tokenToChar[O] = "O"
tokenToChar[0] = " "

class TicTacToeBoard:
    # The TicTacToeBoard contains a dictionary which is called data. This encapsulates 
    # the board into the TicTacToeBoard object and hides the details from those using 
    # the object. 
    def __init__(self):
        self.data = {}
    
    # Here is the set item magic method for the set item operator
    def __setitem__(self,key,val):
        self.data[key] = val
    
    # And here is the get item method.
    def __getitem__(self,key):
        return self.data[key]
    
    def eval(self):
        board = self
    
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
    
    def print(self):  
        board = self
      
        for i in range(3):
            print("|",end="")
            for j in range(3):
                print(tokenToChar[board[(i,j)]]+"|",end="")
            print('\n-------')
          
def main():
    row1 = "X _ O".split() #input("Please enter the first row of the board : ").split()
    row2 = "X X O".split() #input("Please enter the second row of the board: ").split()
    row3 = "O O X".split() #input("Please enter the third row of the board : ").split()

    # Notice that the board is created differently now. 
    board = TicTacToeBoard()

    # __setitem__ is used in the code below.
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

    # check out how the two methods below are now called. They
    # are no longer functions. They are methods which are a part
    # of the TicTacToeBoard class. 
    board.print()
    print(board.eval())


if __name__ == "__main__":
    main()