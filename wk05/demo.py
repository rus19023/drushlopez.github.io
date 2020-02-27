import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
BOX_WIDTH = 50
BOX_HEIGHT = 20
BOX_COLOR = arcade.color.PINK


class Box:
    """
    This class defines the box that moves around the screen.
    """
    def __init__(self):
        self.x = 100
        self.y = 100

        self.dx = 10
        self.dy = 10

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, BOX_WIDTH, BOX_HEIGHT, BOX_COLOR)

    def advance(self):
        if self.x + BOX_WIDTH // 2 > SCREEN_WIDTH:
            self.dx *= -1
        elif self.x - BOX_WIDTH // 2 < 0:
            self.dx *= -1
        self.x += self.dx        
        if self.y + BOX_HEIGHT // 2 > SCREEN_HEIGHT:
            self.dy *= -1
        elif self.y - BOX_HEIGHT // 2 < 0:
            self.dy *= -1
        self.y += self.dy
        


class DemoApp(arcade.Window):
    """
    This class defines the demo application.
    It produces a rectangle on the screen.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.GRAY)
        self.box = Box()

    def on_draw(self):
        """
        called every time we need to draw the window.
        :return:
        """
        arcade.start_render()
        self.box.draw()

    def update(self, delta_time: float):
        """
        The purpose of this method is to move everything forward.
        :param delta_time:
        """
        self.box.advance()


window = DemoApp(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
