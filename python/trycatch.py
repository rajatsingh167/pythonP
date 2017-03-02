#try catch finally 
import sys, traceback
try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")
   fh.close()
   
   
try:
  x=5
  y=x/0;
except ZeroDivisionError:
   print("Error: cant devide by 0" , sys.exc_info())
except IndexError:
	print("Error: IndexError")
else:
   print("after divide : ",y)
