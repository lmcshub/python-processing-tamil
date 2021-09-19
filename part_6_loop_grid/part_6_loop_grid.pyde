# This sketch draws a grid over the window, spaced by 100 pixels
# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

size(1400, 900)
x = 0
y = 0

while x <= width:
    line(x, 0, x, height)
    x = x + 100

while y <= height:
    line(0, y, width, y)
    y = y + 100
