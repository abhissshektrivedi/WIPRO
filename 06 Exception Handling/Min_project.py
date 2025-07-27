# Mini Project
"""
You had saved the items and their price details in a text file, which you purchased yesterday from a nearby super market.

You need to know:
1. How many items did you purchase?
2. How many items are free?
3. What is the total amount you had to pay?
4. What is the discount amount?
5. What is the final amount did you pay after the discount?

Help yourself by writing a python code to do this. Include necessary code to handle the possible exceptions.

Note:
Data is stored in a text file Purchase-1.txt.
Each line contains one item's details.
Item name and price is separated by a space.
You have to enter the file name during run time.
"""
filename = input("Enter the file name: ") + ".txt"

try:
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    purchased = 0
    free = 0
    amount = 0
    discount = 0
    section = 1

    for line in lines:
        line = line.strip()
        if line == "":
            section += 1
            continue
        parts = line.split()
        if section == 1:
            price = parts[-1]
            if price.lower() != "free":
                amount += int(price)
                purchased += 1
        elif section == 2:
            if parts[-1].lower() == "free":
                free += 1
        elif section == 3:
            discount = int(parts[-1])

    final = amount - discount

    print("No of items purchased:", purchased)
    print("No of free items:", free)
    print("Amount to pay:", amount)
    print("Discount given:", discount)
    print("Final amount paid:", final)

except:
    print("Error: Cannot open file")
