# Functions
# def hello():
#     print("Hello, World!")

# hello()

# parmaters
def sum (a, b):
  print (f"Sum of {a} and {b} is: {a + b}")

sum(5, 10)
sum (20, 30)

# Arguments
def greet(name):
    print(f"Hello, {name}!")    

greet("Alice")    

#  types of arguments
# 1. Positional arguments
def sum (a, b):
  print (f"Sum of {a} and {b} is: {a + b}")

sum(5, 10)
sum (20, 30)

# 2. Keyword arguments
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")   

greet(name="Alice", age=25)

# 3. Default arguments
def greet(name, age=30):    
    print(f"Hello, {name}! You are {age} years old.")

greet("Bob")  # age will use the default value of 30

# palindrome
def is_palindrome(st):
    return st == st[::-1]

palindrome_str = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(palindrome_str):
    print(f"{palindrome_str} is a palindrome.") 
else:
    print(f"{palindrome_str} is not a palindrome.") 

# return statement
def add_numbers(a, b):
    return a + b

print (add_numbers(5, 10))  # Output: 15

# what is data structures?
# Data structures are ways of organizing and storing data in a computer so that it can be accessed and modified efficiently.
# types of data structures
# 1. List
# my_list = [1, 2, 3, 4, 5]

#  4 key points about list
# 1. Ordered: Lists maintain the order of elements as they are added.
# example: my_list = [1, 2, 3, 4, 5]  # The order of elements is preserved.

# 2. Mutable: You can change, add, or remove elements from a list after it has been created.
# example: my_list[0] = 10  # Changes the first element to 10.

# 3. Allows Duplicates: Lists can contain duplicate elements.
# example: my_list = [1, 2, 2, 3, 4]  # The number 2 appears twice in the list.

# 4. Indexed: Each element in a list has an index, starting from 0 for the first element.
# example: my_list[0]  # Accesses the first element of the list, which is 1.
 
#  Indexing and slicing
n = [1, 2, 3, 4, 5]
print(n[0])  # Output: 1 (first element)

# Slicing
print(n[1:4])  # Output: [2, 3, 4] (elements from index 1 to 3)

# List Traversing
#  yeh kaval value ke liye use hota hai
for element in n:
    print(element)  # Output: 1 2 3 4 5 (each element printed on a new line)

# yeh index ke liye use hota hai
for i in range(len(n)):
    print(n[i])  # Output: 1 2 3 4 5 (each element printed on a new line)


 # methods of list

# 1. append(): Adds an element to the end of the list.
# example: my_list.append(6)  # Adds 6 to the end of the list.

m = [1, 2, 3]

m.append(4)  

print(m)  # Output: [1, 2, 3, 4] 

# 2. insert(): Inserts an element at a specified index.
# example: my_list.insert(1, 10)  # Inserts 10 at index 1.

j = [1, 2, 3]

j.insert(1, 10)

print(j)  # Output: [1, 10, 2, 3]

# 3. extend(): Extends the list by appending elements from another iterable.
# example: my_list.extend([7, 8, 9])  # Adds

p= [1, 2, 3]
p.extend([4, 5, 6])
print(p)  # Output: [1, 2, 3, 4, 5, 6] 

# 4. remove(): Removes the first occurrence of a specified element from the list.
# example: my_list.remove(2)  # Removes the first occurrence of 2 from  

k=  [1, 2, 3, 2, 4]
k.remove(2)
print(k)  # Output: [1, 3, 2, 4] (the first occurrence of 2 is removed)

# 5. pop(): Removes and returns the element at a specified index (or the last element if no index is specified).
# example: my_list.pop(1)  # Removes and returns the element at index

l= [1, 2, 3, 4]
removed_element = l.pop(1)  # Removes and returns the element at index 1    
print(removed_element)  # Output: 2 (the removed element)
print(l)  # Output: [1, 3, 4] (the list after removal)

# 6. index(): Returns the index of the first occurrence of a specified element.
# example: my_list.index(3)  # Returns the index of the first occurrence of 3
m = [1, 2, 3, 4, 5]
print(m.index(3))  # Output: 2 (the index of the first occurrence of 3)

