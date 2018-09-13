import math     # we need to include the math library like so
# Lets print something
print("Hello World")
# Just as simple as that
# we can declare some variables
name = "Wladymir"
age = 21     # notice we don't need variable types
# Lets print them
print("My name is: " + name)
print("I am: " + age + "years")   # this is incorrect
# We need to parse the numeric type
print("I am: " + str(age) + "years")
# lets get some input from the user
num1 = input("Enter a number")
num2 = input("Enter another number")
# lets add them together
print(num1+num2)    # we are adding strings we need to parse them
int_num1 = int(num1)
int_num2 = int(num2)
print(num1+num2)    # now we are adding some integers
# what if we want some decimal values
flo_num1 = float(num1)
flo_num2 = float(num2)
print(flo_num1+flo_num2)
# just as easy we can operate, bare in mind order of operations
print(5+4*8)
# we can alter that order with some parenthesis
print((5+4)*8)
# as we have seen before, we can concat strings using the + operator
print("Something "+"Someone ")

# some more math

# we now can access methods like sin, cos, square root, etc

print(math.sqrt(4))
print(pow(4, 2))    # also we could use the ** operator
print(4**2)
# some trigonometry
print(math.sin(math.pi/6))  # by default the degree unit is on radians but not to worry, we can parse it
print(math.radians(60))     # or the other way around
print(math.degrees(math.pi))
# this are some important functions and we will use them latter on

# now some control statements
# first we define a function, a function is a portion of code that does something


def check_number(n):    # indentation is crucial at this part
    if n > 0:     # So it is very similar to other programing languages
        return "Positive"
    elif n is 0:
        return "Zero"
    else:
        return "Negative"


def print_n_times(n, text):
    for i in range(n):
        print(str(i+1)+"._ "+text)


def text_gather():
    user_input = ""
    while not user_input.isdigit():
        user_input = input("Enter any phrase, to exit any digit ")
        print("You picked: "+user_input)
# to get use to this kind of syntax we will make some lists
# to define an array or a list


friends=["Nicole", "Fred", "Peter"]
ages = [21, 25, 22]
# we can print a list
print(friends)
print(ages)
# we can add the two lists together
friends.extend(ages)    # this alters friends
print(friends)

zipped_friends=list(zip(friends,ages))
print(zipped_friends)

# we can add elements to the list, always at the bottom
friends.append("Maria")
ages.append(20)
# we also can insert something in the middle of the list
friends.insert(1, "Kelly")
ages.insert(1, 20)
# to access a particular element we can reference it with its index
print(friends[0])   # we start the count at 0, from the top
print(friends[-1])  # we start the count from -1 if we need to iterate backwards
# we could also select some portion from the list
print(friends[1:])  # here we get from the 2nd element to the end
print(friends[::-1])  # here we get a shallow copy of the reversed list
# to get the length of our list:
print(len(friends))
# to clear our list
friends.clear()
print(friends)
# to count the occurrences of an element
print(friends.count("Maria"))
# to sort in ascending order our list
friends.sort()
print(friends)
# some stack functions, like pop for example
print(friends.pop())
print(friends)
# we can alter the list in bulk like
friends[1:3]= ["Wladymir", "Miguel"]     # notice that the last index is not included

# tuples are a set of data that its immutable
coord = (3, 4)
print(coord)    # they are used to store data that is not going to change

# we can access each position as in a list
print(coord[0])
print(coord[1])
# we could use a for loop to go through every element into the list


def print_list(p_list):
    for element in p_list:
        print(element)  # in fact this is a for each loop


# now we can define classes, like containers for objects of the same type

# we use the class: reserved word


class Matrix:

    def __init__(self, _items):  # this is the equivalent of a constructor
        self.items = _items

    def __repr__(self):  # ths is the equivalent of ToString() method
        obj = ""
        for column in self.items:
            for item in column:
                obj += str(item) + " "
            obj += "\n"
        return obj


matrix = Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

print(matrix)