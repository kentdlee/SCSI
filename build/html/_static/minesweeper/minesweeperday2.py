import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom
import random

class Tile(turtle.RawTurtle):
    def __init__(self,canvas,screen,rowIndex,colIndex,matrix,bomb,gameApp):
        super().__init__(canvas)
        
        

class MineSweepApplication(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.matrix = []
        self.buildWindow()

    def buildWindow(self):
        canvas = tkinter.Canvas(self,width=600,height=600)
        canvas.pack(side=tkinter.LEFT)
    
        theTurtle = turtle.RawTurtle(canvas)
        theTurtle.ht()        
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