#SETS
# 1.unorderd  (no indexing)
#2. semi -mutable (can add, but cannot change or remove)
'''3.unicqe elements (no duplicates)
4.Heterogenous (can contain different data tytpes)'''
#5. CREATING A SETS
'''a=[]
b={}
print(type (b))
c=set()# Type conversion 

# challenge (sat)
data types
variables 
loops
conditional statement
functions
s=set ()# Empty set
s={1,2,3,4,5}
print(type (s))'''

s={1,2,3,4,4,5,5}

# METHODS IN SET 
'''1. add()
2. update()
3.remove()
4.discard()
5.pop()'''
# 6. clear()

# s={1,2,3,4,5}
# s.add(6)
# print(s)

# s={1,2,3,4,5}
# s.update([7,8,9])
# print(s)

# REMOVE if values is not present we will get error
# s={1,2,3,4,5}#
# s.remove(5)
# print(s)

#DISCARD 
# s={1,2,3,4,5}
# s.discard(10)
# print(s)

# POP (REMOVE smallest elent from the sets )
# s={8,2,3,4,5}
# s.pop()
# print(s)

# CLEAR  (remove all this elements and give us an empty)
# s={1,2,3,4,5}
# s.clear()
# print(s)

# 1.INTERSECTION 
#2. UNION 
#3.difference
4.# Symetric difference

# intersection(common value)
# s1={1,2,3,4}
# s2={2,3,4,6}
# print(f"intersection :{s1.intersection(s2)}")

# UNOION (sare value)
# s1={1,2,3,4}
# s2={2,3,4,6}
# print(f"union:{s1.union (s2)}")

#  Differnce       (jo ek me ho dusare me na ho value)
# s1={1,2,3,4}
# s2={2,3,4,6}
# print(f"differnce s1 :{s1.difference(s2)}")

#SYMETRIC DIFFERNCE  (jo dono me value na ho)
# s1={1,2,3,4}
# s2={2,3,4,6}
# print(f"symetric differeence:{s1.symmetric_difference(s2)}")


# FROZEN SET
fs={10,20,30,40,50}
fs= frozenset (fs)
fs.add(60)
fs.remove(10)
print(fs)
