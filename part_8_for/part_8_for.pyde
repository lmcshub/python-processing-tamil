# This sketch draws vertical lines at the given list of x co-ordinates
# using a for loop.
# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

size(900, 900)
strokeWeight(5)

def drawVLines(xList):
    for x in xList:      
        line(x, 0, x, height)

drawVLines([100, 200, 300, 600, 800])



























x = 10
x = 200
x = 300

x = [100, 200, 300]
