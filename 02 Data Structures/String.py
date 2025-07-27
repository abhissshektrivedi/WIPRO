#Q1. Write a program to count the number of upper and lower case letters in a String.
s="This is a Sample STRING."
upper_count=0
lower_count=0
for char in s:
    val=ord(char)
    if val>=65 and val<=90:
        upper_count+=1
    elif val>=97 and val<=122:
        lower_count+=1
print("String :",s)
print("Upper case count :",upper_count)
print("Lower case count :",lower_count)

#Q2. Write a program that will check whether a given String is Palindrome or not.
import re
s="A man, a plan, a canal: Panama"
clean= re.sub(r'[^a-z0-9]', '', s.lower())
s_rev=clean[::-1]
if clean==s_rev:
    print(s,"is Palindrome.")
else:
    print(s,"is not Palindrome.")

#Q3. Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string. The string length will be >=2.
#If input is "Wipro" then output should be "Wiwiwiwiwi".
s="Wipro"
print((s[0]+s[1])*len(s))

#Q4. Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged. 
#If the input is "xhix", then output is "Hi".
s="xo"
new_s=s.lower()
if s[-1]=="x" or s[0]=="x":
    if s[-1]=="x" and s[0]=="x":
        print(s[1:-1])
    elif s[0]=="x":
        print(s[1:])
    elif s[-1]=="x":
        print(s[:-1])
else:
    print(s)

#Q5. Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 0 and the length of the string inclusive. 
#For example if the inputs are "Wipro" and 3, then the output should be "propropro".
s="Wipro"
input=3
char=""
for i in range (input,0,-1):
    char+=s[-i]
print(char*input)