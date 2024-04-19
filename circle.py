# Andrew - adding a comment using remote

from graphics import *
from time import sleep
def main():
    win = GraphWin("My Circle", 200, 200)
    c = Circle(Point(50,50), 10)
    c.setFill("red")
    message = Text(Point(70,10), "Click to start move!")
    c.draw(win)
    message.draw(win)
    sleep(1)
    win.getMouse() # pause one more time
    for num in range (1, 30) :
        c.move (5,2.5)
        sleep(0.05)
    for num in range (1, 30) :
        c.move(-5, 2.5)
        sleep(0.05)
    win.getMouse() # pause one last time
    win.close()

main()
