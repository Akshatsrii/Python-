# q2 Create random number 
#  they is library random which is used for generating the random number 
import random
random_num = random.randint(1, 10)
guess = int(input("Guess the number: "))
if guess == random_num:
    print("Congratulations! You guessed the correct number.")
else:
    print("Sorry, the correct number was:", random_num)

