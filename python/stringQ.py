# April 15 may Slicing value 15(n+1)14

#31. PRINT STRING IN REVERSE, ITS LENGTH IN UPPERCASE,LOWERCASE AND COPY INTO ANOTHER STRING
s= "shery"
print(s[::-1])
print(len(s))
#OR
s="shery"
print(F"reverse string (s[::-1])")
print(f'length of string {len(s)}')
print(f'string in upper format{s.upper()}')
print(f'string in lower format{s.lower()}')

#32. ARRANGE STRING.......
# s="ShEry"
# lower=""
# upper=""
# for i in s:
#     if i.islower():
#         lower=lower+i
#     elif i.isupper():
#         upper=upper+i
# print(lower+upper)

# #33. COUNT ALL
# str1="p@#yn26at^&i5ve"
# alpha=0
# digit=0
# special=0
# for i in str1:
#     if i.isalpha ():
#         alpha=alpha +i
#     elif i.digit():
#         digit=digit+i
#     else:
#         special=special+i
# print(f"Alphabat count :{alpha}")
# print(f"digit count :{digit}")
# print(f"special count :{special}")

#34 COMPRE TWO STRING WITHOUT USING INBUILT FUNCTION
# str1="hello"
# str2="hello"
# if len(str1)==len (str2):
#     for i in range(len(str1)):
#         if str1[0]!=str2[0]:
#             print('string are not a same')
#             break
#     else:
#         print("string are same")

# else:
#     print("both string are of not the same length ")    

##  16 April 2026
#35.COUNT VOWELS FROM GIVEN STRING
# def countvowels():   
#   str1="Hello"
# vowels="aeiouAEIOU" 
# count=0
# for i in str1 :
#     if i in vowels:
#         count+=1
#         print(f"total count of vowels are:{count}")
# print(countvowels())
# (DOUTS)

# 36.REVERSE A STRING 
# S="hello"
# # for i in s[::-1]:
# #    print(i)(douts)
   
# s="hello"
# rev=""
# for i in s[::-1]:
#    rev=rev+i
#    print(rev)
   
# 37.check string is palindrome or not
# s="madam"
# rev=""
# for i in s[::-1]:
#    rev=rev+i
#    print(rev)

# s="madam"
# rev=s[::-1]
# if s==rev:
#    print(f"{s}is not a palindrome")
# else:
#    print(f"{s}is a palindrome")
# 37. check string is palindrome.

# def palindrome():
#  rev=s[::-1]
# if s==rev:
#    print(f"{s}is not a palindrome")
# else:
#    print(f"{s}is a palindrome")

# palindrome("Madam")

# 39. count number of vowels and consonants from a string
# s1 = "Golmaal"
# consonant=0
# vowels=0
# for i in s1:
#     if i in "aeiouAEIOU":
#        vowels+=1
#     else:
#         consonant+=1
# print(f"total vowels are:{vowels}")
# print(f"total consonants are :{consonant}")
       

