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

        self.gameApp = gameApp
        self.bomb = bomb
        self.rowIndex = rowIndex
        self.colIndex = colIndex
        self.matrix = matrix
        self.penup()
        #screen.tracer(0)

        self.shape("tile36.gif")
        self.screen = screen

        self.goto(30+colIndex*36,30+rowIndex*36)

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
        if self.isvisible():
            if self.bomb:
                self.shape("bomb36.gif")
                self.screen.update()
                tkinter.messagebox.showinfo(message="You blew up!! Game Over!!", title="Game Over!!!")
                self.gameApp.gameOver()
            else:
                self.ht()
                self.gameApp.decTileNum()

                # Call on the neighbors
                neighbors = []
                bombNeighbors = 0

                for i in range(self.rowIndex-1,self.rowIndex+2,1):
                    for j in range(self.colIndex-1,self.colIndex+2,1):
                        if i >= 0 and i < len(self.matrix) and j >= 0 and j < len(self.matrix):
                            if i != self.rowIndex or j != self.colIndex:
                                neighbor = self.matrix[i][j]

                                if not neighbor.bomb:
                                    neighbors.append(neighbor)
                                else:
                                    bombNeighbors = bombNeighbors+1

                if bombNeighbors == 0:
                    for neighbor in neighbors:
                        neighbor.whenLeftClicked()

                if bombNeighbors > 0:
                    if bombNeighbors == 1:
                        color = "blue"
                    elif bombNeighbors == 2:
                        color = "green"
                    elif bombNeighbors == 3:
                        color = "red"
                    elif bombNeighbors == 4:
                        color = "purple"
                    else:
                        color = "black"

                    self.color(color)

                    self.left(90)
                    self.forward(10)
                    self.write(str(bombNeighbors),align="center",font=("Arial",18,"bold"))
                    self.right(90)
                    self.forward(10)

            self.screen.update()

    # This method whenRightClicked is called when the right mouse button
    # is clicked to do the processing required of a right click on a Tile.
    def whenRightClicked(self):
        # The whenRightClicked sets the shape of the Turtle to a flag36.gif
        # and updates the screen.
        self.shape("flag36.gif")
        self.screen.update()

    # This method is called when the game has ended to display where the
    # bombs were on the board. It also tells the Tile object to ignore
    # any clicks on the Tile from that point forward.
    def gameOver(self):
        if self.bomb:
            self.shape("bomb36.gif")
        self.onclick(None)
        self.onclick(None,btn=3)

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
        self.tileNum = self.tileNum - 1
        self.tileLabel.config(text="Tiles = " + str(self.tileNum))
        if self.tileNum == 40:
            self.gameOver()
            tkinter.messagebox.showinfo(message="You didn't blow up! Congratulations!!",title="You Won!!!!")

    # This method is called from a Tile object when a bomb has been
    # been clicked. This method in turn calls gameOver on each of the
    # 256 tiles.
    def gameOver(self):
        self.running = False
        for row in self.matrix:
            for tile in row:
                tile.gameOver()
        self.screen.update()

    # This method builds the user interface and sets up event handlers
    # for the menu items.
    def buildWindow(self):

        self.canvas = tkinter.Canvas(self,width=600,height=600)
        self.canvas.pack(side=tkinter.LEFT)

        self.master.title("Minesweeper")

        theTurtle = turtle.RawTurtle(self.canvas)
        theTurtle.ht()

        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar,tearoff=0)

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

            for row in self.matrix:
                for tile in row:
                    tile.goto(-1000,-1000)

            randomNumbers = set()

            numBombs = int(self.bombVar.get())

            bombLabel.configure(text="Bombs Remaining = " + self.bombVar.get())

            for i in range(numBombs):
                r = random.randrange(256)
                while r in randomNumbers:
                    r = random.randrange(256)
                randomNumbers.add(r)


            self.matrix = []
            self.tileNum = 256
            count = 0

            for rowIndex in range(16):
                row = []

                for colIndex in range(16):
                    bomb = (count in randomNumbers)


                    aTile = Tile(self.canvas,screen,rowIndex,colIndex,self.matrix,bomb,self)
                    count = count + 1
                    row.append(aTile)

                self.matrix.append(row)

            self.screen.update()
            self.startTime = datetime.datetime.now()
            self.master.after(1000,tickTock)


        fileMenu.add_command(label="New Game",command=newGame)

        fileMenu.add_command(label="Exit",command=self.master.quit)

        bar.add_cascade(label="File",menu=fileMenu)

        self.master.config(menu=bar)

        sideBar = tkinter.Frame(self,padx=5,pady=5)
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        timeLabel = tkinter.Label(sideBar,text="Elapsed Seconds")
        timeLabel.pack()

        self.elapsedTime = tkinter.StringVar()
        self.elapsedTime.set("0")

        self.timeElapsed = tkinter.Label(sideBar,textvariable=self.elapsedTime)
        self.timeElapsed.pack()

        bombCountLabel = tkinter.Label(sideBar,text="Bomb Count")
        bombCountLabel.pack()

        bombEntry = tkinter.Entry(sideBar,textvariable=self.bombVar)
        bombEntry.pack()

        bombLabel = tkinter.Label(sideBar,text="Bombs Remaining = " + self.bombVar.get())
        bombLabel.pack()

        self.tileLabel = tkinter.Label(sideBar,text="Tiles Remaining = 256")
        self.tileLabel.pack()

        screen = theTurtle.getscreen()

        screen.setworldcoordinates(0,600,600,0)
        screen.clear()
        screen.tracer(0)
        self.screen = screen

        screen.register_shape("bomb36.gif")
        screen.register_shape("tile36.gif")
        screen.register_shape("flag36.gif")

        newGame()


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
