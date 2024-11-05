import time
import sys

text = input("Enter text\n")

text_str = str(text)

if text_str == text_str[::-1]:
    print("Palindrome")

elif text_str != text_str[::-1]:
    print("Not palindrome")

time.sleep(3)

sys.exit
