file = open("t2.txt","w+")
file.write("This is File Write/Read Operation using W+")
print("File Pointer Current Position :",file.tell())
file.seek(10)
print(file.read())
file.close()
print("*"*59)
