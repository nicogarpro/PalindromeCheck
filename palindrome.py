import time
import sys

number = input("Enter a number\n")

if number == number[::-1]:
    print("Palindrome")

elif number != number[::-1]:
    print("Not palindrome")

time.sleep(3)

sys.exit
