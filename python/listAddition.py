#Lsit addition in function 
sum1=0
def AddList(mylist):
	"This is for addition of list into this function"
	sum=0
	for index in mylist:
		sum= sum + index
			
	return sum
	
list = [1,2,3,4,5,6,7]
sum1=AddList(list)
print("SUM of LIST : ",sum1)
