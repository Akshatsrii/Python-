# # # Conditional Statements in Python
# # Q1 Accept two numbers from the user and print the largest number.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("The largest number is:", num1)
else:
    print("The largest number is:", num2)

# Q2 Accept the gender from the user and print "Good Morning Sir" if the gender is male
gender = input("Enter your gender (male/female): ")

if gender == "male":
    print("Good Morning Sir")
else:
    print("Good Morning Ma'am")

#     # Q3 Accept the interger and check whether it is even or odd.
# number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# # q4 Accept the age of a person and check whether they are eligible to vote or not. (age>=18)
# age = int(input("Enter your age: "))    

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#     # Q5 Accept the year and check whether it is a leap year or not. (year%4==0 and year%100!=0) or (year%400==0)
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")  

else:
    print(year, "is not a leap year.")  


# # Loop in Python
#  Type of loop
# 1. For loop
for i in range(5):
    print(i)  # This will print numbers from 0 to 4
    # reverse loop
    for j in range(16,1, -1):
        print(j)  # This will print numbers from 16 to 2
#  print the table of 5

#     # 2. While loop
count = 0       
while count < 5:
    print(count)  # This will print numbers from 0 to 4
    count += 1

#  q3 Print the table of 5 using for loop in different way
n = int (input("Enter a number to print its multiplication table: ")
         )
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
