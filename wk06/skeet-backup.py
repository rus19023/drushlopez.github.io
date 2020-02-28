"""
File: skeet.py
Original Author: Br. Burton
Designed to be completed by others
This program implements an awesome version of skeet.
"""
import arcade
import math
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15


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
    """ create the flying objects: bullets, clay pigeons, and other targets
         that will be launched into the air """

    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 10
        self.center.x = 10
        self.center.y = random.uniform(SCREEN_HEIGHT // 2, SCREEN_HEIGHT)
        self.velocity.dx = random.uniform(1, 5)
        self.velocity.dy = random.uniform(-2, 5)
        self.color = TARGET_COLOR
        self.alive = True
        self.max_hits = 1

    def draw(self):
        ''' draw projectile using constant and member variables '''
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.color)

    def advance(self):
        ''' projectile moves at the current velocity '''
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def hit(self):
        while self.hits > 0:
            if self.hits == 1:
                score = 1
            elif self.hits == 2:
                score = 1
            elif self.hits == 3:
                score = 5
        return score


    def is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.x > SCREEN_WIDTH or self.x < 0 or self.y > SCREEN_HEIGHT or self.y < 0:
            return True


class Standard(Projectile):
    def __init__(self):
        super().__init__()
        self.radius = TARGET_RADIUS
        self.hits = 1  # 1 hit to destroy target
        self.score = 1


class Strong(Projectile):
    def __init__(self):
        super().__init__()
        self.radius = TARGET_RADIUS
        self.velocity.dx = random.uniform(1, 3)
        self.velocity.dy = random.uniform(-2, 3)
        self.hits = 3  # 3 hits to destroy target
        self.score = 0  # if hits = 1, score +1, if 2, score +1, if 3, score +5

    def draw(self):
        arcade.draw_circle_outline(
            self.center.x, self.center.y, self.radius, TARGET_COLOR)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.lives), text_x, text_y, TARGET_COLOR, font_size=20)


class Safe(Projectile):
    def __init__(self):
        super().__init__()
        self.center = Point()
        self.radius = TARGET_SAFE_RADIUS
        self.hits = 1  # 1 hit destroys target, but it should be avoided
        self.score = -10   # if hit, score -10

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, TARGET_RADIUS, TARGET_RADIUS, TARGET_SAFE_COLOR)


class Bullet(Projectile):
    ''' bullets are shot from the rifle toward the targets'''

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.radius = BULLET_RADIUS
        self.velocity = BULLET_SPEED

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, BULLET_RADIUS, BULLET_COLOR)

    def fire(self, angle):
        self.alive = True
        self.velocity.dx = math.cos(math.radians(self.angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(self.angle)) * BULLET_SPEED


class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """
    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0

        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, self.angle)


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []

        # TODO: Create a list for your targets (similar to the above bullets)
        self.targets = []

        arcade.set_background_color(arcade.color.FAWN)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw()

        # TODO: iterate through your targets and draw them...
        for item in self.targets:
            self.targets.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=14, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()

        # TODO: Iterate through your targets and tell them to advance

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """

        # TODO: Decide what type of target to create and append it to the list

        
    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                                abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score += target.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()
        bullet.fire(angle)

        self.bullets.append(bullet)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
