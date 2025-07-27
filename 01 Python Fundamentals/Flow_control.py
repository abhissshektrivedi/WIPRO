#Q1. Write a program to check if a given number is Positive, Negative or Zero.
num=int(input("Enter any number: "))
if num == 0:
    print("Given Number is Zero")
elif num>0:
    print("Given Number is Positive")
else:
    print("Given Number is Negative")

#Q2. Write a program to check if a given number is odd or even.
num=int(input("Enter any number: "))
if num%2==0:
    print("Given Number is Even")
else:
    print("Given Number is Odd")

#Q3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
num1=int(input("Enter any number: "))
num2=int(input("Enter any number: "))
if num1>=0 and num2>=0:
    a=num1-num2
    if a%10==0:
        print("Given Number have same last digit.")
    else:
        print("Given Number does not have same last digit.")
else:
    print("Number is negative.")

#Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range (1,11):
    print(i, end="  ")

#Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row.
for i in range (23,58):
    if i%2==0:
        print(i)

#Q6. Write a program to check if a given number is prime or not.
num=int(input("Enter any Number: "))
if num>1:
    for i in range (2,(int(num/2))+1):
        if num%i==0:
            print("Given Number is not Prime")
            break
    else:
        print("Given Number is Prime")
else:
    print("Given Number is not Prime")

#Q7. Write a program to print prime numbers between 10 and 99.
for num in range (10,100):
    for i in range(2,int((num/2)+1)):
        if num%i==0:
            break
    else:
        print(num)

#Q8. Write a program to print the sum of all the digits of a given number.
num=int(input("Enter any number: "))
sum=0
if num<0:
    num=abs(num)
while num>0:
    ld=num%10
    sum+=ld
    num//=10
print(sum)

#Q9. Write a program to reverse a given number and print.
num=int(input("Enter any number: "))
rev=0
neg=False
if num<0:
    neg=True
    num=abs(num)
while num>0:
    ld=num%10
    rev=(rev*10)+ld
    num//=10
if neg:
    rev=-rev    
print(rev)

#Q10. Write a program to find if the given number is palindrom or not.
num=int(input("Enter any number: "))
a=str(num)
rev=a[::-1]
if a==rev:
    print("Given number is Palindrome")
else:
    print("Given number is not a Palindrome")

