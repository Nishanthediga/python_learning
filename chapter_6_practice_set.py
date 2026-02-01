# Q1
# a=int(input("Enter a 1st number:"))
# b=int(input("Enter a 2st number:"))
# c=int(input("Enter a 3st number:"))
# d=int(input("Enter a 4st number:"))
# if(a>b and a>c and a>d):
#   print(f"{a} is the greatest number")
# elif(b>a and b>c and b>d):
#   print(f"{b} is the greatest number")
# elif(c>a and c>b and c>d):
#   print(f"{c} is the greatest number")
# else:
#   print(f"{d} is the greatest number")


#Q2
# marks1=int(input("Enter a marks1:"))
# marks2=int(input("Enter a marks2:"))
# marks3=int(input("Enter a marks3:"))
# total_percentage=((marks1+marks2+marks3)/300)*100
# print(total_percentage)

# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 ):
#   print("your passed in the exam")
# else:
#   print("try next year")

#Q3
# p1="Make a lot of money"
# p2="buy now"
# p3="subscribe this"
# p4="click this"

# message=input("Enter your comment:")
# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#   print("This comment is a spam")
# else:
#   print("This comment is not a spam")

#Q3
# username=input("Enter the user name:")
# if(len(username)<10):
#   print("invalid username")
# else:
#   print("valid username")

#Q4
# l=["rohan","piyush","samarth","arya"]
# name=input("enter your name:")
# if(name in l):
#   print("Your name is recorded")
# else:
#   print("Your name is not recorded")

#Q6
post=input("Enter your post:")
if("Harry".lower() in post.lower()):
  print("This post is talking about Harry")
else:
  print("This post is not talking about Harry")