

class Robot:
    """ Class for working with a robot. """

    def __init__(self, x=10, y=10, fuel=100):
        ''' initialize Robot class '''
        self.x = x
        self.y = y
        self.fuel = fuel

    def left(self):
        self.fuel -= 5
        self.x -= 1

    def right(self):
        self.fuel -= 5
        self.x += 1

    def up(self):
        self.fuel -= 5
        self.y -= 1

    def down(self):
        self.fuel -= 5
        self.y += 1

    def fire(self):
        if self.fuel >= 15:
            print("Pew! Pew!")
            self.fuel -= 15

    def status(self):
        print("({}, {}) - Fuel: {}".format(self.x, self.y, self.fuel))

    def quit(self):
        print('Goodbye.')

    def prompt_command(self):
        ''' ask user for a command '''
        command = input("Enter command: ")
        return command

    def run_command(self):
        ''' run the command chosen by user '''
        command = self.prompt_command()
        command = command.lower()
        while self.fuel >= 0:
            if command == 'quit':
                ''' exit the program '''
                self.quit()
                break
            elif command == 'status':
                ''' display status of robot '''
                self.status()
            else:
                if self.fuel >= 5:
                    if command == 'up':
                        ''' robot moves up 1 space '''
                        self.up()
                    elif command == 'down':
                        ''' robot moves down 1 space '''
                        self.down()
                    elif command == 'left':
                        ''' robot moves left 1 space '''
                        self.left()
                    elif command == 'right':
                        ''' robot moves right 1 space '''
                        self.right()
                    elif command == 'fire':
                        ''' robot fires laser '''
                        if self.fuel >= 15:
                            self.fire()
                        else:
                            print('Insufficient fuel to perform action')
                else:
                    print('Insufficient fuel to perform action')
            command = self.prompt_command()


def main():
    rowdy = Robot()
    ''' set up the robot instance '''
    rowdy.run_command()
    '''make robot go to work '''


if __name__ == "__main__":
    main()
