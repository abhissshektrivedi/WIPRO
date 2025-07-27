#Q1. Write a program to create a list of 5 integers and display the list items. Access individual elements through index.
list=[1,2,3,4,5]
print("My list is :",list)
print("Accessing individual elements.....")
print("Index 0 :",list[0])
print("Index 1 :",list[1])
print("Index 2 :",list[2])
print("Index 3 :",list[3])
print("Index 4 :",list[4])

#Q2. Write a program to append a new item to the end of the list.
list=[1,2,3,4,5]
print("My list is :",list)
print("Now appending 6 to the end of the list...")
list.append(6)
print("Now list is :",list)

#Q3. Write a program to reverse the order of the items in the list.
list=[1,2,3,4,5]
print("My list is :",list)
list.reverse()
print("Reverse order list :",list)

#Q4. Write a program to print the number of occurrences of a specified element in list.
list=[1,2,3,4,5,3,2]
e=input("Enter the element : ")
if e.isdigit():
    e=int(e)
print("My list is :",list)
print("Number of occurrences of a specified element",list.count(e))

#Q5. Write a program to append the items of list1 to list2 in the front.
list1=[1,2,3,4,5,3,2]
list2=[12,43,54,76,89,3.45]
print("list1 is :",list1)
print("list2 is :",list2)
new_list=list1+list2
print("New list :",new_list)

#Q6. Write a program to insert a new item before the second element in an existing list.
list=[1,2,3,4,5]
print("list is :",list)
list.insert(1,"new")
print("new list :",list)

#Q7. Write a program to remove the item from a specified index in a list.
list=["a","b","c","d","e"]
print("list is :",list)
e=int(input("Index : "))
list.pop(e)
print("new list :",list)

#Q8. Write a program to remove the first occurrence of a specified element from a list.
list=[1,2,3,4,5,2]
print("list is :",list)
list.remove(2)
print("new list :",list)
