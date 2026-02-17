
#Check Given number is even or odd

num = int(input("Enter a positive number: "))
if num > 0:
    if num%2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Invalid input")
