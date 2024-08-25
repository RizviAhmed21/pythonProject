# For loops ======

monday_temperature= [9.1, 8.8, 7.5]

for temperature in monday_temperature:
    print(round(temperature))

#another example for loops

for letter in 'hello':
    print(letter.title())


# EX no 1

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for items in colors:
    if isinstance(items, int) and items > 50:
        print(items)

# A for loop can also be used to execute a function multiple times. For example, below we are executing celsius_to_kelvin three times since there are three items in the iterating list:
def celsius_to_kelvin(cels):
    return cels + 273.15


for temperature in [9.1, 8.8, -270.15]:
    print(celsius_to_kelvin(temperature))

# The output of that would be:

282.25
281.95
3.0

# So, in the first iteration celsius_to_kelvin(9.1) was executed, in the second celsius_to_kelvin(8.8) and in the third celsius_to_kelvin(-270.15).

# 61. Looping Through a Dictionary =====

student_grades = { "Rizvi": 32, "Motin": 33, "Rifat": 33}

for grades in student_grades.items():
    # // keys, values instent items
    print(grades)


# Here is an example that combines a dictionary loop with string formatting. The loop iterates over the dictionary and it generates and prints out a string in each iteration:

phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}

for pair in phone_numbers.items():
    print(f"{pair[0]} has as phone number {pair[1]}")

# And here is a better way to achieve the same results by iterating over keys and values:

phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}

for key, value in phone_numbers.items():
    print(f"{key} has as phone number {value}")

# In both cases, the output is:
# John has as phone number +37682929928
# Marry has as phone number +423998200919

#EX Loop Over Dictionary and Replace

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
    print(value.replace("+", "00"))


# 63 While loops ======

 a = 3

while a > 0
    print(1)
    print(2)

# 64. While Loop Example with User Input

username = ''

while username != "pypy":
    username = input("Enter Username:")

# 65. While Loops with Break and Continue

while True:
    uername = input("Enter username: ")
    if username == 'pypy':
        break
    else:
        continue