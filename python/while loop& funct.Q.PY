# #Q.1 COUNT THE NUMBER OF DIGIT IN A NUMBER
# n=1234
# count=0
# while n>0:
#     digit =n%10
#     count=count+1#--->(count increase)
#     n=n//10#---(float division)
# print(f"count of digit is{count}")


def count(n):
    n=1234
    count=0 
    while n > 0 :
        digit =n%10
        count=count+1
        n=n//10
print(f"count of digit is{count}") 
count(654)


# # if we use return inside a functions 
# #it will act like a mini variable and untill unless we didnt print the variable the output will not be displayed

#THE SUM OF DIGITS OF A NUMBER    

# n=123
# sum=0
# while n>0:
#    digit=n%10
#    sum =sum+digit
#    n=n//10
#    print(f"sum is{sum}")


# def sum(n):
#         sum=0
#         while n>0:
#             digit =n%10
#             sum=sum+digit 
#             n=n//10
#         return f"sum is {sum}"

# print(sum(123))

# #check a whether a number is armstrong or not

# n=153
# duplicate = n 
# sum = 0
# while n>0:
#   digit=n%10
#   power=digit**3
#   sum=sum+power
#   n=n//10
# if duplicate == sum:
#     print("aremstrong number")
# else:
#   print('not a armstrong number')


# count the number of digit in a  number

# n=1234
# count=0
# while n > 0:
#    digit = n % 10
#    count=count+1
#    n=n//10
#    print(f"count of digit is {count}")
   
#@ function 
def count(n):
   
    count=0
    while n>0:
        digit=n%10
        count=count+1
        n=n//10
    return(f"count of digit is{count}")


print (count(256))

