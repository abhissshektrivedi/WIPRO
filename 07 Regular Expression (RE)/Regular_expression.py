#Q1. Write a program to find check if a string has only octal digits, Given string ["789", '123', '1004']
strings = ["789", "123", "1004"]
for s in strings:
    is_octal = True
    for ch in s:
        if ch not in "01234567":
            is_octal = False
            break
    if is_octal:
        print(s, "is octal")
    else:
        print(s, "is not octal")

#Q2. Extract the user id, domain name and suffix from the following email addresses.
#emails = """zuck@facebook.com
#sunder33@google.com
#jeff42@amazon.com"""
emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""
lines = emails.splitlines()
for email in lines:
    parts = email.split("@")
    user = parts[0]
    domain_parts = parts[1].split(".")
    domain = domain_parts[0]
    suffix = domain_parts[1]
    print("User ID:", user)
    print("Domain:", domain)
    print("Suffix:", suffix)
    print()

#Q3. Split the following irregular sentence into proper words
#sentence = """A, very very; irregular_sentence""" ## expected outout: A very very irregular sentence
sentence = "A, very very; irregular_sentence"
for ch in ",;_":
    sentence = sentence.replace(ch, " ")
words = sentence.split()
result = " ".join(words)
print(result)

#Q4. Clean up the following tweet so that it contains only the user's message. That is, remove 11 URLs, hashtags, mentions, punctuations, RTs and CCs.
#tweet = '''Good advice! RT @TheNextweb: What I would do differently if I was learning to code today http://t.co/lbwejepxod cc: @garybernhardt #rstats.'''
##desired_output = 'Good advice What I would do differently if I was learning to code today'
import re
tweet = '''Good advice! RT @TheNextweb: What I would do differently if I was learning to code today http://t.co/lbwejepxod cc: @garybernhardt #rstats.'''
tweet = re.sub(r"http\S+", "", tweet)
tweet = re.sub(r"RT", "", tweet)
tweet = re.sub(r"cc", "", tweet)
tweet = re.sub(r"@\w+", "", tweet)
tweet = re.sub(r"#\w+", "", tweet)
tweet = re.sub(r"[^\w\s]", "", tweet)
tweet = re.sub(r"\s+", " ", tweet)
print(tweet.strip())

#Q5. Extract all the text portions between the tags from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.html
#Code to retrieve the HTML page is given below:
"""
import requests
r=
requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html") r.text # html text is contained here
desired_output = ['Your Title Here', 'Link Name', 'This is a Header', "This is a Medium Header', 'This is a new paragraph!", "This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']
"""
import requests
from bs4 import BeautifulSoup
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html = r.text
soup = BeautifulSoup(html, "html.parser")
texts = []
for tag in soup.find_all():
    if tag.string and tag.string.strip():
        texts.append(tag.string.strip())
print(texts)

#Q6. Given below list of words, identify the words that begin and end with the same character.
"""
civic
trust
widows
maximum
museums
aa
as
"""
words = ["civic", "trust", "widows", "maximum", "museums", "aa", "as"]
for word in words:
    if word[0] == word[-1]:
        print(word)
