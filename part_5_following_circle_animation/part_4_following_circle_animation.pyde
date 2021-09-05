# This sketch draws a circle that follows the mouse
# Youtube Playlist:
# https://www.youtube.com/playlist?list=PL5eh956CtlEQxk52EOq53pjz8qWZjcvWk

def setup():
    size(800, 800)

def draw():
    background(255, 0, 0)
    circle(mouseX, mouseY, 100)
