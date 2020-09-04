#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = number
if number < 0:
    last = (number * -1) % 10
    last = last * -1
else:
    last = number % 10
if number > 5:
    print('Last digit of', number, 'is', number % 10, 'and is greater than 5')
elif number == 0:
    print('Last digit of', number, 'is', number % 10,  'and is 0')
elif number < 6 and not 0:
    print('Last digit of', number, 'is', last, 'and is less than 6 and not 0')
