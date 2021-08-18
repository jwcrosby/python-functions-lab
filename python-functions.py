# 1. Write a function named `sum_to` that accepts a single integer, `n`, 
#     and returns the sum of the integers from 1 to `n`.

def sum_to(n):
  sum = 0
  for num in range(1, n + 1):
    sum += num
  return sum

print(sum_to(6))
print(sum_to(10))


# 2. Write a function named `largest` that takes a list of numbers as an argument 
#     and returns the largest number in that list.

def largest(numbers):
  largestNum = 0
  for num in numbers:
    if num > largestNum:
      largestNum = num
  return largestNum

print(largest([1,2,3,4,5]))
print(largest([2,10,25,50,100]))


# 3. Write a function named `occurances` that takes two string arguments as input
#     and counts the number of occurances of the second string inside the first string.

#     For example:

#     ```python
#     occurances('fleep floop', 'e')   # returns 2
#     occurances('fleep floop', 'p')   # returns 2
#     occurances('fleep floop', 'ee')  # returns 1
#     occurances('fleep floop', 'fe')  # returns 0
#     ```

def occurances(bigString, lilString):
  removedLilStrings = bigString.replace(lilString, '')
  # "//" is floor division, removes remainder
  return (len(bigString) - len(removedLilStrings)) // len(lilString)

print(occurances('fleep floop', 'e'))
print(occurances('fleep floop', 'p'))
print(occurances('fleep floop', 'ee'))
print(occurances('fleep floop', 'fe'))

# 4. Write a function named `product` that takes an *arbitrary* number of numbers,
#     multiplies them all together, and returns the product. HINT: Review your notes on `args`.

#     For example:

#     ```python
#     product(-1, 4) # returns -4
#     product(2, 5, 5) # returns 50
#     product(4, 0.5, 5) # returns 10.0
#     ```







