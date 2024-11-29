from spacecode import (
    Game,
    Color
)
import math
import time
import random

# EXERCICE : We want our spacehip to patrol in a four direction square loop, clockwise and starting from the top left corner


# 1. Connect to a new game with a valid host or ip address, with your name and choose the color of your player (color is a string as any css color cf. https://www.w3schools.com/cssref/css_colors_legal.php)
game = Game(host="localhost", username="YOUR NAME", color=Color.getRandomColor())

# Define a variable me with your player instance : your spaceship !
me = game.currentPlayer

# First, we position our spaceship at the top left corner of the game board, with some space (e.g. 20 px from the corner on the x and y axis)
# you can set the x and y attribute 

## TODO

# save the starttime of our script
starttime = time.time()

# Loop for ever
while True:
   
    # We defined a variable that give the time in second for each direction
    second_per_direction = 5
    direction = math.floor((time.time()-starttime) / second_per_direction % 4)

    # to help you understand the value of direction, we can print its value to the output
    print( f"Direction = {direction}")

    # Now, depending on the value of direction, set the rotation attribute of our spaceship in degrees of the spaceship (0 for North/Up, 90 for East/Right, 180 fro South/Down, 270 for West/Left)

    ## TODO

    # Call the method moveForward()) on me to move our spaceship forward
    
    ## TODO

    # Call the method shoot() on me to shoot a bullet 
    
    ## TODO
    
    # Must be called at the end of each loop for the game to update
    game.update()