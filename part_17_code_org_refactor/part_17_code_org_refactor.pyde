# This sketch bounces a ball inside the window in all directions.
# This has code refactored into functions, compared to the previous version.

# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

# position of the ball
px = 0
py = 0

# speed in x and y directions
sx = 0
sy = 0

def drawBall():
    circle(px, py, 100)

def bounceBall():
    global sx, sy
    if px >= width or px <= 0:
        sx = -sx
    if py >= height or py <= 0:
        sy = -sy

def createBall(x, y, vx, vy):
    global px, py, sx, sy
    px = x
    py = y

    sx = vx
    sy = vy

def moveBall():
    global px, py
    px = px+sx
    py = py+sy

def setup():
    size(800, 800)
    createBall(width/2, height/2, random(5, 10), random(5, 10))

def clearScreen():
    background(255, 0, 0)

def draw():
    clearScreen()
    moveBall()
    bounceBall()
    drawBall()
