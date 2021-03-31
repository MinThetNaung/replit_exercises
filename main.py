'''All questions are taken from https://www.w3resource.com/python-exercises/python-basic-exercises.php'''

#Q1
'''
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")
'''
#Q2
'''
import sys
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)
'''
#Q3
'''
import datetime
print("Current date and time:")
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
'''
#Q4
'''
radius_input = float(input("r = "))
pi_value     = 3.14
area_value   = (pi_value * (radius_input**2))
print("Area = %.2f" %(area_value))
'''
#Q5
'''
first_name = input("Enter first name: ")
last_name  = input("Enter last name: ")
print("Nice to meet you, " + last_name + " " + first_name + " !")
'''
#Q6
#Continue tomorrow

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)




x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)