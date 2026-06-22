#  25 APRIL 2026
# for i in range(20):
#     print("sorry")

# print("sorry"*5)

# for i  in range(11):
#     print("hello")
# print("hii"*10)


# n=int(input("enter your name"))
# for i in range(0,n,1):
#     print("hello")
# Q. pint natural number from 1 to 15
# n=int(input("enyer your number"))
# for i in range(1,n+1,1):
#     print(i)
# Q. PRINT A TABLE 5 
# n=int(input("enyer your number"))
# for i in range(5,51,5):
#     print(i)
# Q.
# n=int(input("enyer your number")) 
# for i in range(n,(n*10)+1,n):
#     print(i)

# n=int(input("enter your number"))
# for i in range(1,11,1):
#     print(f"{n}*{i}={n*i}")

# n= int(input("enter your numer"))
# sum=0
# for i in range (1,n+1,1):
#     sum=sum+i 
#     print(i)
# print(sum)
#OR
# n=int(input("enter your number"))
# length=len(str,(n))
# sum=0
# prod= 1
# for i in range (1,length+1):
#     sum=sum+i
#     prod *=1
#     print(i)
#     print(sum)
# print(prod)
# if sum ==prod :
#     print("the number is spy.")
# else:
#     print("spy")

# WHILE LOOP
n=0
# while n>=5:  
#    print(n)

# # Q
# n=int(input("enter your number"))
# sum=0
# prod=1
# temp=0

#9 may 26
#LIST (list is a advance a data types ) 
# list [] (multiple data types are store in list  its called advanced data type)
# 1.int,float ,str)
# list have a duplicate value allow
#** indexing starts with 0 and goes to len-1)
# list have unique thing that is known  is indexing 
# 
# age=[]#empty list
# #   0   1   2
# age=[21,22,23]
# print(age[2])

# l=[1,2,3,4,5,6,7]
# l[3]=10
# print(l)

#slicing
# start_indexing:stop_indexing:step_skip
# step(by_default =+1)

# l=[1,2,3,4,5,6,7]
# print(l[1:4])

#Direct loop
l=[1,2,3,4,5]
# for i in l:
#     print(i)

# index value
# l=[1,2,3,4,5]
# for i in range(len(l)):
#     print(i,l(i))# index ,values

# METHODS
# 1.append() add last value
# 2.extend()  multiple value add at one time
# 3.insert()  
# 4.pop()   last index  delete hoga 
# 5.remove() -- value are delete
# 6.clear()

#1.Append
# l=[1,2,3,4,5]
# l.append(6)

# l=[1,2,3,4,5]
# ll=[6,7,8]
# # print(l+ll)
# l.extend(ll)
# print(l)

# #5 clear()
# l=[1,2,3,4,5]
# l.clear()
# print(l)

#Roatet a list by k elements.
# l=[10,20,30,40,50]
# k=2
# for i in range(k):
#     last=l[len(l)-1]
    
# for j in range (len(l)-1,0,-1):
#     l[j]=l[j-1]
# l[0]=last

# print(l)

#FUNCTION def--(define)
def greet():
    print(f"hello (greet)")
greet()