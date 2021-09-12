# This sketch moves a ball across the window
# while demonstrating the concept of variable scopes.
# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

# previous position of the ball
px = 0
py = 0

def drawBall(x, y):
    global px, py
    background(255, 0, 0)
    circle(x, y, 100)
    px = x
    py = y
    

def setup():
    size(800, 800)
    drawBall(width/2, height/2)
    

def draw(): 
    drawBall(px + 1, py)
    
