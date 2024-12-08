print("Hello World")

# Variable

full_name = "John Smith"
age = 20
is_new = True
bill = 525.52

# Input Taking From User

name = input('What is your name? ')
birth_year = int(input('Birth year: '))
weight = float(input("Your Weight In Pound: "))
convert_kilo = 0.45 * weight
print("Your weight is", convert_kilo, "kg")

# String

course = '''
Hello Akg,

Here is our first email to you.

Thank you,
The support team
'''

print(course)

course = 'Python for Beginners'
print(course[0])
print(course[-1])
name = "Hello"
print(name[1:-1])

first_name = 'John'
last_name = 'Smith'
message = first_name + ' [' + last_name + '] is a coder'
msg = f'{first_name} [{last_name}] is a coder'
print(message)
print(msg)

course = 'Python for Beginners'
print(course.upper())
print(course.lower())
print(len(course))
print(course.find('P'))
print(course.replace('P', 'J'))
print('P' in course)


# Arithmetic Operations

print(10/3)
print(10//3)
print(10 % 3)
print(10**3)

import math

print(round(2.9))
print(abs(-5))
print(math.ceil(2.5))

# If Else Condition

price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = price * .1

else:
    down_payment = price * 0.2

print(f'Down Payment: ${down_payment}')

name = input("Enter your name: ")

if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) > 50:
    print('Name can be a maximum of 50 characters')
else:
    print('Name looks good!')


# While Loop

i = 1
while i <= 5:
    print('*' * i)
    i += 1
print('Done')


# For Loop

for item in 'Python':
    print(item)
for item in range(2, 10, 2):
    print(item)

# List

prices = [10, 20, 30]
total_price = 0
for price in prices:
    total_price += price
print(total_price)


# 2D List

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[0][0])
for row in matrix:
    for item in row:
        print(item)


numbers = [1, 278, 3, 4, 5, 5, 6, 7]
numbers.append(20)
numbers.insert(2, 5)
print(numbers)
numbers.remove(5)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(6))
print(50 in numbers)
print(numbers.count(5))
numbers.sort()
numbers.reverse()
print(numbers)
new_numbers = numbers.copy()
new_numbers.append(88)
print(new_numbers)
numbers.clear()
print(numbers)


# Tuples

numbers = (1, 2, 3)
print(numbers[0])

# Unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates
print(x)

# Dictionaries
customers = {
    "name": "John Smith",
    "age": 20,
    "is_verified": True
}

print(customers["name"])
print(customers.get("birth_date", "Jan 1 1980"))
print(customers)
