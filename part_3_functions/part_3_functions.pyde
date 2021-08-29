# This sketch draws multiple Flags (with Incomplete Chakra) using functions
# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

# Reference for flag size and colors:
# Refer: https://en.wikipedia.org/wiki/Flag_of_India

# drawFlag draws a Flag of size 450x300 
# at x, y co-ordinates
def drawFlag(x, y):
    fh = 300
    fw = 450
    fill("#FF9933") # saffron
    rect(x, y, 450, 100)
    fill("#FFFFFF") # white
    rect(x, y+100, 450, 100)
    fill("#138808") # green
    rect(x, y+200, 450, 100)
    fill("#000080") # blue
    circle(x+fw/2, y+fh/2, 90)

  
# draw everything
size(1400, 900)
background("#aabbcc")
noStroke()
drawFlag(100, 100)
drawFlag(700, 100)
drawFlag(100, 500)
drawFlag(700, 500)
