

class Robot:
    """ Class for working with a robot. """

    def __init__(self, x=10, y=10, fuel=100):
        ''' initialize Robot class '''
        self.x = x
        self.y = y
        self.fuel = fuel

    def calculate_fuel(value, x):
        return {
            'quit': lambda x: x - 0,
            'status': lambda x: x - 0,
            'up': lambda x: x - 5,
            'left': lambda x: x - 5,
            'down': lambda x: x - 5,
            'right': lambda x: x - 5,
            'fire': lambda x: x - 15
        }.get(value)(x)

    def calculate_y(value, x):
        return {
            'quit': lambda x: x - 0,
            'status': lambda x: x - 0,
            'up': lambda x: x + 1,
            'left': lambda x: x - 0,
            'down': lambda x: x - 1,
            'right': lambda x: x + 0,
            'fire': lambda x: x - 0
        }.get(value)(x)

    def calculate_x(value, x):
        return {
            'quit': lambda x: x - 0,
            'status': lambda x: x - 0,
            'up': lambda x: x - 0,
            'left': lambda x: x - 1,
            'down': lambda x: x - 0,
            'right': lambda x: x + 1,
            'fire': lambda x: x - 0
        }.get(value)(x)

    def prompt_command():
        ''' ask user for a command '''
        command = input("Enter command: ")
        return command

    def run_command(self):
        ''' run the command chosen by user '''
        command = self(prompt_command)
        if self.calculate_fuel > self.fuel:
            if command.lower() == 'quit':
                print('Goodbye')
            if command.lower() == 'status':
                self.display_status()
            if command.lower() == 'fire':
                print("Pew. Pew.")
                self.fuel -= 15
            if command.lower() == 'status':
                print("({},{}) - Fuel: {}".format(self.x, self.y, self.fuel))
        else:
            print('Insufficient fuel to perform action')


def main():
    rowdy = Robot()
    command = rowdy.prompt_command
    fuel_needed = rowdy.calculate_fuel(rowdy.run_command)


if __name__ == "__main__":
    main()
