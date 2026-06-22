"""QUESTION 1"""
# Given a list of integers and an integer K, rotate the list to the right by K positions
nums = [1, 2, 3, 4, 5]
k = 2
for i in range (k):
    last=nums[-1]
    for j in range (len(nums)-1,0,-1):  
        nums[j]= nums[j-1]
    nums[0]=last 
print(nums)

'''Question 2: Check Palindrome List Using Recursion
Problem Statement:
Write a recursive function to determine whether a given list is a palindrome. A list is called a palindrome if it
reads the same forward and backward.'''

nums = [1, 2, 3, 4, 5]
k = 2

nums[-2:]  = [4, 5]
nums[:-2]  = [1, 2, 3]

Result = [4, 5] + [1, 2, 3]
[4, 5, 1, 2, 3]

# QUESTION 4
nums = [4, 5, 1, 2, 0, 4, 1, 2]
def first_non_repeating(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for num in nums:
        if freq[num] == 1:
            return num

    return -1
nums = [4, 5, 1, 2, 0, 4, 1, 2]

print(first_non_repeating(nums))


'''Question 5:
Count Frequency of Each Element
Problem Statement:
Given a list of integers, count how many times each element appears in the list and store the result in a
dictionary.'''
nums = [1, 2, 2, 3, 3, 3]
def count_frequency(nums):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq

nums = [1, 2, 2, 3, 3, 3]
print(count_frequency(nums))
