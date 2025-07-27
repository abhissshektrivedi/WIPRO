#Mini Project
"""
Your friend has sent you a text file containing n lines. He sent a secret message with it, 
which tells you the place and time where you have to go and meet him.

He challenges you to find it out without seeing the content of the file. He has given hints to find it.
Let's surprise him by breaking the challenge with our python code.
"""
file = open("sample.txt", "r")
lines = file.readlines()
line_count = len(lines)

if line_count > 12:
    time = line_count % 12
    if time == 0:
        time = 12
    meet_time = str(time) + " PM"
else:
    meet_time = str(line_count) + " AM"

file = open("sample.txt", "r")
content = file.read()
words = content.split()

freq = {}
for word in words:
    word = word.strip(",.()\"").lower()
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

max_word = ""
max_count = 0
for word in freq:
    if freq[word] > max_count:
        max_count = freq[word]
        max_word = word

place = max_word.capitalize() + " Street"

print("Meeting time:", meet_time)
print("Meeting place:", place)
