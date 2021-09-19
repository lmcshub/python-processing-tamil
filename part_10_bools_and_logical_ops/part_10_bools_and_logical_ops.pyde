# This sketch demonstrates boolean expressions and logical operators
# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

x = -180
width = 1400
val = x <= width
f = x > width
print(val)
print(f)
bool = True
bool = False
print(bool)

isBallInsideR = x <= width
isBallInsideL = x >= 0
print(isBallInsideL and isBallInsideR)
print(x >=0 and x <= width)
isInside = isBallInsideL and isBallInsideR
print(isInside)

isBallOutsideR = x > width
isBallOutsideL = x < 0
print(isBallOutsideR or isBallOutsideL)
print(x < 0 or x > width)
print(not isInside)
