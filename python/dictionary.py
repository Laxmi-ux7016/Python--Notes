# DICTONARY
#LIST HAS INDEXING ---> []
#DICTIONARY HAS KEYS ---> {}
#YOU CAN HAVE ANY  DATA TYPE IN DICTIONARY
#EG-
# d = {"one":1, "two":2, "three":3}
   #"key" : #value
   
# d1 = {1:10, 2:20, 3:30}
# d2 = {4:40, 5:50, 6:60}
# for i in d1:
#     print(d1[i])
    
#CREATION OF KEY
# d1 = {1:10,2:20,3:30}

# d1[4] = 40
# print(d1)

#UPDATION OF KEY
# d1 = {1:10,2:20,3:30}

# d1[1] = 100
# print(d1)

#DELETION
# d1 = {1:10,2:20,3:30}
# del [d1]
# print(d1)


# d1 = {1:10,2:20,3:30}
# #METHODS
# #fromkey method
# print(dict.fromkeys([1,2,3,4,5],10))


#get method
# d1 = {1:10,2:20,3:30}
# print(d1.get(3))

#item method
# d1 = {1:10,2:20,3:30}
# print(d1.items())

#keys method
# d1 = {1:10,2:20,3:30}
# print(d1.keys())


#pop method
# d1 = {1:10,2:20,3:30}
# print(d1.pop(3))

#popitem method
# d1 = {1:10,2:20,3:30}
# print(d1.)

#setdefault method
# d1 = {1:10,2:20,3:30}
# print(d1.setdefault(3,40))
# print(d1)

#update method
# d1 = {1:10,2:20,3:30}
# d2 = {4:40, 5:50, 6:60}
# d1.update(d2)
# print(d1)

#values method

#UPDATING THE D2 IN D1 WITHOUT USING UPDATE() METHOD
# d1 = {1:10,2:20,3:30}
# d2 = {4:40, 5:50, 6:60}
# for i in d2:
#     d1[i] = d2[i]
    
# print(d1)

#AND 

# d1 = {1:10,2:20,3:30}
# d2 = {3:40, 5:50, 6:60}
# for i in d2:
#     d1[i] = d2[i]
    
# print(d1)



# d1 = {1:10,2:20,3:30}
# d2 = {3:40, 5:50, 6:60}

# for i in d2:
#     if i in d1.keys():
#         d1[i] = d1[i] + d2[i]
#     else:
#         d1[i] = d2[i]
        
# print(d1)
 
#COUNTING 2 
# l = [1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,6,6]

# count = 0

# for i in l:
#     if i == 2:
#         count = count + 1
        
# print(count)
 
#COUNTING ALL THE ELEMENT FROM THE LIST
# l = [1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,6,6]
# d = {}

# for i in l:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1
        
# print(d)

# d={"one":1,"two":2,"three":3}
# print([d])
# d1={1:10,2:20,3:30}
# for i in d1:
#     print(d1[i])
# CREATION OF KEY 
# d1={1:10,2:20,3:30}
# d1[[4]]=40
# print(d1)

# methods 
# fromkey 
# d1.fromkeys()
# print(dict .fromkeys([1,2,3,4,5],10))
# # get key method
# print(d1.get (3))
# # itemkey method 
# d1={}

# # pop method
# print(d1.pop(3))
# #popitem  method
# print(d1)

# # setdefault
# d1={1:10,2:20,3:30}
# d1.setdefault (3,40)
# print(d1)

# d1={1:10,2:20,3:30}
# d2={4:40,5:50,6:60}
# d1.update(d2)
# print(d1)
#question
# d1={1:10,2:20,3:30}
# d2={4:40,5:50,6:60}#4-key,40-- value

# for i in d2:
#     d1[i]=d2[i]
# print(d)
# d1={1:10,2:20,3:30}
# d2={3:40,5:50,6:60}#4-key,40-- value

# for i in d2:   
#     if i in d1.keys():
#         d1[i]=d1[i]+d2[i]
# else:
#     d1[i]=d2[i]
# print(d1)

# 29 april 2026

# l=[1,1,1,2,2,2,3,3,4,4,4,6,6,6,7,7,7,7]
# d={}
# for i in l:
#     if i in d.keys():
#         d[i]=d[i]+1
# else:
#     d[i] =1
# print(f"frequency of element are {d}")
# always accaess are keys 

l=[1,1,2,2,2,3,3,4,4,4,5,5]# DOUTS
# d={}
# for i in l:
#     if i in d.keys():
#         d[i]=d[i]+1

# else:
#     d[i]=1
# print(f"frequency of element are{d}")


# a={1:10,2:20,3:30}
# b={3:40,5:50,6:60}
# for i in b:
#     if i in a.keys():
#         a[i]=a[i]+b[i]
# else:
#     a[i]=b[i]
# print(a)

# a={1:10,2:20,3:30}
# b={2:70,5:50,6:60}
# for i in b:
#     if i in a.keys():
#         a[i]=a[i]*b[i]
# else: 
#     a[i]=b[i]
# print(a)
# 30 april 2026
#Leetcode question
#  Q. 2206
# l=[3,2,3,2,2,2]
# d={}

# for i in l:
#     if i in d:
#      d[i]+=1
#     else:
#       d[i] =1
# for i in d.values():
#  if i%2!=0:
#   print(" not pair")
# else:
#  print( "pair")

# l=[3,2,3,5,2,]
# d={}
# for i in l:
#   if i%2==0:
#     print("Pair")
# else:
#   ("not pair")
# print("pair")


# Q.2341
#  d ={}
# for i in l:
#     if i in d:
#             d[i]+= 1
# else:
#             d[i]=1
# paairs=0
# lefovers=0
# for i  in d.values():
#         pairs =pairs+i//2# to calculate  pairs we will  use // 
#         leftovers = leftovers + i % 2 # to calculate pairs we will  use %

# return [/p//airs,leftovers]
        
l=[1,5,0,3,5]
for i in l:
  if i in l:
    continue
  elif i==0:
        continue
  else:
     l.append(i)
     print (i)







