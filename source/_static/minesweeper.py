# The imports include turtle graphics and tkinter modules along with a couple
# of other miscellaneous modules.
import turtle
import tkinter
import tkinter.filedialog
import random
import datetime


# The Tile class inherits from RawTurtle. A RawTurtle is a Turtle but we
# get to say which canvas it will draw on when it is created. There are
# a number of arguments passed to the Tile object when it is created
# which are used later in the development of this application.
class Tile(turtle.RawTurtle):
    def __init__(self,canvas,screen,rowIndex,colIndex,matrix,bomb,gameApp):
        super().__init__(canvas)

        # The following three lines of code call the whenLeftClicked when the
        # left mouse button is clicked on a Tile (i.e. Turtle) object. The
        # self.onclick registers the event handler called leftClickHander
        # so it is called whenever the left mouse button is clicked.
        def leftClickHandler(x,y):
            self.whenLeftClicked()

        self.onclick(leftClickHandler)

        # The following three lines of code call the whenRightlicked when the
        # right mouse button is clicked on a Tile (i.e. Turtle) object.
        def rightClickHandler(x,y):
            self.whenRightClicked()

        self.onclick(rightClickHandler,btn=2)

    # This method whenLeftClicked is called when the left mouse button
    # is clicked to do the processing required of a left click on a Tile.
    def whenLeftClicked(self):
        # See the web page for a description of what happens when a tile
        # is clicked.
        pass

    # This method whenRightClicked is called when the right mouse button
    # is clicked to do the processing required of a right click on a Tile.
    def whenRightClicked(self):
        # The whenRightClicked sets the shape of the Turtle to a flag36.gif
        # and updates the screen.
        pass

    # This method is called when the game has ended to display where the
    # bombs were on the board. It also tells the Tile object to ignore
    # any clicks on the Tile from that point forward.
    def gameOver(self):
        pass

# The MineSweepApplication inherits from tkinter's Frame class which corresponds
# to a part of a window. A frame is a component of a window in which things
# can be drawn or widgets can be placed.
class MineSweepApplication(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.matrix = []
        self.bombVar = tkinter.StringVar()
        self.bombVar.set("40")
        self.buildWindow()
        self.running = True

    # This method decrements the number of unclicked tiles and displays
    # the number in its label. Then it checks for gameover by looking
    # to see if only 40 tiles are left unclicked. If so, they must all
    # be bombs and the user wins.
    def decTileNum(self):
        pass

    # This method is called from a Tile object when a bomb has been
    # been clicked. This method in turn calls gameOver on each of the
    # 256 tiles.
    def gameOver(self):
        pass

    # This method builds the user interface and sets up event handlers
    # for the menu items.
    def buildWindow(self):
        # Replace the next line with your code from lesson 14
        print("I was here!")

        # This method is there to count the seconds that have passed
        # since the start of the game and display those seconds on the board.
        def tickTock():
            currentTime = datetime.datetime.now()
            elapsed = currentTime - self.startTime
            elapsedSeconds = elapsed.seconds
            self.elapsedTime.set(str(elapsedSeconds))
            if self.running:
                self.master.after(1000,tickTock)

        # This method is called to get the game ready to play. It creates the
        # 256 tiles and places them on the board and sets a few other variables
        # in preparation for playing.
        def newGame():
            pass



def main():
    # root is the main window. Then the minesweepApp will be a Frame
    # that fills that window.
    root = tkinter.Tk()
    minesweepApp = MineSweepApplication(root)

    # This calls the event loop so that events get processed since
    # this is an event driven application.
    minesweepApp.mainloop()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()
