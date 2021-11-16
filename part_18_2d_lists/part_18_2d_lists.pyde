# This sketch creates bouncing balls where the mouse was clicked inside the window

# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

# list of ball info. each items is in-turn another list.
balls = []

#index of various info in the list of balls
PX = 0 # x position
PY = 1 # y position
SX = 2 # x velocity/speed
SY = 3 # y velocity/speed

def drawBall(i):
    circle(balls[i][PX], balls[i][PY], 100)

def bounceBall(i):
    global balls
    if balls[i][PX] >= width or balls[i][PX] <= 0:
        balls[i][SX] = -balls[i][SX]

    if balls[i][PY] >= height or balls[i][PY] <= 0:
        balls[i][SY] = -balls[i][SY]

def createBall(x, y, vx, vy):
    balls.append([x, y, vx, vy])

def moveBall(i):
    global balls
    balls[i][PX] = balls[i][PX]  + balls[i][SX] 
    balls[i][PY] = balls[i][PY]  + balls[i][SY]

def setup():
    size(800, 800)
    createBall(width/2, height/2, random(-5, 5), random(-5, 5))

def mouseClicked():
    createBall(mouseX, mouseY, random(-5, 5), random(-5, 5))

def clearScreen():
    background(255, 0, 0)

def draw():
    pass
    clearScreen()
    for i in range(len(balls)):
        moveBall(i)
        bounceBall(i)
        drawBall(i)
