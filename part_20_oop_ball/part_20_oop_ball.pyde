# This sketch demonstrates Object Oriented Programming
# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

# List of Ball objects
balls = []

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

def clearScreen():
    background(255, 0, 0)


def mouseClicked():
    balls.append(Ball(mouseX, mouseY, random(-5, 5), random(-5, 5)))

def setup():
    size(800, 800)
    b = Ball(width/2, height/2, random(-5, 5), random(-5, 5))
    balls.append(b)

def draw():
    clearScreen()
    for b in balls:
        b.move()
        b.draw()

