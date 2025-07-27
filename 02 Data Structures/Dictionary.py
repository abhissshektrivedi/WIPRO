#Q1. Write a program to add a key and value to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}
dic={0: 10, 1: 20}
print("Dictionary : ",dic)
dic[2]=30
print("Updated dictionary : ",dic)

#Q2. Write a program to concatenate the following dictionaries to create a new one. 
#Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
print("Dictionary1 : ",dic1)
print("Dictionary2 : ",dic2)
print("Dictionary3 : ",dic3)
new_dic=dic1|dic2|dic3
print("New dictionary : ",new_dic)

#Q3. Write a program to check if a given key already exists in a dictionary.
key=4
dic={1:10,4:20,5:None}
print("Dictionary : ",dic)
if key in dic:
    print(True,key,"is in the dictionary")
else:
    print(False,key,"is not in the dictionary")

#Q4. Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.
dic={1:10,4:20,5:None}
print("Dictionary : ",dic)
print("Keys :",end=" ")
for keys in dic:
    print(keys,end=" ")
print()
print("Values :",end=" ")
for i in dic:
    print(dic[i],end=" ")
print()
print("Keys and Values")
for keys in dic:
    print(keys,end=" ")
    print(dic[keys])

#Q5. Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.
dic={}
for i in range(1,16):
    dic[i]=i*i
print(dic)

#Q6. Write a program to sum all the values in a dictionary, considering the values will be of int type.
sum=0
dic={1:10,2:20,3:30}
print("Dictionary : ",dic)
for keys in dic:
    sum+=dic[keys]
print("Sum of all the values :",sum)