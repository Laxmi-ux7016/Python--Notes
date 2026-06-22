## fuctions 
# 13 APRIL 2026
# USER DEFINED FUNCTIONS

# FUNCTION
# PARAMETER ( THE THING YOU ACCEPT ARE PARAMETER)
#ARGUMENT ( THE THING YIU PROVIDE  TO PAEAMETERS  IS ARGUMENT
# def hello(a,b):
#     print("this is my computer{a+b}")
# hello(12,34)

# ARGUMENT are mainly two types
# 1. positional arguments
# 2. default value arguments 

# POSITIONAL ARGUMENTS
# def hello (name,age):
#     print(f"your name is {name}  and your age is {age}")
# hello("akarsh",24)

#KEYWORDS ARGUMENTS
# def hello(name, age):
#     print(f"your name is {name}  and your age is {age}")
# hello(age=24,name="akarsh")

# DEFAULT arguments
# def sum (a,b=5):
#     print(f"the sum is {a+b}")
# sum(12,2)

# def greeting():
#     print("hello good morning")

# greeting() #-->calling a functions

# parameters and argumebnts

# def addition (a,b):#--> a and b are a parameters
#     print(a+b)
# addition(10,20)

# def palindrome (n):
#     rev =0
#     copy=n
#     while n!=0:
#         rev=rev *10 +n%10
#         n=n //10

#     if   copy == rev :
#        print("palindrome")
#     else:
#        print("not a palindrome")

# palindrome(121)
# palindrome(134)
# palindrome(198891)
# palindrome(451)

# ARGUMENTS TYPES
#1 positional arguments

# def  multiply(a,b):
#     print(a,b)

# multiply (12,67)# fixed arguments

# #2nd default arguments keyword arguments
  
# def info (a,b,c,d,e):
#     print(a,b,c,d,e)

# info (12,34,e=67,c=12,d=67)
# if you give a value using default arguments you always
#have to give further value using default arguments

# defaults parameters

# def info (name,age,id=None):
#     print("info recived")

# info ("akarsh ",24) 

# def palindrome (st):
#     rev=""
#     for i in range (len (str)-1,-1,-1):
#         rev =rev+st[i]

#         if rev ==st:
#             print(f"{st}is a palindrome")
#         else:
#             print(f"{st}is not a palindrome")
#     palindrome("NAMAN")
#     palindrome("CURSOR")

# 15 may 2026
# How can you create  a function that can add up to two numbwers
# def add (a,b):# yaha a,b  patameter hai
#     print(a+b)
# add (10,20)

# problems is what if hume hi nahi pata ki kitne parameters hone wale hai 
# solution-->using args
# args ->*variables (*strcks)
# variable_name-->
# args value ko accept karte hai as a tuple

# def args(*a):
#     print(type(a))
#     print(a)
# args(1,2,3,4,5)

# def  add (*a):-->
#     for i in a
#         print(i)
# add (1,2,3,4,5)

def polio (name ,age ,pin,contact):
    print(name,age ,pin,contact)
# polio(name="Ramseh",age=12,pin=123456,contact=9876543210) --> keyword arguments

#  args* must be used when we are not sure about the number of arguments that will be passed to a function
# Kwargs->keyword arguments (denoted by **variable_name)
# kwarge -> it accept the value as a dictionary
# parameters->keys
# argument woh hai --> value

def polio (**variables):
#     print(type(variables))
    print(variables)
polio(name="suresh",age=12,pin=123456,contact=9876543210,school="abc school")

# def polio(**a):
#     for  i in a:
#         print(f"parameter is {i} and argument is {a[i]}")
#         #i->dict keys,a[i]-> unn keys ki values


# LAMDA FUNCTION 
# lambda function ->jab hume ek line ka function banana hota hai tab hum lambda function ka use karte hai| jab ek function 
# ek line me aa jaye tab hum lambda function ka use karte hai
# lamda --> keyword ek variable ko convert kiya function me
# a,b :a+b ->agar a and b  variable  me kuch value aayegi toh a+b  chalega varna  nahi chalega 

# add =lambda a,b: a+b
# print(add(12,34))