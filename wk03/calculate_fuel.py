def switch_func(value, x):
    return {
        'quit': lambda x: x - 0,
        'status': lambda x: x - 0,
        'up': lambda x: x - 5,
        'left': lambda x: x - 5,
        'down': lambda x: x - 5,
        'right': lambda x: x - 5,
        'fire': lambda x: x - 15
    }.get(value)(x)


fuel = 100
# take user input
command_given = input('Enter command : ')

print('Fuel is now : ', switch_func(command_given, fuel))
