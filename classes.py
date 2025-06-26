from dataclasses import dataclass

# Statements executed by the top-level invocation of the interpreter are considered
# part of the __main__ module. The names of built-in types are in the builtins module.

# A piece of Python code that expects a particular abstract data type can often be passed a
# class that emulates the methods of that data type instead. For instance, if you have a
# function that formats some data from a file object, you can define a class with methods
# read() and readline() that get the data from a string buffer instead, and pass it as an
# argument.

# Python implicitly defines a namespace for each module. This means globally defined
# variables don't pollute a namespace that all imported files share.
BEST_NAME = 'Damien'  # If a file imported this one, this would be `classes.BEST_NAME`


# Used in class Example
def external_function_object(self, x, y):
    return f'Minimum is {min(x, x+y)}'


# Inheriting from `object` is implicit in Python 3, and can be omitted. However, must
# be explicit in python 2 to gain access to the same features that the base object
# class provides.
# Classes can also inherit from base types like Integers.
class Example(object):
    """A simple example class"""
    # Class members are normally all public.

    # All class methods are considered virtual as in C++'s definition.

    # Function Objects and Method Objects
    # Functions in a class have an instance of themselves as the first argument.
    # When instantiated, the function objects are converted to method objects which implicitly
    # add the self argument. For example, the method object of upgrade_name has one argument.
    # However, the function object can still be called by passing self explicitly.
    # Additionally, even function objects defined outside the class will produce method objects
    # if assigned to a class attribute as seen here:
    external_function_object = external_function_object

    # Defined here, worst_name is a class variable which is shared among all instances.
    worst_name = 'Bob'  # Class Variable

    # __init__ is the class constructor.
    def __init__(self, name):
        # Self is an instance object making name_public an instance variable.
        # Instance variables are unique to each instance
        self.name_public = name  # Instance Variable
        if name == Example.worst_name:
            self.name_public = BEST_NAME

    # Like C++, class operators can be overloaded.
    def __add__(self, obj):
        return self.name_public + obj.name_public

    # Objects passed into functions use references.
    # Python refers to this as aliasing. Two variables pointing to the same data.
    def upgrade_name(self, obj):
        obj.name_public = BEST_NAME  # Object used to call this is modified.


print('\n- 1 ----------------------------------\n')
print(Example.__doc__)
ex_damien = Example('Damien')
ex_dan = Example('Dan')

print(ex_damien + ex_dan)  # Calls method object
print(ex_damien.__add__(ex_dan))  # Calls method object

print(Example.__add__(ex_damien, ex_dan))  # Calls function object
print(ex_damien.__add__.__func__(ex_damien, ex_dan))  # Calls function object


print('\n- 2 ----------------------------------\n')
# Function defined outside the class and assigned to class attribute becomes method object
print(ex_damien.external_function_object(5, 10))

# Every object has a class, aka its type, this info is stored in the __class__ attribute.
print(ex_damien.__class__)


# Scopes - nonlocal and global keywords
# This function demonstrates how the `nonlocal` and `global` keywords effect scope.
def scope_test():
    def do_local():
        msg = 'local message'

    def do_nonlocal():
        nonlocal msg
        msg = 'nonlocal message'

    def do_global():
        global msg
        msg = 'global message'

    msg = 'test message'
    do_local()
    print('After local assignment:', msg)  # test message
    do_nonlocal()
    print('After nonlocal assignment:', msg)  # nonlocal message
    do_global()
    print('After global assignment:', msg)  # nonlocal message


print('\n- 3 ----------------------------------\n')
scope_test()
print("In global scope:", msg)  # global message


# Class Variables vs Instance Variables
# Sample class showing some of the effects of class variables vs instance variables
class Dog:
    tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


print('\n- 4 ----------------------------------\n')
Ace = Dog()
Snowball = Dog()
Ace.add_trick('Roll_over')
Snowball.add_trick('Stay')
print(Snowball.tricks)
print(Ace.tricks)

# If an instance var and a class var share names, the instance var is preferred.
Snowball.tricks = ['Stay']
print(Snowball.tricks)


