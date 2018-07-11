import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom
import random

# The Tile class inherits from RawTurtle. A RawTurtle is a Turtle but we
# get to say which canvas it will draw on when it is created. There are
# a number of arguments passed to the Tile object when it is created
# which are used later in the development of this application.
class Tile(turtle.RawTurtle):
    def __init__(self,canvas,screen,rowIndex,colIndex,matrix,bomb,gameApp):
        super().__init__(canvas)

# The MineSweepApplication inherits from tkinter's Frame class which corresponds
# to a part of a window. A frame is a component of a window in which things
# can be drawn or widgets can be placed.
class MineSweepApplication(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.matrix = []
        self.buildWindow()

    def buildWindow(self):
        print("I was here!")


def main():
    # root is the main window. Then the minesweepApp will be a Frame
    # that fills that window.
    root = tkinter.Tk()
    minesweepApp = MineSweepApplication(root)

    # This calls the event loop so that events get processed since
    # this is an event drive application. 
    minesweepApp.mainloop()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()
