# This sketch creates bouncing balls where the mouse was clicked inside the window

# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

# positions of the balls
px = []
py = []

# speeds in x and y directions
sx = []
sy = []


def drawBall(i):
    circle(px[i], py[i], 100)

def bounceBall(i):
    global sx, sy
    if px[i] >= width or px[i] <= 0:
        sx[i] = -sx[i]
    if py[i] >= height or py[i] <= 0:
        sy[i] = -sy[i]

def createBall(x, y, vx, vy):
    global px, py, sx, sy
    px.append(x)
    py.append(y)

    sx.append(vx)
    sy.append(vy)

def moveBall(i):
    global px, py
    px[i] = px[i]+sx[i]
    py[i] = py[i]+sy[i]

def setup():
    size(800, 800)
    createBall(width/2, height/2, random(-5, 5), random(-5, 5))

def mouseClicked():
    createBall(mouseX, mouseY, random(-5, 5), random(-5, 5))

def clearScreen():
    background(255, 0, 0)

def draw():
    clearScreen()
    for i in range(len(px)):
        moveBall(i)
        bounceBall(i)
        drawBall(i)
