from graphics import *
def main():
    win = GraphWin("My Circle", 100, 100)
    c = Circle(Point(50,50), 10)
    c.setFill("red")
    c.draw(win)
    win.getMouse() # pause for click in window
    c.move(10,10)
    win.getMouse() # pause one more time
    win.close()

main()
