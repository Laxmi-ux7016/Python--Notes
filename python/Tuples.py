# Tuples 
# 1.Tuples are order (indexing allow)
# 2. Tuples can have duplicacy
# 3. Are hetrogenous (can not change the values )
# 4. Are imutable 

t=()# empty tuple
#DIRECT LOOP 
# t= (1,2,3,4,5)
# for i in t:
#     print(i)
# # INDEX LOOP
#     for i in range (len (t)):
#         print(i,t[i])

# for  index ,value in enumerate(t):
#     print(index ,value)

# t=(1,2,3,4,5)
# print(t[1:4])

# METHOD IN TUPLES
# 1. count()
# 2.index()

# t=(1,2,2,2,3,4,5,3,4)
# print(t.count(3))

# t=(1,2,2,2,3,4,5,3,4)
# print(t.index(4)) # first occurence of 3

# MEMBERSHIP OPERATOR IF THE ELEMENT IS FROM THE GIVEN SET 
# t=(1,2,2,2,3,4,5,3,4)
# print(3 in t)
# print(9 in t)

# #TUPLE UNPACKING ( all value are distribute in value)
# t= (1,2,3,4,5)
# a,b,c,d,e=t
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# # PACKING ( this is unpaking)
# a=1,2

# STAR EXPRESSION(*)   
# t=(1,2,3,4,5)
# a,*b,c=t
# print(a)
# print(b)  #Middle value Extraction 
# print(c)


