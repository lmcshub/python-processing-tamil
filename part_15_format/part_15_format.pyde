# This sketch demonstrates string operations and string immutability
# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk


# write draws the given input as text in the middle of the window
def write(param):
    background("#ccff00")
    text(str(param), 0, height/2)

def isupper(c):
    return ord(c) >= ord('A') and ord(c) <= ord('Z')

def isupper_verbose(c):
    ans = ord(c) >= ord('A') and ord(c) <= ord('Z')
    y = "Yes"
    n = ""
    if not ans:
        y = "No"
        n = "not"

    # Two different ways to create formatted strings in Python 2.
    s = "%s. '%c' is %s upper case."%(y, c, n)
    s = "{}. '{}' is {} upper case.".format(y, c, n)
    return s

def setup():
    size(1000, 400)
    fill(0)
    textSize(40)
    noLoop()
    s = "Hello World " * 4
    write(ord('H'))
    write(chr(72))
    write("Is H upper?\n" + str(isupper('H')))
    write(isupper_verbose('w'))



