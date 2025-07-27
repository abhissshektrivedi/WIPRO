#Q1. Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
try:
    result = a / b
    print("Result:", result)
except:
    print("Error: Cannot divide")

#Q2. Write a program to accept a number from the user and check whether it's prime or not. If user enters anything other than number, handle the exception and print an error message.
try:
    n = int(input("Enter a number: "))
    if n < 2:
        print("Not Prime")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
except:
    print("Error: Invalid input")

#Q3. Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.
filename = input("Enter file name: ")
try:
    file = open(filename, "r")
    content = file.read()
    print(content.title())
    file.close()
except:
    print("Error: File not found")

#Q4. Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid Index is entered, handle the exception and print an error message.
numbers = [5, -3, 7, -1, 9, -6, 2, -8, 4, -10]
try:
    index = int(input("Enter index: "))
    value = numbers[index]
    if value >= 0:
        print("Positive number")
    else:
        print("Negative number")
except:
    print("Error: Invalid index")
