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


x = 10
# take user input
command_given = input('Enter command : ')

print('X position is now : ', calculate_x(command_given, x))
