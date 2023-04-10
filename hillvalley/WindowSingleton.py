from graphics import *
from Vec import Vec

# pixels per meter
ppm = 80

hole_pos = Vec(0, 5.5, 0)

valley_center = Vec(0.5, 4, 0)
hill_center = Vec(-0.5, 2, 0)


class WindowSingleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(WindowSingleton, cls).__new__(cls)
            print("new window made")
            cls.win = GraphWin("Putt Putt", 7*ppm, 8*ppm, autoflush=False)
            cls.win.setBackground(color_rgb(135, 214, 149))
            green = Rectangle(Point(2*ppm, 1*ppm), Point(5*ppm, 7*ppm))
            green.setFill(color_rgb(10, 114, 72))
            green.draw(cls.win)

            hole = Circle(Point(3.5 * ppm, (7-hole_pos.y) * ppm), 0.05 * ppm)
            hole.setFill("black")
            hole.draw(cls.win)
            
            valley = Circle(Point((3.5+valley_center.x) * ppm, (7-valley_center.y) * ppm), 1 * ppm)
            valley.setFill(color_rgb(0, 150, 0))
            valley.draw(cls.win)
            
            hill = Circle(Point((3.5+hill_center.x) * ppm, (7-hill_center.y) * ppm), 1 * ppm)
            hill.setFill(color_rgb(100, 255, 100))
            hill.draw(cls.win)
        return cls.instance

    def __call__(self):
        return self.getWindow()

    def getWindow(self):
        return self.win
