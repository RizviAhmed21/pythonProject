def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return  the_mean

print(mean([1,4,5]))

# Currency Converter Function
def convert(amount):
    output = amount * 1.75
    return output


print(convert(10))


def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

student_grades= {"Rizvi": 3.1, "Motin": 6.5, "Rifat": 7.5}
print(mean(student_grades))


# if else condition ========

>>> if 3 > 1:
...     print("greater")
... else:
...     print("Not greater")
...
greater
>>> 3>1
True
>>> if True:
...     print ("greater")
... else:
...     print ("Not greater")
...
greater
>>> type(4) == int
True
>>> isinstance(3, int)
True
>>>

##Boolean Operators "and" and "or"

##So far, you learned how to check for one single condition:
    x = 1

    if x == 1:
        print("Yes")
    else:
        print("No")

##You can also check if two conditions are met at the same time using an and operator:

x = 1
y = 1

if x == 1 and y == 1:
    print("Yes")
else:
    print("No")
##That will return Yes since x == 1 and y ==1 are both True.

##You can also check if one of two conditions are met using an or operator:

x = 1
y = 1

if x == 1 or y == 2:
    print("Yes")
else:
    print("No")

##That will return Yes since at least one of the conditions is True. In this case x == 1 is True.

# elif operation =======

>>> x =3
>>> y = 1
>>> if x > y:
...     print(" x is greater than y")
... elif x == y:
...     print ("x is equal to y")
...
 x is greater than y
>>>

# Functions and Conditionals ======

Define functions:

def cube_volume(a):
    return a * a * a


# Write if - else conditionals:

message = "hello there"

if "hello" in message:
    print("hi")
else:
    print("I don't understand")

# Write if - elif - else conditionals:

message = "hello there"

if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")

# Use the and operator to check if both conditions  are True at the same time:

x = 1
y = 1

if x == 1 and y == 1:
    print("Yes")
else:
    print("No")

# Use the or operator to check if at least one condition is True:

x = 1
y = 2

if x == 1 or y == 2:
    print("Yes")
else:
    print("No")

# Check if a value is of a particular type with isinstance:

    isinstance("abc", str)
    isinstance([1, 2, 3], list)

or directly:

    type("abc") == str
    type([1, 2, 3]) == lst