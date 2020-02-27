"""
File: check05a.py

To this file you need to add:

A Ship class with member variables: x, y, dx, dy
It should have two simple method: advance and draw

Then to the provided Game class, add calls to your draw
and advance.

You should not need to modify the main function.
"""

import random


# TODO: Define your Ship class here



class Game:
    def __init__(self, dx, dy):
        self.ship = Ship()

        # Set the ship's initial velocity
        self.ship.dx = dx
        self.ship.dy = dy

    def on_draw(self):
        #TODO: Add a call to the draw method of self.ship


    def update(self):
        #TODO: Add a call to the advance method of self.ship



def main():
    """
    The main function sets up the game class and calls its
    methods repeatedly, just like will happen in actual games.
    
    You should not need to change anything here:
    """

    seed = input("Enter a random seed: ")
    random.seed(seed)

    dx = random.randint(-4, 4)
    dy = random.randint(-4, 4)

    print("Starting the ship with velocity ({}, {})".format(dx, dy))

    game = Game(dx, dy)

    for i in range(20):
        game.update()
        game.on_draw()

if __name__ == "__main__":
    main()
