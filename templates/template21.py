
"""Mini Project – Palindrome Checker

Palindrome = same forward & backward

Example:

madam

level"""

word = input("Enter your string: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
