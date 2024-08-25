
# 53. User Input===========
def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return  "Cold"

user_input = float(input("Enter temperature:"))
print(weather_condition(user_input))

# 54. String Formatting =====

user_input = input("Enter your name: ")
message = "Hello %s " % user_input
message = f"Hello {user_input}"
print(message)

#output
Enter your name: Rizvi
Hello Rizvi

# 55. String Formatting with Multiple Variables

name = input("Enter your name: ")
surname = input("Enter your surname: ")
nickname = input("Enter your nickname: ")
when = "today!"
message = "Hello %s %s %s" % (name, surname, nickname)
message = f"Hello {name} {surname} {nickname}. How was going {when}"
print(message)

# Another formate================================

name = "Rizvi"
surname = "Ahmed"
nickname = "Rumon"

message = "Your name is {}. Your surname is {}.Your nickname is {}".format(name, surname, nickname)
print(message)


# The input function halts the execution of the program and gets text input from the user:
name = input("Enter your name: ")

# The input function converts any input to a string, but you can convert it back to int or float:
experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12

# You can also format strings with:

name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
# output: Hi Sim, you have 1.5 years of experience.
