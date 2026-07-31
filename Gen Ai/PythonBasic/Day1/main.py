print ("Hello World")

#comment
# toh hum python ma comment# se karta hai aur mutli line comment ke liye hum triple quote ka use karte hai """" hyy""""

#varible
name = "Akshat"
print (name)

#namespace 
fullname = "Akshat Srivastava" # Cammel Case
FullName = "Akshat Srivastava" # Pascal Case
Full_name = "Akshat Srivastava" # Snake Case

 #Data Types
r = 12 # Interger
u= 12.5 # Float
c = "Akshat124^&&(353" # String
d=34j # Complex

#String 
y="Akshat"
print (y[0]) # INDEXING THIS IS CALLED String Indexing answer kaval A aayega 
print (y[0:3]) # SLICING THIS IS CALLED String Slicing answer kaval Aks aayega
 # type Casting
x = 1 # int
x= str(x) # int to string
o = "3" # string
o = int(o) # string to int

 #Input and output

name1 = "Akshat"
print(f"Hello, my name is {name1}")


#input 
# g =  input ("Type your number ")
# print(g)
# # q2
# age = input ("Type your age ")
# print (age)

# Opertor 
# Arthimetic opertor
#add
q=300
t=4
print (q+t)

#sub
print (t-q)
print(q*t)
print (q/t)
print (q%t)
print (q//t) # float division esse point ke baad wali value nhi aati hai 
print (q**t)

# Assignment opertor 
w = 23
# resign 
w= 24  # now the value of w=24 because it assign the value

# compound assign opertor
# w=23
# w=w+23
# w= w+23
w=23
w+=23
w+=23
print (w) #69

#comparsion opertor
# ==, !=, >, <, >=, <=
c= 23
m=23
j= 24
print (c==m) # True
print (c<j) # True
print (c!=j) # True 
print (c>j) # False
print (c<=j) # True
print (c>=j) # False
print (ord("a")) # 97 ASCII value of a
print (ord("A")) # 65
print (ord("z")) # 122 ASCII value of z
print (ord("Z")) # 90 ASCII value of Z

# Logical opertor
# and, or, not
print (True and True) # True
print (True and False) # False
print (False and False) # False
print (True or True) # True
print (True or False) # True
print (False or False) # False
print (not True) # False
print (not False) # True
 
# conditional statement

# if elso
if 5>2:
    print ("5 is greater than 2")
else:
    print ("5 is not greater than 2")