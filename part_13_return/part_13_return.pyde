# This sketch demonstrates how functions can return values to the caller
# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

# write draws the given input as text in the middle of the window
def write(param):
    background("#ccff00")
    text(str(param), 0, height/2)

# count the number of upper case characters in a string
def countUpper(s):
    c = 0
    for l in s:
        if l.isupper():
            c = c + 1
    return c


def setup():
    size(1000, 400)
    fill(0)
    textSize(40)
    noLoop()

    s = "Hello World"
    write(s)
    n = countUpper(s)
    write(n)
