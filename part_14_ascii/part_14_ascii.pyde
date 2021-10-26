# This sketch demonstrates string operations and string immutability
# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

# write draws the given input as text in the middle of the window
def write(param):
    background("#ccff00")
    text(str(param), 0, height/2)

def isupper(c):
    return ord(c) >= ord('A') and ord(c) <= ord('Z')

def setup():
    size(1000, 400)
    fill(0)
    textSize(40)
    noLoop()
    s = "Hello World " * 4
    write(ord('H'))
    write(chr(72))


