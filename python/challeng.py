#INPUT AND OUTPUT
# Q.8 Ask the user to enter their favourite food and print: I love eating [food].
# Fav_food=input("Enter your favourite food:-")
# print(f"I Love eating,{Fav_food}")

# ARITHMETIC OPERATORS

# Ask the user to enter two numbers and print all operations (sum, difference, product, division)
# a=int(input("Enter your first number:-"))
# b=int(input("Enter your second number:-"))
# print(f"The sum of {a} and {b} is  = {a+b}")
# print(f"The difference of {a} and {b} is  = {a-b}")
# print(f"The product of {a} and {b} is  = {a*b}")
# print(f"The division of {a} and {b} is  = {a/b}")

# 1️⃣ Arithmetic Operators (Maths)

# Used for calculations.

# +  Addition        5+2  → 7
# -  Subtraction     5-2  → 3
# *  Multiplication  5*2  → 10
# /  Division        5/2  → 2.5
# // Floor Division  5//2 → 2
# %  Modulus         5%2  → 1
# ** Power           2**3 → 8


# 2️⃣ Comparison Operators (True / False)

# Used in conditions.

# ==  Equal          5==5  → True
# !=  Not equal      5!=3  → True
# >   Greater        5>2   → True
# <   Smaller        5<2   → False
# >=  Greater equal  5>=5  → True
# <=  Smaller equal  3<=5  → True

# 3️⃣ Assignment Operators (Value Update)
# =   x=5
# +=  x+=2   → x=x+2
# -=  x-=2   → x=x-2
# *=  x*=2   → x=x*2
# /=  x/=2   → x=x/2
# %=  x%=2   → x=x%2
# **= x**=2  → x=x**2
# Example:
# x=5
# x+=3
# print(x)   # 8

# 4️⃣ Logical Operators (Conditions Combine)
# and   Both True     True and False → False
# or    One True      True or False  → True
# not   Reverse       not True → False

#example:
# True  and True  → True
# True  and False → False
# False and True  → False
# False and False → False

# True  or True  → True
# True  or False → True
# False or True  → True
# False or False → False

#Practice Sheet – Strings (Indexing & Slicing)

# 1. Ask the user to enter a string and print its first character
# n=str(input("enter your string:-"))
# print(n[0])
# 9. Ask the user to enter a string and print characters from index 2 to end
# a=str(input("Enter your string:-"))
# print(a[2:])

# 3. Ask the user to enter a string and print the second character
# n=str(input("enter your string:-"))
# print(n[1])

# Practice Sheet – Control Statements (Medium Level)

# 1. Ask the user to enter a number and check if it is even or odd.
# n=int(input("please tell your number:-"))
# if n % 2 == 0 and n % 2 !=0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

#  Ask the user to enter a number and print reverse of number
# n=int(input("enter your number:-"))
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
#     print("Reverse=",rev)




    
# for loops questio
# 11 may 2026
# n=int(input("please tell your number:-"))
# sum=0
# for i in range(1,n+1,1):
#     print(sum)

2.
# n=int(input("please tell your number:-"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     print(fact)
# Q.3 
# n=int(input("pleease tell your number:-"))
# even=0
# for i in range(1,n+1):
#      if i%2 == 0:
#        print(i)

# Ask the user to enter a number and print all odd numbers up to that number.
# n=int(input("please tell your number:--"))
# odd=0
# for i in range(1,n+1):
#     if i % 2 !=0:
#         print(i)

# Ask the user to enter a number and print numbers divisible by 5 up to that number.
# n=int(input("please enter your number:--"))
# for i in range(1,n+1):
#     if i % 5 ==0:
#         print(i)

# Ask the user to enter a number and print the sum of even numbers up to that number
# n=int(input("please tell your number:--"))
# sum=0
# for i in range(1,n+1):
#     if i % 2 ==0:
#         sum=sum+i
#         print(sum)

# Ask the user to enter a number and print the product of numbers from 1 to n.
# n=int(input("please tell your number:--"))
# product=1
# for i in range(1,n+1):
#     product = product * i
    # print("product=",product)-------product(1 × 2 × 3 × 4 × 5 = 120)

#  Ask the user to enter a number and print squares of numbers from 1 to n
# n=int (input("please tell your number:-"))
# for i in range (1,n+1):
#     print(i*i)

#  Ask the user to enter a number and print sum of odd numbers up to n
# n=int(input("enter your number:--"))
# sum=0
# for i in range(1,n+1):
#     if i % 2 !=0:
#         sum=sum+i
#         print(sum)

