# rent=3200
# wifi=200
# food=3500
# homemade=650
# electric=300
# print(rent)
#
# total=rent+wifi+food+homemade+electric
# print("My overall expence:",total)
#
# ===================
#
# spend =3
# donated= 4
#
# total_amount= spend + donated
#
# print(total_amount)
#
# ===========================
#
# items= 10
# price= 2
#
# total_price= items * price
#
# print(total_price)
#
# ========================
#
# items = 10
# price = 2
#
# total_price = items * price
#
# Below we print out three variables
# print(total_price, items, price)
#
#
# Simple Types: Integers, Strings, and Floats
#
# x = 10
# y = "10"
# z = 10.1
#
# sum1 = x + y
# sum2 = y + y
#
# print(sum1, sum2)
# print(type(x), type(y), type(z))
#
# list & Ranges ==========////////
#
# student_grades= [9.1, 8.8, 7.5]
#
# student_grades = [9, "hello", 1, 2, 4.33]  # Corrected code
# print(student_grades)  # Print the list contents
#
# student_grades = list (range(0, 11))  # range
#
# print(student_grades)  # Print the range contents
#


#21 How to Find Out What Code You Need dir(list) =======

# student_grades= [9,.1, 2.2, 7.5]
#
# mysum= sum(student_grades)
# length= len(student_grades)
#
# mean= mysum/length
# print(mean)

# 22. Dictionary Type {} ========

# monday_temperatures= [9,.1, 2.2, 7.5]
# student_grades={"Harry":3.1, "chill":20}
#
# mysum= sum(student_grades.values())
# length= len(student_grades)
#
# mean= mysum/length
# print(mean)


# 25. Tuples ===========
monday_temperatures= [9,.1, 2.2, 7.5]
monday_temparature2=[1,3,5]
monday_temparature2.append(7)
print(monday_temparature2)

# 26. How to Use Datatypes in the Real World?========

# Integers are used to represent whole numbers:

rank = 10
eggs = 12
people = 3

# Floats represent decimal numbers:

temperature = 10.2
rainfall = 5.98
elevation = 1031.88

# Strings represent text:

message = "Welcome to our online shop!"
name = "John"
serial = "R001991981SW"

# Lists represent arrays of values that may change during the course of the program:

members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]

# Dictionaries represent pairs of keys and values:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}

# Keys of a dictionary can be extracted with:
phone_numbers.keys()

# Values of a dictionary can be extracted with:
phone_numbers.values()

# Tuples represent arrays of values that are not to be changed during the course of the program:

vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# You can get a list of attributes of a data type has using:

dir(str)
dir(list)
dir(dict)

# You can get a list of Python builtin functions using:

dir(__builtins__)

# You can get the documentation of a Python data type using:

help(str)
help(str.replace)
help(dict.values)


