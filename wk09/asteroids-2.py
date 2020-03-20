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
    '''initialize point to center of screen as default'''

    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2


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
        self.angle = random.uniform(0, 360)
        self.center.x = random.uniform(0, SCREEN_WIDTH - self.radius)
        self.center.y = random.uniform(0, SCREEN_HEIGHT - self.radius)
        self.velocity.dx = math.cos(math.radians(self.angle))
        self.velocity.dy = math.cos(math.radians(self.angle))
        self.alive = True
        self.img = "images/rock_big.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.alpha = 255  # For transparency, 1 means transparent, 255 opaque/visible

    def draw(self):
        ''' draw projectile using constant and member variables '''
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, self.alpha)

    def advance(self):
        ''' projectile moves at the current velocity '''        
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    ''' @abstract? '''
    def hit(self):
        pass

    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.center.x >= SCREEN_WIDTH + self.texture.width / 2:
            self.center.x = 0        
        if self.center.x <= 0 - self.texture.width / 2:
            self.center.x = SCREEN_WIDTH
        if self.center.y >= SCREEN_HEIGHT + self.texture.height / 2:
            self.center.y = 0
        if self.center.y <= 0 - self.texture.height / 2:
            self.center.y = SCREEN_HEIGHT
        

class Ship(Projectile):
    """
    The ship is an image that is manipulated by arrows up/down for speed and left/right for direction.
    """
    def __init__(self):
        super().__init__()
        self.center.x = SCREEN_WIDTH / 2
        self.center.y - SCREEN_HEIGHT / 2
        self.radius = SHIP_RADIUS
        self.img = "images/ship1.png"
        self.texture = arcade.load_texture(self.img)

    def advance(self):
        pass

    def change_heading(self):
        pass

    def die(self):
        pass

    def hit(self):
        self.alive = False

    
class Rock_big(Projectile):
    def __init__(self):
        super().__init__()
        self.radius = BIG_ROCK_RADIUS
        self.velocity.dx = math.cos(math.radians(self.angle)) * BIG_ROCK_SPEED
        self.velocity.dy = math.sin(math.radians(self.angle)) * BIG_ROCK_SPEED
        self.speed = BIG_ROCK_SPEED
        self.img = "images/rock_big.png"
        self.texture = arcade.load_texture(self.img)
        self.spin = BIG_ROCK_SPIN

    def draw(self):      
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, self.alpha)

    def hit(self):
        '''  # split big rock into 2 medium and 1 small rocks, original destroyed and removed from game '''
        self.alive = False
        medium1 = Rock_medium(5)
        medium2 = Rock_medium(-5)
        small1 = Rock_small(5,0)

    def rotate(self):       
        self.angle += self.spin

    
class Rock_medium(Rock_big):
    def __init__(self, dy):
        super().__init__()
        self.radius = MEDIUM_ROCK_RADIUS
        self.img = "images/rock_medium.png"
        self.texture = arcade.load_texture(self.img)
        self.spin = MEDIUM_ROCK_SPIN

    def draw(self):       
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, self.alpha)

    def hit(self):
        """ split medium rock into 2 small rocks, original destroyed and removed from game   """ 
        self.alive = False
        #  split rocks have +1.5 velocity up/right, 1.5 down/left
        split1 = Rock_small(1.5, 1.5)
        split2 = Rock_small(-1.5, -1.5)  

    def rotate(self):       
        self.angle += self.spin

    
class Rock_small(Rock_big):
    def __init__(self, dx, dy):
        super().__init__()
        self.radius = SMALL_ROCK_RADIUS
        self.img = "images/rock_small.png"
        self.texture = arcade.load_texture(self.img)
        self.spin = SMALL_ROCK_SPIN

    def draw(self):       
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, self.alpha)

    def hit(self):
        self.alive = False  # destroyed and removed from game

    def rotate(self):       
        self.angle += self.spin
        
    def display(self):
        print("Rock coordinates: ({}, {})".format(self.center.x, self.center.y))
        print("velocity: ({}, {})".format(self.velocity.dx, self.velocity.dy))


class Laser(Ship):
    """ laser bolts are shot from the ship toward the asteroids, start with the same velocity of the ship (speed and direction) plus 10 pixels per frame in the direction the ship is pointed. """

    def __init__(self):
        super().__init__()
        self.radius = LASER_RADIUS
        self.velocity.dx = LASER_SPEED
        self.velocity.dy = LASER_SPEED
        self.alive = True
        self.width = LASER_RADIUS * 2
        self.height = LASER_RADIUS * 2
        self.img = "images/laser.png"
        self.texture = arcade.load_texture(self.img)

    def fire(self):
        """  set the laser velocity = ship velocity + ship angle * them by the laser speed. """
        self.velocity.dx = math.cos(math.radians(self.angle)) * LASER_SPEED
        self.velocity.dy = math.sin(math.radians(self.angle)) * LASER_SPEED

    def die(self):
        if self.life >= LASER_LIFE:
            self.alive = False


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
        self.create_rock()

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: draw each object
        self.ship.draw()

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

        # TODO: Tell everything to advance or move forward one frame (step in time)
        for rock in self.rocks:
            pass
            rock.rotate()
        for laser in self.lasers:
            laser.life += 1

        # TODO: Check for collisions

        self.check_collisions()
        
        for rock in self.rocks:
            rock.advance()

    def create_rock(self):
        """
        Creates initial large rocks and adds them to the list.
        :return:
        """

        for rock in range(0, INITIAL_ROCK_COUNT):
            big_rock = Rock_big()
            self.rocks.append(big_rock)

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
                    """  sqrt((x1-x2)**2 + (y1-y2)**2)  """
                    if math.sqrt((laser.center.x - rock.center.x) ** 2 + (laser.center.y - rock.center.y) ** 2) < too_close:
                        # its a hit!
                        laser.alive = False
                        rock.hit()
                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.bury_the_dead()

    def bury_the_dead(self):
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

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.turn_left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.turn_right()

        if arcade.key.UP in self.held_keys:
            self.ship.accelerate()

        if arcade.key.DOWN in self.held_keys:
            pass

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()