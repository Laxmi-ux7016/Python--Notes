# Q.1 
# a=int(input ("how many elements your want :"))

# l=[]
# for i in range(a):
#     z=int(input("tell your number"))
#     l.append(z)

# print(l)


# n=int(input("enter your number"))
# a=[1,2,3,4,5]
# l=[]
# for i in range (len(a)-1,1,-1):
#     l.append(a[i])
# print()
# Q.2 print list number and reverse order
# a=[10,20,30,40,50]
# l=[]
# for i in range (len(a)-1,-1,-1):
#     l.append(a[i])
# print(l)


# Q.3   swapping.
#  """a= [10,20,30,40,50]
#  z=len(a)-1
# for i in range (len(a)//2):
#     a[i],a[z]=a[z],a[i]
#     z=z-1

# print(a)"""

#Q.4 positive and negative number seprate.
# a=[1,2,-4,-2,1,-5,-2,12,45,8]
# for i in a:
#     if i >0:
#         print(i)
# for i in a:
#     if i in a:
#         if i <0:
#             print(i)


# Q.1 Create a list of 5 numbers and print each item.
# l=[]
# for i in range (5):
#     num=int(input("enter your number"))
#     l.append(num)

# print(l)

# Q.2 Create a list of 3 fruits and print each item.
# l=[]
# for i in range (3):
#     a=input("Tell your fruts name")
#     l.append(a)

# print(l)

# Q.3 Create a list and print the first elements.
# l=[]
# for i in range(5):
#     a=int(input("enter your number"))
#     l.append(a)

# print(l[0])
# Q.4 Create a list print the last element
# l=[]
# for i in range (3):
#     a=int(input ("enter your number:"))
#     l.append(a)

# print(l[2])
# Q.5 Create a list and print its length.

# Q.9 Create a list and print all elements using lop
# l=[]
# for i in range(3):
#     a=int(input("enter your number"))
#     l.append(a)

# print(l)
# Q.6 create a list and remove an element


# 22 APRIL 2026
# Bubble sort
# a=[56,12,69,23,56,90,13]
# for j in range (len (a)-1 ):
#    for i in range(0,len (a)-1-j):
#     if a[i]>a[i+1]:# compare kiya
#         a[i],a[i+1]=a[i+1],a[i]# swappe 

# print(a)

# a=[56,12,47,67,80,15]
# for i in range(len(a)-1):
#     for i in range(0,len(a)-1 ):
#         if a[i]>a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]
        
# print(a)

# #find the greatest element  largest 
 
# a=[56,12,69,23,56,90,13]
# for j in range (len(a)-1):
#     for  i in range(0,len(a)-1,-j):
#      if a[i]>a[i+1]:
#         a[i],a[i+1]=a[i+1],a[i]
# print(a)
## April 23 2026
#Start question
# l=[1,16,17,23,2,45,89]
# largest =l[0]
# for i in l:
#     if i>largest:
#         largest=i
# print(largest)
#OR

# l=[1,16,17,23,2,45,89]
# largest =l[0]
# s_largest=l[0]
# for i in l:
#     if i>largest:
#         s_largest=largest
#         largest=i
# print(largest)
# print(s_largest)
# #OR
# l=[1,16,17,23,2,45,89]
# largest =l[0]
# s_largest=l[0]
# for i in l:
#     if i>largest:
#         s_largest=largest
#         largest=i
#     elif i>s_largest:
#         s_largest=i
# print(largest)
# print(s_largest)
# #OR
#QUESTION
# l=[1,16,17,23,2,45,89]
# largest =l[0]
# s_largest=l[0]
# s_largest_index=0
# for i in range (1,len(1)):
#     if 1[i]>largest:
#         s_largest=largest
#         largest=l[i]
#         second_largest_index=s_largest_index
#         largest_index=i

#     elif l[i]>s_largest:
#        s_largest=l[i]
# print(largest,largest_index)
# print(s_largest,second_largest_index)
# QUESTION
# l=[1,16,17,23,2,45,89]
# smallest =float("inf")
# smallestt_index =0
# s_smallest = float("inf")
# s_smallest_index = -1

# for i in range (len(l)):
#     if l[i] < smallest:
#         s_smallest = smallest
#         smallest = l[i]
#         s_smallest_index = s_smallest_index
#         smallest_index = i

#     elif l[i] <  s_smallest:
#        s_smallest = l[i]
#        s_smallest_index = i
# print(smallest,smallest_index)
# print(s_smallest,s_smallest_index)

#  24  April 2026
#47 check if list is sorted or not
# l=[1,2,3,4,5,6,7]
# for i in range(len(l)-1):
#     if l[i]>l[i+1]:
#         print("list is not sorted")
#         break
# else:
#     print("list is sorted")
#Q.48 Pallindrome
# l=[2,3,15,15,3,2]
# for i in range (len(l)//2):
#     if l[i]!=l[len(l)-1-i]:
#          print("list is not a palindrome")
#          break
# else: 
#      print("list is palindrome")
# 
# n=int(input("enter a number"))
# l=[]
# sum=0

