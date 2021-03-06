import sys

"""
use this script as the backend to the tictactoe.py frontend.
"""

# The eprint function can be used instead of print to print debugging information
# to the screen while the print function is used to send information to the frontend
# code that started this module.

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

Human = -1
Computer = 1

# put you Board class here.
class Board:
    # When a board is constructed, you may want to make a copy of the board.
    def __init__(self, board=None):

        self.data = {}
        for i in range(3):
            for j in range(3):
                if board==None:
                    self.data[(i,j)] = Dummy()
                else:
                    self.data[(i,j)] = board[(i,j)]


    # The getitem method is used to index into the board. It should
    # return a row of the board. That row itself is indexable (it is just
    # a list) so accessing a row and column in the board can be written
    # board[row][column] because of this method.
    def __getitem__(self,key):
        return self.data[key]

    def __setitem__(self,key,val):
        self.data[key] = val

    # This hash method is necessary eventually to memoize the tic tac toe
    # program. Memoization is a technique that can significantly speed up
    # search when the same paths are encountered multiple times.
    # It should return an integer that uniquely identifies
    # the state of the board.
    def __hash__(self):
        val = 0
        for i in range(3):
            for j in range(3):
                val += val*3 + self.data[(i,j)].eval()+1

        return val

    # This method should return true if the two boards, self and other,
    # represent exactly the same state.
    #def __eq__(self,other):
    #    if other == None:
    #        return False
    # Uncomment and finish the code above to complete the memoization code.

    # This method will mutate this board to contain all dummy
    # entries. This way the board can be reset when a new game
    # is selected. It should NOT be used except when starting
    # a new game.
    def reset(self):
        for i in range(3):
            for j in range(3):
                self.data[(i,j)] = Dummy()

    # This method should return an integer representing the
    # state of the board. If the computer has won, return 1.
    # If the human has won, return -1. Otherwise, return 0.
    def eval(self):
        for row in range(3):
            rowSum = 0
            for col in range(3):
                rowSum+= self[(row,col)].eval()

            if abs(rowSum) == 3:
                return rowSum//3

        for col in range(3):
            colSum = 0
            for row in range(3):
                colSum += self[(row,col)].eval()

            if abs(colSum) == 3:
                return colSum//3

        diagSum = 0

        for i in range(3):
            diagSum+=self[(i,i)].eval()

        if abs(diagSum) == 3:
            return diagSum//3

        diagSum = 0

        for i in range(3):
            j = 2-i
            diagSum+=self[(i,j)].eval()

        if abs(diagSum) == 3:
            return diagSum//3

        return 0

    # This method should return True if the board
    # is completely filled up.
    def full(self):
        for row in range(3):
            for col in range(3):
                if self[(row,col)].eval() == 0:
                    return False

        return True

    # This method should return True if the board
    # is completely empty.
    def empty(self):
        for row in range(3):
            for col in range(3):
                if abs(self.data[(row,col)].eval()) == 1:
                    return False

        return True

    def __repr__(self):
        return "Board("+repr(self.data)+",None)"

    def __str__(self):
        s = ""
        for row in range(3):
            for col in range(3):
                s+="|"+str(self.data[(row,col)])+"|"
            s+="\n"

        return s


class Dummy:
    def __init__(self):
        pass

    # You can call eval to get its value.
    def eval(self):
        return 0

    def goto(self,x,y):
        pass

    def __repr__(self):
        return "Dummy()"

    def __str__(self):
        return " "

class X:
    def __init__(self):
        pass

    # You can call eval to get its value.
    def eval(self):
        return Computer

    def __repr__(self):
        return "X()"

    # calling str(v) where v is an X object will return the "X" as a string.
    # This is useful if you write a __str__ method for your Board class
    # as well. You can use this __str__ in your Board class __str__.
    def __str__(self):
        return "X"

class O:
    def __init__(self):
        pass

    # You can call eval to get its value.
    def eval(self):
        return Human

    def __repr__(self):
        return "O()"

    def __str__(self):
        return "O"

# Put your minimax function here.


def humanTurn(gameBoard):
    move = int(input())
    eprint("In humanTurn")
    row = move//3
    col = move%3

    if gameBoard.full():
        print(1)
    elif abs(gameBoard.eval()) == 1:
        # game is already over
        print(1)
    elif gameBoard[(row,col)].eval() != 0:
        # move was already made
        print(2)
    else:
        # Using X and O as classes will help
        # if printing the board.
        gameBoard[(row,col)] = O()
        print(0)

def computerTurn(gameBoard):
    # Here you should write your computerTurn function.
    pass

def main():
    gameBoard = Board()

    while True:
        #The following eprint can be really handy during debugging so you
        #can see how to interact with the program given the board contents.
        #The code on the next line requires you to define a __str__ method
        #for your Board class which returns a string representation of the
        #board.
        eprint(gameBoard)
        eprint("Enter a message Id: ")
        msgId = int(input())

        if msgId == 2:
            humanTurn(gameBoard)

        elif msgId == 0:
            gameBoard.reset() # or gameBoard = Board()
            print("0")

        elif msgId == 1:
            computerTurn(gameBoard)

        elif msgId == 3:
            status = gameBoard.eval()

            if status == Computer:
                print(1)
            elif status == Human:
                print(2)
            else:
                if gameBoard.full():
                    print(3)
                else:
                    print(0)
        else:
            eprint("Something is wrong with the front-end")
            print(1)

main()
