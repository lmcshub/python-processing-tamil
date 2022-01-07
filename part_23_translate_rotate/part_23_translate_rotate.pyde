# This sketch draws a grid on the canvas with labels on the axes.
# while rotating and translating
# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

def drawGrid():
    ts=15 # text size
    pad=2  # padding
    textSize(ts)
    stroke(0)
    fill(0, 0, 255)
    for x in range(0, width, 100):
        line(x, 0, x, height)
        text(x, x+pad, ts)

    for y in range(0, height, 100):
        line(0, y, width, y)
        text(y, 0+pad, y+ts)


def setup():
    size(1400, 900)

angle = 0.1
def draw():
    global angle
    background(255, 255, 255)

    push()
    translate(width/2, height/2)
    rotate(angle)
    drawGrid()
    angle = angle + 0.02
    pop()

    fill(0)
    stroke(0)
    textSize(30)
    text(angle, 50, 50)
