# This sketch is an animated python processing version of the 10print program

# Refer: http://10print.org

# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

s = 50
x = 0
y = 0

def setup():
    size(900, 900)
    background(255, 255, 0)
    strokeWeight(5)

def draw():
    global x, y

    if random(1) > 0.5:
        line(x, y, x+s, y+s)
    else:
        line(x, y+s, x+s, y)

    x = x+s
    if x >= width:
        x = 0
        y = y+s

    if y >= height:
        noLoop()

