# This sketch demonstrates the use of tuples to return multiple values from a function
# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

from __future__ import division

# The ball object
b = None

class Ball():
    def __init__(self, px, py, sx, sy):
        self.px = px
        self.py = py
        self.sx = sx
        self.sy = sy
        self.r = 100

    def draw(self):
       circle(self.px, self.py, self.r)

    def move(self):
        self.px = self.px + self.sx
        self.py = self.py + self.sy
        self.bounce()

    def bounce(self):
        if self.px >= width or self.px <= 0:
            self.sx = -self.sx

        if self.py >= height or self.py <= 0:
            self.sy = -self.sy

    # returns a tuple containing the x and y positions of the ball
    def getPosition(self):
        return int(self.px), int(self.py)

def clearScreen():
    background(255, 0, 0)

def setup():
    global b
    size(800, 800)
    b = Ball(width//2, height//2, random(-5, 5), random(-5, 5))

def draw():
    clearScreen()
    b.move()
    b.draw()

    pos = b.getPosition()
    textSize(30)
    text(str(pos), width//2, height//2)
