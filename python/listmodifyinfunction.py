#Lsit addition in function 
sum1=0
def AddList(mylist):
	"This is for addition of list into this function"
	mylist[0]=9
	mylist.append([1,2,3,4]);		
	return mylist
	
list = [1,2,3,4,5,6,7]
sum1=AddList(list)
print("SUM of LIST : ",sum1)
