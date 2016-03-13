from graphics import *
from time import sleep
def main():
    win = GraphWin("My Circle", 200, 200)
    c = Circle(Point(50,50), 10)
    c.setFill("red")
    c.draw(win)
    win.getMouse() # pause for click in window
    c.move(10,10)
    win.getMouse() # pause one more time
    for num in range (1, 30) :
        c.move (5,2.5)
        sleep(0.05)
    win.close()

main()
