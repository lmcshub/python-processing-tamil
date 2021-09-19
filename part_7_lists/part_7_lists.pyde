# This sketch draws vertical lines
# with the drawVLines function
# that takes a list of x co-ordinates as input
# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

size(900, 900)
strokeWeight(5)

def drawVLines(xList):
    i = 0
    while i < len(xList):
        line(xList[i], 0, xList[i], height)
        i = i+1

drawVLines([100, 200, 300, 600, 800])




























x = 10
x = 200
x = 300

x = [100, 200, 300]
