# This sketch moves a ball inside the window in all directions.
# WASD keys can be used to steer the ball in different directions
# while hitting any other key would halt it.

# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

# previous position of the ball
px = 0
py = 0
# speed in x and y directions
sx = random(5, 10)
sy = random(5, 10)

def drawBall(x, y):
    global px, py
    background(255, 0, 0)
    circle(x, y, 100)
    px = x
    py = y

def updateDir():
    global sx, sy
    if px >= width or px <= 0:
        sx = -sx
    if py >= height or py <= 0:
        sy = -sy

def setup():
    size(800, 800)
    drawBall(width/2, height/2)


def draw():
    updateDir()
    drawBall(px+sx, py+sy)

def keyPressed():
    global sy, sx
    if (key == 'w' or key == 'W') and sy > 0:
        sy = -sy
    elif (key == 's' or key == 'S') and sy < 0:
        sy = -sy
    elif (key == 'a' or key == 'A') and sx > 0:
        sx = -sx
    elif (key == 'd' or key == 'D') and sx < 0:
        sx = -sx
    else:
        sx = sy = 0