# for i in range(n):
#     inputs =int(input(f'enter the elements at index'))
#     sum+=input
#     l.append(inputs)
#     print(l)
#     print(sum)
        
# lst= list (map(int,input ('enter element').split()))
# print(lst)
# map (data types,input)
# split (seprate all the value and digit)
#list (covertsthe value in the form of list data structure)

"""sabse pehle input accept --> har input split hoga --> input will be type casted the form of int 
we sorted all the values inside a list"""
# l=[1,2,3,4,5,6,7]
# for i in range(len(l)-1):
#     l[i]>l[i+1]
#     print("list is not sorted")
#     break
# else:
#     print("list is sorted")

# 1.Ask the user to enter a list of number and print the largest element.
# l=[2,5,1,8]
# largest =l[0]
# for i in l:
#      if i>largest:
#          largest=i
# print(largest)
 # 2.Ask the user to enter a list and print the smallest element.
# l=[4,2,9,1]
# smalllest=l[0]
# for i in  l:
#      if i<smalllest:
#           smallest=i
# print(smallest)
# 3. Ask the user to enter a list and print sum of all elements.
# l=[1,2,3,4]
# sum=0
# for i in l:
#     sum=sum+i
    
# print(sum)
#.4 Ask the user to enter a list and count even number.
# l=[1,2,3,4,5]
# count=0
# for i in l:
#      if i%2==0:
#         count+=1
# print("even number",count)

#5. l=[1,2,3,4,5]
# count=0
# for i in l:
#      if i%2!=0:
#         count+=1
# print("odd number",count)
# 6. reverse
# l=[1,2,3]
# rev=0
# print(l[::-1])

# 7.Ask the user  to ente ra list and remove duplicate.
# num=input[ 1,2,2,3,3]## DOUTS
# l=list (map(int,num.spli()))
# new_list=[]
# for  i in l:
#     if i not in new_list:
#         new_list.append(i)
# print("Without duplicates",new_list)

# 8.Ask the user to enter a list and sort it in ascending order.
# n=int(input("enter your number..."))##DOUTS
# l=[2,8,1]
# l=list (map(int,n.split()))



# num=(int(input ("entr your name"even)))
# l.sort()
# print("sorted list:",l)
# Q.9
# l=[10,20,4,45]
# largest =l[0]
# s_largest=l[0]
# for i in l:
#     if i>largest:
#         s_largest=largest
#         largest=i

# print(s_largest)

# Q. 10
l=[10,20,30,40,50]
# smallest =float("inf")
# smallestt_index =0
# s_smallest = float("inf")
# s_smallest_index = -1

# for i in range (len(l)):
#     if l[i] < smallest:
#         s_smallest = smallest
#         smallest = l[i]
#         s_smallest_index = s_smallest_index
#         smallest_index = i

#     elif l[i] <  s_smallest:
#        s_smallest = l[i]
#        s_smallest_index = i
# print(smallest,smallest_index)
# print(s_smallest,s_smallest_index)

# 27 April 2026
# Rotate a list by K elements
# l=[1,2,3,4,5]# o//p =k=2 [4,,5,1,2,3]
# k=2
# for i in range (k):
#     last=l[-1]# last value 5
#     for j in range (len(l)-1,0,-1):  #j-->4,3,2,1
#         l[j]= l [j-1]
#     l[0]=last 
# print(l)

# # Assign all the 0s at the end of the list
# l=[0,1,0,3,12]
# j=0
# for i in range (len(l)):
#     if l[i]!=0:
#         l[i],l[j]=l[j],l[i]#(value swapping)
#         j=j+1# (value swape kro indicate )
# print(l)

# l=[1,2,3,4,5]
# k=2
# for i in range(k):
#     last=l[-1]
#     for j in range (len (l)-1,0,-1):
#         l[j]= l[j-1]
#         l[0]=last
# print(l)

# l=[1,2,3,4,5]# o//p =k=2 [4,,5,1,2,3]
# k=2
# for i in range (k):
#     last=l[-1]# last value 5
#     for j in range (len(l)-1,0,-1):  #j-->4,3,2,1
#         l[j]= l [j-1]
#         l[0]=last 
# print(l)

# 42) ACCEPT SIZE n from user and create a n size list than take n inputs into tha and finally
# print the sum of all elements in the list in the following manner 
# 10+20+30=60
# l=[10,20,30]
# sum=0
 
# 44) Find the greatest element and print its index too.
#    {2, 96, 69, 77, 145, 20} = Max element = 145 found at 4 index
# l=[1,2,3,4,5]
# k=2
# for i in range(k):
#     last=l[-1]
#     for j in range (len(l)-1,0,-1):
#         l[0]=last
# print(l)

# l = [1,2,3,4,5]
# k = 2

# for i in range(k):
#     last = l[-1]           # 5

#     for j in range(len(l)-1, 0, -1):
#         l[j] = l[j-1]      # shift right

#     l[0] = last            # put last element at first

# print(l)

