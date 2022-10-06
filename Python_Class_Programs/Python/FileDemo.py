
#File Write
file = open("t1.txt","w")
file.write("This is File Management using python")
file.close()
print("File Written Successfully!")

#File Read
print("*"*50)
file = open("t1.txt","r")
print(file.read())
file.close()
print("*"*50)

#File Append
file = open("t1.txt","a")
file.write("Now this is File Appended")
file.close()
print("File Appended Successfully!")
