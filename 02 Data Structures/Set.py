#Q1. Write a program to remove a given item from the set.
element=260
s={45,34,4,26,67}
print("Original :",s)
if element in s:
    s.remove(element)
    print("Modified :",s)
else:
    print(element,"is not present in set")

#Q2. Write a program to create an intersection of sets.
s1={45,34,44,26,67}
s2={2,3,6,1,9,5,26}
print("Set 1 :",s1)
print("Set 2 :",s2)
print("Intersection of Set 1 and Set 2 :",s1.intersection(s2))

#Q3. Write a program to create an union of sets.
s1={45,34,44,26,67}
s2={2,3,6,1,9,5,26}
print("Set 1 :",s1)
print("Set 2 :",s2)
print("Union of Set 1 and Set 2 :",s1.union(s2))

#Q4. Write a program to find the maximum and minimum value in a set.
s={45,34,44,26,67}
print("Set :",s)
if len(s)>=1:
    print("Maximum value in the set :",max(s))
    print("Minimum value in the set :",min(s))
else:
    print("Your set is empty")