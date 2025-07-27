#Q1. Write a program to accept two numbers as command line arguments and display their sum.
import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
total = num1 + num2
print("Sum:", total)

#Q2. Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.
import sys
filename = sys.argv[0]
message = sys.argv[1]
print("File Name:", filename)
print("Welcome Message:", message)


#Q3. Write a program to accept 18 numbers through command line arguments and calculate the sum of prime numbers among them.
import sys
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
numbers = sys.argv[1:]
total = 0
for num in numbers:
    n = int(num)
    if is_prime(n):
        total = total + n
print("Sum of prime numbers:", total)
