# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.


def sum(n):
    num = 0
    i = 0
    while i <= n:
        num += i
        i+= 1
    return num 

# print(sum(6))

# Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.
def largest(nums):
    return max(nums)

# print(largest([1, 2, 3, 4, 0]))
# print(largest([10, 4, 2, 231, 91, 54]))

# Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

def occurances(string1, string2):

    occurance = string1.count(string2)
    return occurance

# print(occurances('fleep floop', 'e'))   # returns 2
# print(occurances('fleep floop', 'p'))  # returns 2
# print(occurances('fleep floop', 'ee'))  # returns 1
# print(occurances('fleep floop', 'fe')) # returns 0

def product(*args):
    sum = 1
    for num in args:
        sum = sum * num
    return sum

print(product(-1, 4))

