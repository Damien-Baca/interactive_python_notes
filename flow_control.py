# In Python, conditional code blocks do not require braces. Instead
# Python uses indentation to define what block the conditional
# applies to. The pep8 style guide specifies that 4 white spaces
# of indentation is preferred here.

# If Statements
# If statements can be in-lined if the conditional expression is
# also a one-liner as seen below.

# Conditional If Statements
print('\n- 1 ----------------------------------\n')
temperature = 35
if temperature > 30:
    print("It's Warm")
    print("Drink Water")
elif temperature < 10:
    print("It's Too Cold")
    print("Don't Drink Water")
else:
    print("It's Room Temperature")
print("Done")

print('\n- 2 ----------------------------------\n')
# In-Line Conditional If Statements
age = 22
# Cumbersome Implementation
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
# One-Line Readable Implementation
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

print('\n- 3 ----------------------------------\n')
# Comparing Strings w/ '>' and '<'
# bag is greater than apple because alphabetically bag is below apple.
# bag is not greater than cat because alphabetically cat is below bag.
if "bag" > "apple" and not "bag" > "cat":
    print("Eligible")

# Values Are Also Expressions
eligible = True  # Could be any Truthy or Falsy value.
if eligible:
    print("Eligible")

print('\n- 4 ----------------------------------\n')
# Expressions Only Evaluated When Necessary
first = False
second = True
third = True
# Only `first` is evaluated since the expressions value is already determined.
if first and second and third:
    pass

# `first`, `second`, and `third` are all evaluated here because they must be.
if first or second and third:
    pass

# Range Conditional Expressions
if 18 <= age < 65:
    print('Eligible')


# Loops
# `range` is a common function to use with for loops because it can
# generate an array that we can iterate over. The first two parameters
# specify the range as a `[closed, open)` interval. Meaning the start
# point is included and the end point is not.

# The range Function
print('\n- 5 ----------------------------------\n')
rng_1 = range(3)  # [ 0, 1, 2 ]
for number in rng_1:
    print('Attempt', number)  # Attempt 0  Attempt 1  Attempt 2

rng_2 = range(1, 4)  # [ 1, 2, 3 ]
for number in rng_2:
    print('Attempt', number)  # Attempt 1  Attempt 2  Attempt 3

rng_3 = range(1, 5, 2)  # [ 1, 3 ]
for number in rng_3:
    print('Attempt', number)  # Attempt 1  Attempt 3


# For Else Loop
print('\n- 6 ----------------------------------\n')
successful = False
for number in range(3):
    print('Attempt')
    if successful:
        print('Successful')
        break
else:
    print('Attempted three times and failed')


# Iterables
print('\n- 7 ----------------------------------\n')
rng_1 = range(1, 5, 2)
print(type(rng_1))  # <class 'range'>
for i in rng_1:
    print("Range", i)
print()

rng_2 = [1, 2, 3, 4]
print(type(rng_2))        # <class 'list'>
for i in rng_2:
    print("List", i)
print()

rng_3 = '1234'
print(type(rng_3))  # <class 'str'>
for i in rng_3:
    print("String", i)
print()

# Custom objects can also be made iterable
# for i in shopping_cart:
#     print(i)


# While Loops
print('\n- 8 ----------------------------------\n')
number = 1000
while number > 0:
    print(number)
    number //= 2  # Integer divide by 2 and assign to number

# A simple idea of how the python interpreters while loop works
# print('\n- 8A ---------------------------------\n')
# command = ""
# while command.lower() != "quit":
#     command = input("> ")
#     print("ECHO", command)

# Infinite Loops
# print('\n- 8B ----------------------------------\n')
# while True:
#     command = input('> ')
#     print("ECHO", command)
#     if command.lower() == 'quit':
#         break


# Match Statements
# Match statements are much like switch case statements from C++,
# matching a data point to a number of patterns. Only the first pattern
# gets matched.

# You can also combine several patterns with '|'
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 100 | 200 | 300:
            return "You're in trouble"
        case _:  # _ acts as a wildcard that matches anything
            return "Somethings wrong I think"


# Patterns can also be used to bind variables, looking like unpacking
# assignments.
print('\n- 9 ----------------------------------\n')
point = (10, 12)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f'Y={y}')
    case (x, 0):
        print(f'X={x}')
    case (x, y):
        print(f'X={x} Y={y}')
    case _:
        raise ValueError("Not a point")


# This can also be done if instead of a tuple you have a class
class Point_1:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point_1(x=0, y=0):
            print("Origin")
        case Point_1(x=0, y=y):
            print(f'Y={y}')
        case Point_1(x=x, y=0):
            print(f'X={x}')
        case Point_1(x=x, y=y):
            print(f'X={x} Y={y}')
        case _:
            raise ValueError("Not a point")


print('\n- 10 ---------------------------------\n')
a = Point_1(10, 12)
where_is(a)


# You can use the __match_args__ attribute in your classes to define
# a specific position and name for attributes in patterns.

# For example, the following patterns are all equivalent assuming we
# we have set __match_args__ to ('x','y')
# Point(1, var)
# Point(1, y=var)
# Point(x=1, y=var)
# Point(y=var, x=1)

# We can also add an if clause to a pattern known as a guard.
class Point_2:
    __match_args__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


print('\n- 11 ---------------------------------\n')
a = Point_2(10, 12)
points = [a]
match points:
    case []:
        print("No points")
    case [Point_2(0, 0)]:
        print("The origin")
    case [Point_2(x, y)] if x == y:  # Pattern Guard
        print(f"Y=X at {x}")
    case [Point_2(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point_2(0, y1), Point_2(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
