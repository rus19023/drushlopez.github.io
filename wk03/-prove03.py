''' be sure the user enters a number (integer) - adapted from www.101computing.net '''


def input_number_only(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not a number! Please try again.")
            continue
        else:
            return userInput
            break


evens = []
odds = []
number1 = 999
while number1 != 0:
    number1 = input_number_only("Enter a number (0 to quit): ")
    if number1 == 0:
        break
    number1 = int(number1)
    if number1 % 2 == 0:
        evens.append(number1)
        print(evens)
    else:
        odds.append(number1)
    print(odds)
print('Even numbers: ')
for i in range(len(evens)):
    print(evens[i])
print()
print('Odd numbers:')
for i in range(len(odds)):
    print(odds[i])



