"""
Starting Template
Once you have learned how to use classes, you can begin your program with this
template.
A walk-through of this code is available at:
https://vimeo.com/168051968
"""
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BALL_RADIUS = 40
BALL_COLOR = arcade.color.RED
BOX_HEIGHT = 50
BOX_WIDTH = 50
BALL_SPEED = 70
BOX_COLOR = arcade.color.BLACK


class MyApplication(arcade.Window):
    """
    Main application class.
    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        self.ball_x_position = BALL_RADIUS
        self.ball_x_pixels_per_second = BALL_SPEED

        arcade.set_background_color(arcade.color.WHITE)

        # Note:
        # You can change how often the animate() method is called by using the
        # set_update_rate() method in the parent class.
        # The default is once every 1/80 of a second.
        # self.set_update_rate(1/80)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Draw the circle
        arcade.draw_circle_filled(self.ball_x_position, SCREEN_HEIGHT // 2,
                                  BALL_RADIUS, BALL_COLOR)

        # Draw the text
        arcade.draw_text("This is a simple template to start your game.",
                         10, SCREEN_HEIGHT // 2, arcade.color.BLACK, 20)

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        # Move the ball
        self.ball_x_position += self.ball_x_pixels_per_second * delta_time

        # Did the ball hit the right side of the screen while moving right?
        if self.ball_x_position > SCREEN_WIDTH - BALL_RADIUS \
                and self.ball_x_pixels_per_second > 0:
            self.ball_x_pixels_per_second *= -1

        # Did the ball hit the left side of the screen while moving left?
        if self.ball_x_position < BALL_RADIUS \
                and self.ball_x_pixels_per_second < 0:
            self.ball_x_pixels_per_second *= -1

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        print(key, key_modifiers)

        # See if the user hit Shift-Space
        # (Key modifiers are in powers of two, so you can detect multiple
        # modifiers by using a bit-wise 'and'.)
        # NOTE: This won't work if you have NUM-LOCK turned on.  Another
        # way to do this is to do a bitwise AND to ignore the NUM-LOCK
        # code (and other codes).  The second condition would be written as:
        # "key_modifiers & arcade.key.MOD_SHIFT == arcade.key.MOD_SHIFT"
        if key == arcade.key.SPACE and key_modifiers == arcade.key.MOD_SHIFT:
            print("You pressed shift-space")

        # See if the user just hit space.
        elif key == arcade.key.SPACE:
            arcade.draw_rectangle_filled(100, 100, 50, 50, arcade.color.BLUE)
            print("You pressed the space bar.")

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.SPACE:
            print("You stopped pressing the space bar.")

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """

        self.ball_x_pixels_per_second = 300
        # self.set_update_rate(1/160)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        self.ball_x_pixels_per_second = 100


window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()
