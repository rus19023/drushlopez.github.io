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


y = 10
# take user input
command_given = input('Enter command : ')

print('Y position is now : ', calculate_y(command_given, y))