# 10. Ask the user to enter a number and print reverse of that number using loop.     
# n = int(input("Enter your number: "))
# rev = 0

# while n > 0:
#     digit = n % 10      # last digit nikalna
#     rev = rev * 10 + digit
#     n = n // 10         # last digit hata dena

# print("Reverse =", rev)     


# 1. Ask the user to enter a number and print all prime numbers up to that numbe

# n=int(input("entr your number:-"))
# num=2
# while num<=n:
#     i=2
# prime=1

# while i<num:
#     if num%i==0:
#         prime =0
#     i=i+1

# if prime ==1:
#     print (num)
# num=num+1# (douts)

# 2. Ask the user to enter a number and check if it is Armstrong number.

# n=int(input("enter your number-:"))
# duplicate=n
# sum=0
# while n>0:
#     digit=n%10
#     power =digit **3
#     sum=sum+power
#     n=n//10
# if duplicate==sum:
#         print("Armstrong number")
# else:
#         print("Not a armstrong number")
    
# 3. Ask the user to enter a number and print the sum of digits using loop.
n=int(input("enter your number:-"))
sum=0
while n>0:
    digit =n%10
    sum=sum+digit
    n=n//10
print("sum of digits is :",sum)

































#FUNCTIONS
# 1. Write a function to check if a number is prime or not
# def is_prime(n):
#     if n<=1:
#         print("not a prime number")
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 print("not a prime number")
#                 break
#         else:
#             print("prime number")

# 2. Write a function to return sum of all numbers from 1 to n.
# def sum_n(n):
#         toatal=0
#         for i in range(1,n+1):
#             total=toatal+i
#         return total

# n=int(input("enter your number:-"))
# print("Sum =", sum_n(n))

#3 3. Write a function to count vowels in a string
# def vowel_count(text):
#     vowel="aeiouAEIOU"
#     total=0
#     for ch in text:
#         if chr is vowel:

#             count+=1

#         return count
    
# n=input("enter your text:-")
# print( "vowel_count=",vowel_count(str))

# 4. Write a function to print Fibonacci series up to n terms.
# def fibonacci(n):
#     a=0
#     b=1
    
#      n=int(input("enter your number:-"))
#         print("fibonacci series=",fibonacci(n))
    
##  **ITERATIVE STATEMENTS**(final sheet)
# 16) Accept an integer and Print hello world n times
# n=int(input("enter your number:-"))
# for i in range(1,n+1):
#     print("Hello World")
# 17) Print natural number up to n.
# n=int(input("enter your number:-"))
# for i in range(1,n+1):
#     print(i)
#18) Reverse for loop. Print n to 1
# n=int(input("enter your number:-"))
# for i in range (n,0,-1):
#     print(i)
# 19) Take a number as input and print its table
#        5 * 1 = 5
#        5 * 2 = 10 up to 10 terms
# n=int(input("Enter your number:-"))
# for i in range(5,55,5):
#     print(i)
# 20) Sum up to n terms.
# n=int(input("enter your number:-"))
# sum=0
# for i in range:
#     sum=sum+i
#     print(i)
# 21) Factorial of a number

# 5. Write a function to find second largest element in a list.(douts)
# l=[1,16,17,23,2,45,89]

# 6. Write a function to remove duplicate elements from a list.

# def remove_duplicates(lst):
#     unique_list = []
    
#     for item in lst:
#         if item not in unique_list:
#             unique_list.append(item)
            
#     return unique_list


# # Example usage
# numbers = [1, 2, 2, 3, 4, 4, 5]
# result = remove_duplicates(numbers)

# print("Original list:", numbers)
# print("List without duplicates:", result)

# # 7. Write a function to check whether a number is Armstrong or not.
# def is_armstrong(num):
#     # convert number to string to count digits
#     digits = str(num)
#     power = len(digits)
    
#     total = 0
#     for digit in digits:
#         total += int(digit) ** power
    
#     # check condition
#     if total == num:
#         return True
#     else:
#         return False


# # Example usage
# n = int(input("Enter number: "))

# if is_armstrong(n):
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")
# #  Write a function to find common elements between two lists.
# def common_elements(list1, list2):
#     common = []
    
#     for item in list1:
#         if item in list2 and item not in common:
#             common.append(item)
    
#     return common

# # Example usage
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# result = common_elements(list1, list2)

# print("Common elements:", result)


