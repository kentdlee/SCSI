# The imports include turtle graphics and tkinter modules.
# The colorchooser and filedialog modules let the user
# pick a color and a filename.
import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom
import random

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
        
        def leftClickHandler(x,y):
            self.whenLeftClicked()
            
        self.onclick(leftClickHandler)
        
        def rightClickHandler(x,y):
            self.whenRightClicked()
            
        self.onclick(rightClickHandler,btn=3)        
        
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
                    self.forward(18)
                    self.write(str(bombNeighbors),align="center",font=("Arial",18,"bold"))
                    self.right(90)
                    self.forward(18)
                    
                         
                        
            self.screen.update()
        
    def whenRightClicked(self):
        self.shape("flag36.gif")
        self.screen.update()  
    
    def gameOver(self):
        if self.bomb:
            self.shape("bomb36.gif")
        self.onclick(None)
        self.onclick(None,btn=3)


class MineSweepApplication(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.matrix = []
        self.buildWindow()
        
    def decTileNum(self):
        self.tileNum = self.tileNum - 1
        self.tileLabel.config(text="Tiles = " + str(self.tileNum))
        if self.tileNum == 40:
            self.gameOver()
            tkinter.messagebox.showinfo(message="You didn't blow up! Congratulations!!",title="You Won!!!!")

    def gameOver(self):
        for row in self.matrix:
            for tile in row:
                tile.gameOver()
        self.screen.update()

    def buildWindow(self):

        self.master.title("Minesweeper")

        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar,tearoff=0)

        def newGame():
            screen = theTurtle.getscreen()
            screen.setworldcoordinates(0,600,600,0)  
            screen.clear()
            screen.tracer(0)
            self.screen = screen
            
            screen.register_shape("bomb36.gif")
            screen.register_shape("tile36.gif")
            screen.register_shape("flag36.gif")
            
            for row in self.matrix:
                for tile in row:
                    tile.goto(-1000,-1000)            
            
            randomNumbers = []
            
            for i in range(40):
                r = random.randrange(256)
                while r in randomNumbers:
                    r = random.randrange(256)
                randomNumbers.append(r)
    
            
            self.matrix = []
            self.tileNum = 256
            count = 0
            
            for rowIndex in range(16):
                row = []
                
                for colIndex in range(16):
                    bomb = (count in randomNumbers)

                        
                    aTile = Tile(canvas,screen,rowIndex,colIndex,self.matrix,bomb,self)
                    count = count + 1                
                    row.append(aTile)
                    
                self.matrix.append(row)
                
            self.screen.update()
                    

        fileMenu.add_command(label="New Game",command=newGame)
     
        fileMenu.add_command(label="Exit",command=self.master.quit)

        bar.add_cascade(label="File",menu=fileMenu)

        self.master.config(menu=bar)

        canvas = tkinter.Canvas(self,width=600,height=600)
        canvas.pack(side=tkinter.LEFT)

        theTurtle = turtle.RawTurtle(canvas)
        theTurtle.ht()

        newGame()          

        sideBar = tkinter.Frame(self,padx=5,pady=5)
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        bombLabel = tkinter.Label(sideBar,text="Bombs = 40")
        bombLabel.pack()
        
        self.tileLabel = tkinter.Label(sideBar,text="Tiles = 256")
        self.tileLabel.pack()        


def main():
    root = tkinter.Tk()
    minesweepApp = MineSweepApplication(root)

    minesweepApp.mainloop()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()