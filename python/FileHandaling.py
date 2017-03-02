#file handling 

# Open a file
file = open("word.txt", "r+")
print("Name of the file: ", file.name)

str = file.read(20)
print("Reading file  : ", str)

file.write("Hello world from the write method")
file.write("tesrt the file writing")

file.seek(0)
str = file.read(30)
print("Reading file  : ", str)


# Close opend file
file.close()