# 7. count(): Returns the number of occurrences of a specified element in the list.
# example: my_list.count(2)  # Returns the number of occurrences of 2   
n = [1, 2, 2, 3, 4]
print(n.count(2))  # Output: 2 (the number of occurrences of 2 in the list)

# 8. sort(): Sorts the elements of the list in ascending order (by default).
# example: my_list.sort()  # Sorts the list in ascending order
o = [5, 2, 8, 1, 9]
o.sort()  # Sorts the list in ascending order
print(o)  # Output: [1, 2, 5, 8, 9] (the sorted list)

# 9. reverse(): Reverses the order of the elements in the list.
# example: my_list.reverse()  # Reverses the order of the elements in the list
p = [1, 2, 3, 4, 5]
p.reverse()  # Reverses the order of the elements in the list
print(p)  # Output: [5, 4, 3, 2, 1] (the reversed list)

# 10. clear(): Removes all elements from the list.
# example: my_list.clear()  # Removes all elements from the list        
q = [1, 2, 3, 4, 5]
q.clear()  # Removes all elements from the list
print(q)  # Output: [] (the list is now empty)

# 11. copy(): Returns a shallow copy of the list.
# example: my_list.copy()  # Returns a shallow copy of the list
r = [1, 2, 3, 4, 5]
s = r.copy()  # Creates a shallow copy of the list
print(s)  # Output: [1, 2, 3, 4, 5] (the copied list)

# 12. list(): Converts an iterable (like a string or tuple) into a list.
# example: list("hello")  # Converts the string "hello" into a list of characters
t = list("hello")  # Converts the string "hello" into a list of characters
print(t)  # Output: ['h', 'e', 'l', 'l', 'o'] (the list of characters)

# 13. len(): Returns the number of elements in the list.
# example: len(my_list)  # Returns the number of elements in the list
u = [1, 2, 3, 4, 5]
print(len(u))  # Output: 5 (the number of elements in the list)

# 14. in operator: Checks if an element exists in the list and returns True or False.
# example: 3 in my_list  # Returns True if 3 is in the list
v = [1, 2, 3, 4, 5]
print(3 in v)  # Output: True (3 exists in the list)    

# 15. not in operator: Checks if an element does not exist in the list and returns True or False.
# example: 6 not in my_list  # Returns True if 6 is not in the list
w = [1, 2, 3, 4, 5]
print(6 not in w)  # Output: True (6 does not exist in the list)

# 16. min(): Returns the smallest element in the list.
# example: min(my_list)  # Returns the smallest element in the list
x = [5, 2, 8, 1, 9]
print(min(x))  # Output: 1 (the smallest element in the list)

# 17. max(): Returns the largest element in the list.
# example: max(my_list)  # Returns the largest element in the list
y = [5, 2, 8, 1, 9]
print(max(y))  # Output: 9 (the largest element in the list)

# 18. sum(): Returns the sum of all elements in the list.
# example: sum(my_list)  # Returns the sum of all elements in the list  
# z = [1, 2, 3, 4, 5]
# print(sum (z))  # Output: 15 (the sum of all elements in the list)

# Q1 print postive and negative number of the list 
v = [12,13,15,-16,18,-17]
print ("postive number are ")
for i in v:
    if i>=0:
         print (i)    

print ("negative numbers are ")
for i in v:
    if i<0:
       print (i)

# Q2 Mean of the list 
b = [45,74,74,85,96,21,96]

sum =0

for i in b:
    sum = sum + i

