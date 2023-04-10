from graphics import *
from Vec import Vec

# pixels per meter
ppm = 80

hole_pos = Vec(-1, 0.5, 0)

valley_center = Vec(0.5, 4, 0)
hill_center = Vec(-0.5, 2, 0)

wall_corners = [(Vec(hill_center.x, 0, 0), hill_center), (hill_center, valley_center)]


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

            hole = Circle(Point((3.5+hole_pos.x) * ppm, (7-hole_pos.y) * ppm), 0.05 * ppm)
            hole.setFill("black")
            hole.draw(cls.win)
            
            valley = Circle(Point((3.5+valley_center.x) * ppm, (7-valley_center.y) * ppm), 1 * ppm)
            valley.setFill(color_rgb(0, 150, 0))
            valley.draw(cls.win)
            
            hill = Circle(Point((3.5+hill_center.x) * ppm, (7-hill_center.y) * ppm), 1 * ppm)
            hill.setFill(color_rgb(100, 255, 100))
            hill.draw(cls.win)
            
            for w in wall_corners:
                wall = Line(Point((3.5+w[0].x) * ppm, (7-w[0].y) * ppm), Point((3.5+w[1].x) * ppm, (7-w[1].y) * ppm))
                wall.draw(cls.win)
        return cls.instance

    def __call__(self):
        return self.getWindow()

    def getWindow(self):
        return self.win
