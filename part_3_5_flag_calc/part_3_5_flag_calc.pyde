# This sketch draws multiple Flags using functions
# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

# Reference for flag size and colors:
# Refer: https://en.wikipedia.org/wiki/Flag_of_India

from __future__ import division

# drawFlag draws a Flag of heigh fh at
# (x, y) co-ordinates
def drawFlag(x, y, fh):
    fw = fh//2*3
    bh = fh//3
    fill("#FF9933") # saffron
    rect(x, y, fw, bh)
    fill("#FFFFFF") # white
    rect(x, y+bh, fw, bh)
    fill("#138808") # green
    rect(x, y+(2*bh), fw, bh)
    fill("#000080") # blue
    circle(x+fw/2, y+fh/2,bh*9//10)


# draw everything
size(1400, 900)
background("#aabbcc")
noStroke()
drawFlag(100, 100, 300)
drawFlag(700, 100, 30)
drawFlag(100, 500, 90)
drawFlag(700, 500, 120)
