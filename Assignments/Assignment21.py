
#Palindrome without slicing

name = input("Enter your string: ")
reverse = ""
for char in name:
    reverse = char + reverse
if name == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
