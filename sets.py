#creating a empty set
e=set()#dont use e={} because it will create a empty dictionary

e.add(10)
e.add(20)
e.add(30)
print(e)
# e.remove(10)
#e.pop()
print(e)

s1={10,20,30,40}
s2={20,30,50,60,70}
s3=s1.union(s2)
print(s3)
s4=s1.intersection(s2)
print(s4)
s5=s1.difference(s2)
print(s5)
