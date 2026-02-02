#Q1.

# def greatest(a,b,c):
#   if(a>b and a>c):
#     return a
#   elif(b>a and b>c):
#     return b
#   else:
#     return c
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# c=int(input("Enter a number"))
# max=greatest(a,b,c)
# print(max)

# #Q3
# print("Nishanth ",end="")
# print("H O")

# def fun(n):
#   if(n==0):
#     return 0
#   return n+fun(n-1)
# n=int(input("Enter a number: "))
# print(fun(n))

# print("*"*6)

#Q5
def pattern(n):
  if(n==0):
    return 
  print("*"*n)
  pattern(n-1)
  
pattern(8)