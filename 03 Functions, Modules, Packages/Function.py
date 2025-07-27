#Q1. Write a function to return the sum of all numbers in a list.
#Sample List: (8, 2, 3, 0, 7)
#Expected Output: 20
def listSum(l):
    sum=0
    for item in l:
        sum+=item
    return sum
print(listSum([8, 2, 3, 0, 7]))

#Q2. Write a function to return the reverse of a string.
#Sample String: "1234abcd"
#Expected Output: "dcba4321"
def revString(String):
    return String[::-1]
print(revString("1234abcd"))

#Q3. Write a function to calculate and return the factorial of a number (a non-negative integer).
def factorial(n):
    fact=1
    if n==0:
        return fact
    for i in range (1,n+1):
        fact=fact*i
    return fact
print(factorial(5))

#Q4. Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.
def countUpper_Lower(str):
    upper_count=0
    lower_count=0
    for char in str:
        if char.isupper():
            upper_count+=1
        elif char.islower():
            lower_count+=1
    return f"Upper Count : {upper_count}\nLower Count : {lower_count}"
print(countUpper_Lower("Hello World"))

#Q5. Write a function to print the even numbers from a given list. List is passed to the function as an argument.
#Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Result [2, 4, 6, 8]
def printEven(l):
    even=[]
    for n in l:
        if n%2==0:
            even.append(n)
    return even
print(printEven([1, 2, 3, 4, 5, 6, 7, 8, 9]))

#Q6. Write a function that takes a number as a parameter and checks whether the number is prime or not.
def checkPrime(n):
    if n==0 or n==1:
        return False
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
print(checkPrime(9))