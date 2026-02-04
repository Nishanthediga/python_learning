# try:
#   with open("1.tx","r") as f:
#     print(f.read)
#   with open("2.txt","r") as f:
#     print(f.read())
#   with open("2.txt","r") as f:
#     print(f.read())
    
# except Exception as e:
#   print(e)

list=[1,2,3,4,5,6]
for index,l in enumerate(list):
  if(index==0 or index==2 or index==4):
    print(l)