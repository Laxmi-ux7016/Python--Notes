# FOR LOOP QUESTION
# Q.1 Print numbers from 1-50
# for i in range(1,51):
#     print(i)
# Q.2 Print square of numbers from 1-10
# for i in range(1,11):
#     print(i)
#Q.3 Print numbers from 1 to 20 using for loops and range()
# for i in range(1,21,1):
#     print(i)
# Q.4 Print all even number from 1 to 50
# for i in range(1,51,1):
#     print(i)
# # Q.5 Print the  table of 7 using loop and range 
# for i in range(7,71,7):
#     print(i)
# Q.6 PRINT numbers from 10 to 1
# for i in range (10,0,-1):
#     print(i)
#Q.7( Factorial ) using  only for loop find the factorial of a number (taken n=6)
# n=int(input("which number factorial you want:"))
# fact =1
# for i in range (1,n+1,1):
#     fact =fact*i
#     print(fact)
#Q.8 Reverse number logic (no string )
# num=12345
# rev=0
# for i in range(len(str(num))):
#     rev=rev*10+num%10#(%)---> remainder i.e (2%10=0)
#     num=num//10#(//) floor division i.e(5/2=2.5)

#     print(rev)
# WHILE LOOP QUESTION
#Q.1 PRINT NUMBERS FROM 10 TO 1 USING WHILE LOOP.
# self practice
# 25 April 2026
# print number from 1 to 5 each numbers repeated 3
# for i in range (1,6,1):
#     print(str(i)*3)
# Q.  PRINT PYTH0ON  5 TIME IN ONE LINE
# for i in range(5):
#     print("python")
#OR
# def twosum(self,nums:list[int],target:int)->list[int]:
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if (nums[i]+nums[j]==target):
#         
#         [i,j]

## INput and output questions

#  Q.1 ASK THE USER TO EITHER THEIR NAME AND PRINT WELCOME[NAME]
# n= int (input("enter your age"))
# print ("you are 18 year old !")

# FINAL SHEET

# Q.1  Display three string "name""is ,""james" as name is james
# a= str(input("Enter your name"))
# print("Name is james")

# Q.2 DISPLAY FLOAT NUMBER WITH 2 DECIMAL PLACE USING PRINT()
# n=float(input("enter your number"))
# print(f"formated number{n:2f}")

# Q.3 SUM OF TWO INTEGERS
# a=int(input("enter your first number"))
# b= int(input("enter your second number"))
# print(f"sum of {a} and {b} is {a+b}")

# Q.4 ACCEPT TWO INTEGER FROM USER AND PRINT THE SUM

# a= int(input("enter your first number"))
# b=int(input("enter your second number"))
# print(f"The sum of {a} & {b}  =  {a+b}")

# Q.5 ACCEPT THE USER NAME ,AGE AND PRINT IN FOLLOWING NUMBER

# n=(input( "enter your user name:- "))
# num=int(input("enter your number:-"))
# print(f"Hello shery you are 12 year old")

## CONDITIONAL STATEMENTS

# 1.Take 3 int inputs from user and check and print the result.

# a= int(input("enter first number:-"))
# b= int(input("enter second  number:-"))
# c=int(input("enter third number:-"))

# if a==b and b==c :
#     print("all are equal")
# elif  a== b  or  b==c or a==c:
#     print("any two are equal")
# else:
#     print ("all are differnt")

# 2. ACCEPT TWO  NUMBERS AND PRINT THE GRATEST BETWEEN THEM 
# a= int (input("enter your  first number:-"))
# b= int(input("enter your second number:-"))
# if a>b:
#     print (" greatest number is",{a})
# else: 
#     print(" greatest number is ",{b} )

#3. Accept the gender from the user as char  and print the respected  greating message.

# gen=input("please tell your gender as char (M  or F)")
# if gen == "M"or gen=="m":
#     print("good morning sir")

# elif gen=="F"or gen=="f":
#     print("good morning maam")
# else:
#     print("unknown gender")

# 4. Extend the previous program and handle the wrong inputs.

# gen= input("please enter your  character:-")
# if gen =="m"and gen=="M":
#     print("Good morning sir")
# elif gen=="F" and gen=="f":
#     print("Good morning maam")
# else:
#     print("wrong input")


# def add (a,b):
#     return  a+b
# print(add(2,3))


# for  i in range (5): 
#  print (i)

