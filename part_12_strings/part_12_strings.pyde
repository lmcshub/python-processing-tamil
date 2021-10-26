# This sketch demonstrates string operations and string immutability
# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

# write draws the given input as text in the middle of the window
def write(param):
    background("#ccff00")
    text(str(param), 0, height/2)

def setup():
    size(1000, 400)
    fill(0)
    textSize(40)
    s = "Hello World"
    write(s)
    noLoop()
    c = s[1]
    # s[1] = 'E' # Invalid operation. Strings are immutable.

    write(s + " again")
    write(s * 3)
    write("or" in s)
    write(s.find("or"))
    up = s.upper()
    low = s.lower()
    write(low)
