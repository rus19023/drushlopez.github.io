numbers = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]
print('print numbers list')
print(numbers)

print()
print('1 - insert 5 to front of numbers')
numbers.insert(0, 5)
print(numbers)

print()
print('2 - remove 2348 from numbers')
numbers.remove(2348)
#numbers.pop(numbers.index(2348))
print(numbers)

print()
print('3 - extend new list into numbers')
more_numbers = [55, 91, 0, 34, 22]
numbers.extend(more_numbers)
print(numbers)

print()
print('4 -built in sort numbers')
list.sort(numbers)
print(numbers)

print()
print('5 - reverse sort numbers')
numbers.reverse()
print(numbers)

print()
print('6 - built in count number of 12 in numbers')
twelve = numbers.count(12)
print(twelve)

print()
print('7 - built in find index of 96 in numbers')
nine_six = numbers.index(96)
print(nine_six)


print()
print('8 - slice list in 2 halves, make sure no dupes nor left out')
mid = int(len(numbers) / 2)
print(mid)
first_half = numbers[0:mid]
print(first_half)
last_half = numbers[mid:len(numbers)]
print(last_half)
full_list = first_half
full_list.extend(last_half)
if full_list == numbers: 
    print ("The lists are identical") 
else : 
    print ("The lists are not identical") 
    print(full_list)
    print(numbers)

numbers = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]
print()
print('9 - get every other number from numbers by slicing')
eo = numbers[::2]
print(eo)

print()
print('10 - get last 5 items from numbers using slicing with negative indexes')
last5 = numbers[-5:]
print(last5)