# Inheritance
class Base(object):
    def foo(self):
        print('Base Class - foo')
        self.bar()

    def bar(self):
        print('Base Class - bar')


class Derived(Base):
    def foo(self):
        print('Derived Class - foo')
        Base.foo(self)

    def bar(self):
        print('Derived Class - bar')


print('\n- 5 ----------------------------------\n')
base = Base()
derived = Derived()
derived.foo()
# Derived Class - foo
# Base Class - foo
# Derived Class - bar

# When calling Base.foo(self), self is an instance of the derived class. So when Base.foo calls
# self.bar(), it's actually calling the bar() of the derived class.
print()

print(isinstance(derived, Base))  # True
print(isinstance(derived, Derived))  # True
print()

print(issubclass(type(derived), type(base)))  # True
print(issubclass(type(base), type(derived)))  # False

# Python Has No Private Parts, and Name Mangling
# Python doesn't have private attributes, instead it is convention to add leading underscores to
# attributes that are considered non-public / an implementation detail.


# Additionally if two leading underscores are used then the name is textually replaced.
# '__spam' will become '_classname__spam'
# This is very helpful for letting subclases override methods without breaking method calls.
class Mapping:
    def __init__(self, iterable):
        print('Mapping __init__')
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        print('Mapping update')
        for item in iterable:
            self.items_list.append(item)

    __update = update  # Pseudo-private copy of original update method


class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        print('MappingSubclass update')
        for item in zip(keys, values):
            self.items_list.append(item)


class Error_MappingSubclass(Mapping):
    def _Mapping__update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)


print('\n- 6 ----------------------------------\n')
ms = MappingSubclass([1, 2, 3, 4])
# This next line causes an error though because we have overloaded the mangled name of the
# base classes update method and the overload takes more arguments then the base __init__
# supplied when calling it.
# error = Error_MappingSubclass([1, 2, 3, 4])


# Sometimes it can be useful to bundle data types into a simple struct like class.
# Dataclasses exist for this purpose.
@dataclass
class Student:
    name: str
    major: str
    gpa: float
    address: str


print('\n- 7 ----------------------------------\n')
damien = Student('Damien', 'Computer Science', 4.0, '1234 E Street Ave')
print(f'{damien.name}, {damien.major} ({damien.gpa})')


# Iterators
# When using for loops often times objects are used to iterate through. For example:
print('\n- 8 ----------------------------------\n')
for element in [1, 2]:
    print(element)
for element in (1, 2):
    print(element)
for key in {'one': 1, 'two': 2}:
    print(key)
for char in "12":
    print(char)
for line in open("iterate.txt"):
    print(line, end='')
print()

# Behind the scenes the for loop call iter() on the container object. This object defines the method
# __next__() which access elements one at a time. When there are no more elements, __next__() raises a
# StopIteration exception which tells the for loop to terminate.


# With this said classes can be defined to use this functionality.
class Reverse:
    """Iterator for looping over a sequence backwards"""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


print('\n- 9 ----------------------------------\n')
msg = 'Message'
rev = Reverse(msg)
print(msg, ' -> ', end='')
for char in rev:
    print(char, end='')
print()


# Generators
# Generators are a tool for creating iterators. They are written like normal functions and
# use the yield() statement to return data. Each time next() is called on the generator it
# resumes where it left off.
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
    print()


print('\n- 10 ---------------------------------\n')
print(msg, ' -> ', end='')
for char in reverse(msg):
    print(char, end='')
print()

# Anything that can be done with iterators can be done with generators as well.
# Pros to generators
# - Automatic method creation
# - Automatically raises StopIteration
# - Easier to write and much more clear

# Generator Expressions
# Some simple generators can be coded as expressions similar to list comprehensions. Instead of square
# brackets, generator expressions use parentheses.
print('\n- 11 ---------------------------------\n')
# Dot Product
xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(tuple(zip(xvec, yvec)))
print(sum(x*y for x, y in zip(xvec, yvec)))

# Sum of squares
print(sum(i*i for i in range(10)))

# List Construction
data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))

# Unique Words
print(set(word for line in open("iterate.txt") for word in line.split()))

# Searching Objects
graduates = [damien]
print(max((student.gpa, student.name) for student in graduates))
