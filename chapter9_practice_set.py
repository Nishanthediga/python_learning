#Q1
# f=open("poem.txt","r")
# poem=f.read()
# if(poem.find("twinkle")!=-1):
#     print("Yes, the word 'twinkle' is present in the poem.")
# f.close()


#Q2
# def generateTable(n):
#   table=""
#   for i in range(1,11):
#     table+=f"{n} x {i} = {n*i}\n"
#   with open(f"tables/table_{n}.txt","w") as f:
#     f.write(table)
    
  
# for i in range(2,21):
#   generateTable(i)

#Q3
# with open("donkey.txt","r") as f:
#     content=f.read()
# newContent=content.replace("donkey","######")
# with open("donkey.txt","w") as f:
#     f.write(newContent)
    
#Q4
words=["donkey","strong","animal","careful"]
with open("donkey.txt","r") as f:
    content=f.read()
for word in words:
  content=content.replace(word,"#"*len(word))
with open("donkey.txt","w") as f:
    f.write(content)