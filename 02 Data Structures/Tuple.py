#Q1. Write a program to print the 4th element from first and 4th element from last in a tuple.
tup=(1,2,3,4,5,6,7,8,9,10)
print("Tuple :",tup)
if len(tup)>=4:
    print("4th element from first :",tup[3])
    print("4th element from last :",tup[-4])
else:
    print("Your tuple is smaller than 4 elements")

#Q2. Write a program to check whether an element exists in a tuple or not.
tup=(1,2,3)
element=4
print("Tuple :",tup)
print(element,"is in tuple or not :",element in tup)

#Q3. Write a program to convert a list into a tuple.
list=[1,2,3]
print(list,type(list))
print("--- Converting list into tuple ---")
tup=tuple(list)
print(tup,type(tup))

#Q4. Write a program to find the index of an item in a tuple.
element=38
tup=(1,2,3,4,38,25,13,41,56,73,42,35)
print(tup)
if element in tup:
    print(element,"is in index :",tup.index(element))
else:
    print("element is not found in the tuple")

#Q5. Write a program to replace last value of tuples in a list to 100.
#Sample list: [(10, 20, 40), (40, 50, 60), (78, 80, 90)]
#Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
l=[(10, 20, 40), (40, 50, 60), (78, 80, 90)]
l1=[]
print("Original :",l)
for tup in l:
    tup=list(tup)
    tup.pop()
    tup.append(100)
    tup=tuple(tup)
    l1.append(tup)
print("New :",l1)