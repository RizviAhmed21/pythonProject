
32. Accessing List Slices ======

>>> monday_tempera=[3.1, 2.1, 5.1]
>>> len(monday_temperature)
3
>>> monday_temperature[2]
5.1
>>> monday_temperature [0:2]
[3.1, 2.1]
>>> monday_temperature [0:1]
[3.1]
>>> monday_temperature [0:3]
[3.1, 2.1, 5.1]

#34. Accessing Items and Slices with Negative Indexes =====

>>> monday_tempera=[3.1, 2.1, 5.1]
>>> monday_temperature[-1]
5.1
>>> monday_temperature[-3]
3.1
>>> monday_temperature[-1:]
[5.1]

# 35. Accessing Characters and Slices in Strings ======

>>> mystring= 'hello'
>>> mystring[1]
'e'
>>> mystring[-1]
'o'
>>> mystring[:3]
'hel'
>>> monday_temperature= ['hello', 1 ,2, 3, 4]
>>> monday_temperature[0]
'hello'
>>> monday_temperature[0][2]
'l'


37. Accessing Items in Dictionaries ====

>>> monday_temperature= ['hello', 1 ,2, 3, 4]
>>> monday_temperature[0]
'hello'
>>> monday_temperature[0][2]
'l'
>>> student_mark={"Rizvi":33, "Motin":34, "Rifat":35}
>> student_mark["Rizvi"]
33

Converting Between Datatypes //////////============

From tuple to list:

>>> cool_tuple = (1, 2, 3)
>>> cool_list = list(cool_tuple)
>>> cool_list
[1, 2, 3]


From list to tuple:

>>> cool_list = [1, 2, 3]
>>> cool_tuple = tuple(cool_list)
>>> cool_tuple
(1, 2, 3)


From string to list:

>>> cool_string = "Hello"
>>> cool_list = list(cool_string)
>>> cool_list
['H', 'e', 'l', 'l', 'o']


From list to string:

>>> cool_list = ['H', 'e', 'l', 'l', 'o']
>>> cool_string = str.join("", cool_list)
>>> cool_string
'Hello'

