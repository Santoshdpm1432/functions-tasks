# Defining a Function:
# To define a function, you use the
# def keyword, followed by the function name and a pair of parentheses. If the
# function takes parameters, you list them within the parentheses. The function
# code is indented below the definition.

# def sant():
#     print("welcome to the world")
# sant()

# Return Statement:

# Definition: The return statement is used to exit a function and return a
# value to the caller.

# def mul(a,b):
#     return a*b
# result = mul(5,5)
# print(result)

# Parameters and Arguments:
# Parameters are variables that are used in a function definition, while
# Functions 2
# arguments are values passed to the function during the function call.
# Parameters receive values from arguments.

# def mul(a,b):
#     return a*b
# print(mul(5,5))

# Default Parameters:

# You can provide default values for parameters, which allows the function to
# be called with fewer arguments. If a value is not provided for a default
# parameter, the default value is used.

# def details():
#     user_name = "santosh"
#     dept = "embeded"
#     print(f"username {user_name} and dept {dept}")
# details()

# def multiply(num_1,num_2): 
#     result = num_1 * num_2 
#     print(result) 
# multiply(10,5)
# multiply(50,5)
# multiply(25,225)

# def area(lenght , width = 12):
#     area = lenght * width
#     print(area)
# area(20,)
# area(20,10)


# arbitary arguments--> function can accept a variable number of arguments by using *args(syntax)

# def myfunc(*a):
#     print(a)
# myfunc("vasu",12,45,65,5.7)

# sample = 1.2,5.7,"santosh","kumar"
# print(sample)

# keyword arguments :-->keyword arguments are passed to a function with a keyword and a value, allowing for more explicit parameter passing

# def sant(**a):
#     print(a)
# sant(a=1,b=2,c=3)

# def add(a,b):
#     return a+b
# obj = add(5,5)
# print(obj*5)


# def sample(a,b,c = 25):
#     # print(a*b*c)
#     return a*b*c
# obj = sample(5,5,)
# print(obj)

# def greet():
#     name = "santosh"  # Local variable
#     print("Hello", name)
#     age = 25
#     print(age)
# greet()

# Variable ---> local variables and global variable
#1. local variable ---> function ( inside the function)

# Global Variable:
# A variable declared outside of all functions and accessible throughout the program, including inside functions, is called a global variable.


# balance = 1000
# def credit(amount):
#     result = amount + 1000
#     print(result)
#     print(amount)
#     print(balance)
# credit(500)
# print(balance)

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def expo(a,b):
#     return a**b
# def pivalue():
#     return 3.14159



# balance = 1000 
# def credit(amount):
#     global balance
#     balance+=amount
#     print(balance)
# credit(1000)
# print(balance)

# Key Points:
#     Local variables are limited to the function scope.
#     Global variables are accessible throughout the program but can only be modified inside a function if declared as global.

# """

# Modifying a Global Variable Inside a Function
# To modify a global variable within a function, use the global keyword.



# def greet(a=5,b=5): #function definition
#     print(a+b) #function body
#     # return 1
# greet(5,5) #function call
# greet(5) #function call
# greet() #function call

#* --> all tuple
#** --> dict

# local 
#import modulename
# from modulename import *
# functioncall()


# syntax
# import modulename
# import function


#syntax
# modulename.functionname() 
import math
# print(math.add(5,5))
print(math.expo(4,5))

 