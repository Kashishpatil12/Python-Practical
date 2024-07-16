
# file1 = open("File/file.txt","w")
# file1.write("Hello Python")
# 
# print("--------------------------------")
# file2 = open("File/file2.txt","r")
# print(file2.read())
# 
# print("--------------------------------")
# file1 = open("File/file.txt","r")
# print(file1.read(10))
# 
# print("--------------------------------")
# file3 = open("File/file3.txt","w")
# file3.write("Hello Everyone \n Hope you all are fine \n What are u doing ???")

# print("--------------------------------")
# file4 = open("File/file3.txt","r")
# x =(file4.readlines())
# print(x[2])

file4 = open("File/file3.txt","a")
file4.write("ram \n")
file4.write("shyam \n")
file4.write("gita \n")

file4 = open("File/file3.txt","r")
print(file4.read())



