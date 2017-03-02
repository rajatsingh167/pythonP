#CRUD on List 

#Creation of List
list = ['physics', 'chemistry', 1997, 2000]

#Reading List
print(list[0])
print(list)

#Updatiopn
list[2] = 2001;
print(list)

list.append(10000)

print("after appending list",list)


#Deleting 
del list[2];
print("after Deleting list[2] years list",list)

#Reverse the list
list.reverse()
print("after reverse the list",list)


# CRUD on Dictonary

#Creation of Dictonary 
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict2 = {'Name1': 'RAM', 'Age': 12}

print("Dictonary All items ", dict.items())

#Updatiopn
dict['Name']="Rajat"
dict['Age']=25

print("After updating",dict.items())

dict1 =dict.copy();
print("Copy of dict ", dict1)

dict.update(dict2);
print("After Updating Dictonary",dict);

#Deleting 
del dict['Name']; 
print("After Deleting ",dict.items())

dict.clear();     # remove all entries in dict
print("After clearing all value ",dict.items())

dict1 =dict.copy();
print("Copy of dict ", dict1)

