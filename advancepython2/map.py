
from functools import reduce

#map example
l=[1,2,3,4]
square=lambda x:x*x
sqrList=map(square,l)
print(list(sqrList))#it not directly return the list we need to covert it to list

#filter exaple
def even(n):
  if(n%2==0):
    return True
  return False
lst=[1,2,3,4,5,6,7,8,9,10]
onlyEven=filter(even,lst)
print(list(onlyEven))

#reduce example
def sum(a,b):
  return a+b

print(reduce(sum,lst))

def divisibleBy5(n):
  if(n%5==0):
    return True
  return False

lst=[12,34,55,67,30,60,75,90]
result=filter(divisibleBy5,lst)
print(list(result))

def greater(a,b):
  if(a>b):
    return a
  return b
ans=reduce(greater,lst)#it returns a single value
print(ans)


