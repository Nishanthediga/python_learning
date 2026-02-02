#Q1. Write a program to print multiplication table of a given number using for loop.
# n=int(input("Enter a number to print multiplication table: "))
# for i in range(1,11):
#   print(f"{n} X {i} = {n*i}")


#Q2. Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S. 
# l = ["Harry", "Soham", "Sachin", "Rahul"] 
# for i in l:
#   if(i.startswith("S")):
#     print(i)


#Q3. Attempt problem 1 using while loop. 
# n=int(input("Enter a number to print multiplication table: "))
# i=1
# while(i<=10):
#    print(f"{n} X {i} = {n*i}")
#    i+=1


#Q4.Write a program to find whether a given number is prime or not.
# n=int(input("Enter a number to find wheter it is prime or not: "))
# i=2
# isPrime=True
# while(i<n):
  
#   if(n%i==0):
#     isPrime=False
#     break
#   i+=1
# if(isPrime):
#   print("Entered number is a prime")
# else:
#   print("Entered number is not a prime")


#Q5. Write a program to find the sum of first n natural numbers using while loop. 
# n=int(input("Enter a number: "))
# i=1
# sum=0
# while(i<=n):
#   sum+=i
#   i+=1
# print(sum)


#Q6. Write a program to calculate the factorial of a given number using for loop. 
# n=int(input("Enter a number: "))
# fact=1
# for i in range(1,n+1):
#   fact*=i
# print(fact)

#Q7.  Write a program to print the following star pattern. 
#  * 
# *** 
#***** for n = 3 

#Q10.Write a program to print multiplication table of n using for loops in reversed order. 
n=int(input("Enter a number to print multiplication table: "))
l=[10,9,8,7,6,5,4,3,2,1]
for i in l:
  print(f"{n} X {i} = {n*i}")