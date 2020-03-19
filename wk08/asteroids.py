"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
"""
import arcade
import math
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

LASER_RADIUS = 30
LASER_SPEED = 10
LASER_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2


class Point:
    '''initialize point to lower left corner as default'''

    def __init__(self):
        self.x = 0.0
        self.y = 0.0


class Velocity:
    '''initialize velocity at 1 px for both horizontal and vertical movement'''

    def __init__(self):
        self.dx = 1.0
        self.dy = 1.0


class Projectile:
    """ create the moving objects: lasers, asteroids, and ship
         that move around in outer space """

    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 10
        self.center.x = random.uniform(0, SCREEN_WIDTH - self.radius)
        self.center.y = random.uniform(0, SCREEN_HEIGHT - self.radius)
        self.velocity.dx = random.uniform(1, 5)
        self.velocity.dy = random.uniform(1, 5)
        self.alive = True
        self.angle = 45
        self.width = self.radius * 2
        self.height = self.radius * 2
        self.img = ""
        self.texture = arcade.load_texture(self.img)
        self.alpha = 255  # For transparency, 1 means transparent, 255 opaque/visible

    def draw(self):
        ''' draw projectile using constant and member variables '''
        arcade.draw_texture_rectangle(self.x, self.y, self.width, self.height, self.texture, self.angle, self.alpha)

    def advance(self):
        ''' projectile moves at the current velocity '''        
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def hit(self):
        pass

    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        pass
        # if self.center.x > SCREEN_WIDTH or self.center.x < 0 or self.center.y > SCREEN_HEIGHT or self.center.y < 0:
            # wrap around screen


class Laser(Projectile):
    ''' laser bolts are shot from the ship toward the asteroids'''

    def __init__(self):
        super().__init__()
        self.center.x = 0
        self.center.y = 0
        self.radius = LASER_RADIUS
        self.velocity.dx = LASER_SPEED
        self.velocity.dy = LASER_SPEED
        self.image = "images/laser.png"
        self.width = LASER_RADIUS * 2
        self.height = LASER_RADIUS * 2

    def draw(self):
        pass

    def fire(self, angle):
        self.angle = angle
        self.alive = True
        self.velocity.dx = math.cos(math.radians(self.angle)) * LASER_SPEED
        self.velocity.dy = math.sin(math.radians(self.angle)) * LASER_SPEED

    
class Rock_big(Projectile):
    def __init__(self):
        super().__init__()
        self.spin = BIG_ROCK_SPIN
        self.radius = BIG_ROCK_RADIUS
        self.width = BIG_ROCK_RADIUS * 2
        self.height = BIG_ROCK_RADIUS * 2
        self.speed = BIG_ROCK_SPEED
        self.center.x = random.uniform(1, SCREEN_WIDTH - self.width)
        self.center.y = random.uniform(1, SCREEN_HEIGHT - self.height)
        self.angle = 90
        self.img = "images/rock_big.png"

    def hit(self):
        pass   # split big rock into 2 medium rocks

    def rotate(self):       
        self.spin += 1
        
    def display(self):
            print("Rock coordinates: ({}, {}), velocity: ({}, {})".format(self.center.x, self.center.y, self.velocity.dx, self.velocity.dy))



class Ship(Projectile):
    """
    The ship is an image that is manipulated by arrows up/down for speed and left/right for direction.
    """

    def __init__(self):
        super().__init__()

        self.radius = SHIP_RADIUS
        self.center.x = SCREEN_WIDTH // 2
        self.center.y = SCREEN_HEIGHT // 2
        self.angle = 0

    def advance(self):
        pass

    def draw(self):
        self.angle = 180
        self.img = "images/playerShip1_orange.png"
        self.texture = arcade.load_texture(img)
        self.width = 30
        self.height = 30
        self.alpha = 1 # For transparency, 1 means not transparent
        arcade.draw_rectangle(self.x, self.y, self.width, self.height, self.texture, self.angle, self.alpha)

    def change_heading(self):
        pass

    def die(self):
        pass


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # TODO: declare anything here you need the game class to track

        self.ship = Ship()

        self.lasers = []
        self.rocks = []

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: draw each object
        #self.ship.draw()

        for laser in self.lasers:
            laser.draw()

        for rock in self.rocks:
            rock.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # TODO: Tell everything to advance or move forward one step in time
        for rock in self.rocks:
            rock.rotate()

        # TODO: Check for collisions

        #check_collisions()

    def create_rock(self):
        """
        Creates initially 5 large rocks and adds them to the list.
        :return:
        """

        # TODO: Decide what type of rock to create and append it to the list
        # choose_rock = [Rock_big(), Rock_medium(), Rock_small()]
        # number = int(random.uniform(0,3))
        for rock in range(INITIAL_ROCK_COUNT):
            big_rock = Rock_big()
            self.rocks.append(big_rock)
            rock.display()
            print(self.rocks)

    def check_collisions(self):
        """
        Checks to see if lasers have hit rocks.
        Updates scores and removes dead items.
        :return:
        """

        for laser in self.lasers:
            for rock in self.rocks:

                # Make sure they are both alive before checking for a collision
                if laser.alive and rock.alive:
                    too_close = laser.radius + rock.radius

                    if (abs(laser.center.x - rock.center.x) < too_close and abs(laser.center.y - rock.center.y) < too_close):
                        # its a hit!
                        laser.alive = False
                        #rock.hit() 

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead lasers or rocks from the list.
        :return:
        """
        for laser in self.lasers:
            if not laser.alive:
                self.lasers.remove(laser)

        for rock in self.rocks:
            if not rock.alive:
                self.rocks.remove(rock)

    def check_off_screen(self):
        """
        Checks to see if lasers or rocks have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for laser in self.lasers:
            if laser.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.lasers.remove(laser)

        for rock in self.rocks:
            if rock.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.rocks.remove(rock)

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            pass

        if arcade.key.RIGHT in self.held_keys:
            pass

        if arcade.key.UP in self.held_keys:
            pass

        if arcade.key.DOWN in self.held_keys:
            pass

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


    

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()