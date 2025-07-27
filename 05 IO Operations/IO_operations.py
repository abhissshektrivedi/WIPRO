#Q1. Write a program to read the entire content from a txt file and display it to the user.
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

#Q2. Write a program to read first n lines from a txt file. Get n as user input.
n = int(input("Enter number of lines: "))
file = open("sample.txt", "r")
for i in range(n):
    line = file.readline()
    print(line, end="")
file.close()

#Q3. Write a program to accept input from user and append it to a txt file.
text = input("Enter text to append: ")
file = open("sample.txt", "a")
file.write(text + "\n")
file.close()

#Q4. Write a program to read contents from a txt file line by line and store each line into a list.
file = open("sample.txt", "r")
lines = file.readlines()
lines = [line.strip() for line in lines]
print(lines)
file.close()

#Q5. Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
file = open("sample.txt", "r")
content = file.read()
words = content.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)
file.close()

#Q6. Write a program to count the frequency of a user entered word in a txt file.
word = input("Enter a word: ")
file = open("sample.txt", "r")
content = file.read()
words = content.split()
count = words.count(word)
print("Frequency:", count)
file.close()
