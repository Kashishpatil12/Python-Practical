#open and write
file1 = open("File/WriteFile.txt","w")
file1.write("Hello I'm Kashish Patil, And u ???")

#open and read the file after the appending:
file1 = open("File/WriteFile.txt","r")
print(file1.read())

file1 =open("File/WriteFile.txt","a")
file1.write("Here...khushi patel, where u from ??")

file1 = open("File/WriteFile.txt","r")
print(file1.read()) 