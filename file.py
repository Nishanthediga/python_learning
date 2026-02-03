# f=open("this.txt","r")#open() function return the file object
# text=f.read()
# print(text)
# f.close()

#we can also print the characters of the file by specifying the number of characters to be read
# f=open("this.txt","r")#open() function return the file object
# text=f.read(10)
# print(text)
# f.close()


# f=open("this.txt","r")
# text=f.readline()#it will read only one line
# print(text) 
# text=f.readline()#it will read only one line
# print(text)
# f.close()


# with open("this.txt","r") as f:#using with statement we dont need to close the file
#   text=f.read()
#   print(text)

# f=open("this2.txt","wt")#it will overwrite the existing content and if file not exist it will create a new file
# f.write("I am writing this line to the file\n")
# f.close()

# f=open("this2.txt","at")#it will append the content to the existing file
# f.write("I am appending this line to the file\n")
# f.close()