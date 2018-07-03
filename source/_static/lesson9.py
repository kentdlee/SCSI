row1 = input("Please enter the first row of the board : ").split()
row2 = input("Please enter the second row of the board: ").split()
row3 = input("Please enter the third row of the board : ").split()
board = {}

for i in range(len(row1)):
    if row1[i] in "XO": 
        board[(0,i)] = row1[i] 
    else:
        board[(0,i)] = " "
    
for i in range(len(row2)):
    if row2[i] in "XO": 
        board[(1,i)] = row2[i] 
    else:
        board[(1,i)] = " "

for i in range(len(row3)):
    if row3[i] in "XO": 
        board[(2,i)] = row3[i] 
    else:
        board[(2,i)] = " "  
    
for i in range(3):
    print("|",end="")
    for j in range(3):
        print(str(board[(i,j)])+"|",end="")
    print('\n-------')