print (sum //len(b))


# Tuples 
# exampleof the tuples 
a = (1,2,3,4,56,7,9)  #this is called the tuples
print (a)

# term0logy in tuples4

# Tuple method
numbers = (10, 20, 20, 30, 40)

# count()
print(numbers.count(20))
# Output: 2

# index()
print(numbers.index(30))
# Output: 3

# Set in Python

# A set is a built-in Python data type used to store unique (non-duplicate) elements. Sets are unordered, mutable, and do not allow duplicate values.

# Creating a Set
# Using curly braces
# fruits = {"apple", "banana", "mango"}

# print(fruits)

# Output (order may vary):

# {'banana', 'apple', 'mango'}
# Duplicate Values Are Removed
# numbers = {1, 2, 2, 3, 4, 4, 5}

# print(numbers)

# Output:

# {1, 2, 3, 4, 5}
# Empty Set

# ⚠️ {}
# creates a dictionary, not a set.

# a = {}
# print(type(a))
# # <class 'dict'>

# b = set()
# print(type(b))
# # <class 'set'>
# Set Methods
# 1. add()

# Adds one element.

# fruits = {"apple", "banana"}
# fruits.add("mango")

# print(fruits)
# 2. update()

# Adds multiple elements.

# fruits = {"apple", "banana"}

# fruits.update(["mango", "orange"])

# print(fruits)
# 3. remove()

# Removes an element.
# If it doesn't exist, it gives an error.

# fruits = {"apple", "banana", "mango"}

# fruits.remove("banana")

# print(fruits)

# Error example:

# fruits.remove("grapes")
# # KeyError
# 4. discard()

# Removes an element.
# If it doesn't exist, no error.

# fruits = {"apple", "banana"}

# fruits.discard("grapes")

# print(fruits)
# 5. pop()

# Removes and returns a random element.

# fruits = {"apple", "banana", "mango"}

# removed = fruits.pop()

# print(removed)
# print(fruits)
# 6. clear()

# Removes all elements.

# fruits = {"apple", "banana"}

# fruits.clear()

# print(fruits)

# Output:

# set()
# 7. copy()

# Creates a copy.

# a = {1, 2, 3}

# b = a.copy()

# print(b)
# 8. union()

# Combines two sets.

# A = {1, 2, 3}
# B = {3, 4, 5}

# print(A.union(B))

# Output:

# {1, 2, 3, 4, 5}
# 9. intersection()

# Common elements.

# A = {1, 2, 3}
# B = {2, 3, 4}

# print(A.intersection(B))

# Output:

# {2, 3}
# 10. difference()

# Elements in the first set but not the second.

# A = {1, 2, 3}
# B = {2, 3, 4}

# print(A.difference(B))

# Output:

# {1}
# 11. symmetric_difference()

# Elements that are in either set but not in both.

# A = {1, 2, 3}
# B = {2, 3, 4}

# print(A.symmetric_difference(B))

# Output:

# {1, 4}
# 12. issubset()

# Checks if one set is a subset of another.

# A = {1, 2}
# B = {1, 2, 3, 4}

# print(A.issubset(B))

# Output:

# True
# 13. issuperset()

# Checks if one set is a superset of another.

# A = {1, 2, 3, 4}
# B = {1, 2}

# print(A.issuperset(B))

# Output:

# True
# 14. isdisjoint()

# Checks whether two sets have no common elements.

# A = {1, 2}
# B = {3, 4}

# print(A.isdisjoint(B))

# Output:

# True
# Set Operators
# A = {1, 2, 3}
# B = {3, 4, 5}

# print(A | B)   # Union
# print(A & B)   # Intersection
# print(A - B)   # Difference
# print(A ^ B)   # Symmetric Difference

# Output:

# {1, 2, 3, 4, 5}
# {3}
# {1, 2}
# {1, 2, 4, 5}
# Membership Test
# fruits = {"apple", "banana"}

# print("apple" in fruits)
# print("mango" in fruits)

# Output:

# True
# False
# Key Points
# ✅ Stores unique values only.
# ✅ Unordered (no indexing).
# ✅ Mutable (can add/remove elements).
# ❌ Does not allow duplicates.
# ❌ Cannot access elements using indexes like set[0].
# ⚡ Very fast for membership testing (in) because sets are implemented using a hash table.

# Interview tip: If you need to remove duplicates from a list, convert it to a set:

# numbers = [1, 2, 2, 3, 3, 4]

# unique_numbers = list(set(numbers))

# print(unique_numbers)
# # [1, 2, 3, 4] (order is not guaranteed)