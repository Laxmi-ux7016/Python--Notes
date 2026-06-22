#List
# a=12
# b=13
# c=14
# d=15
# e=16
# for creating list you have to use square 
#breackets[]
# l=[12,13,14,15,16]
#1.SPECIAL POWERS 

#1 -HETEROGENOUS NATURE
# MEENS IT CAN STOORE ANY KINDS OF DATA TYPES OF ONCE
#eg
# l=[12,"hello",12.67,True,print()]

# ORDERED
# EVERY ELIMENT IN LIST HAS A DESIGNATED POSITION
# DUPLICATES
# you can store duplicates element inside list.

#2. (MUTABLE NATURE)
# YOU CAN CHANGE ANYTHING INSIDE THE LIST AT ANY POINT OF TIME
#  reading LIST
# you will use indexing
# a= [10,20,30,40,50,] (squre brackets)
# print(a)
# print(a[4],a[-1]) --->(indexing)

# updating a list 
# a=[10,20,30,40,70]
# a[-1]=50
# print(a)

#delete 
# a=[10,20,30,40,50]
# del a[-1]
# print(a)

# a=[10,20,30,40,50]
# del a[:] (slicing)
# print(a)

# create loops on list
# a=[10,20,30,40,50]
# based on values
# for i in a:
#     print(i)

# here you will access all the values i.e 10,20,30..
# based on index
# for i in range (0,5):
#     print(a[i])

# this loop can  access your index aswell  as values and it gives more control over your list
# for i in range (0,len(a)):
#     print(a[i])

# METHOD 
# l=[1,2,3,4]
# l.append(5)#--> (append are new  value to insert  at last )
# print(l)

# l=[]
# for i in range(10,51,10):
#     l.append(i)

# print(l)

# a=[10,20,40,50]

# a.insert(2,30)
# print(a)

# # a= [10,20,30,40]
# saved =a.pop (1)# this will remove via index

# a.revomved(10)# this will remove via value
# print(a)

# a=[1,2,3,4,5]
# a.sort()

# print(a)

# a=[12,13,18,15,16]

# for i in range(len(a)-1):
#     if a[i]<a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print ("your list is sorted")


