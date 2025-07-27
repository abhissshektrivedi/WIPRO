#Mini Project - 2
"""
Create a Python module with the following functions:

Function Name
ispalindrome(name)
Given the user name as input, this function should tell us whether the name is a palindrome or not.

count_the_vowels(name)
Given the user name as input, this function should tell us how many vowels are present in it.

frequency_of_letters(name)
Given the user name as input, this function should tell us how many times each letter appears in the name

Note: name will be completely in either lower case or upper case

Import the module in another python script and test the functions by passing appropriate inputs

Sample input 1: bob
Sample output 1:
Yes it is a palindrome.
No of vowels: 1
Frequency of letters: b-2, 0-1

Sample input 2: marcel bentok tanaka
Sample output 2:
No it is not a palindrome.
No of vowels: 7
Frequency of letters: m-1, a-4, r-1, c-1, e-2, 1-1, b-1, n-2, 1-2, 0-1, k-2
"""
def ispalindrome(name):
    name_clean = name.replace(" ", "")
    if name_clean == name_clean[::-1]:
        return "Yes it is a palindrome."
    else:
        return "No it is not a palindrome."

def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    return f"No of vowels: {count}"

def frequency_of_letters(name):
    freq = {}
    for char in name:
        if char != " ":
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    freq_str = "Frequency of letters: "
    freq_str += ", ".join([f"{k}-{v}" for k, v in freq.items()])
    return freq_str
