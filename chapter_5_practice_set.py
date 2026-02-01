#Q1
# dectionary={
#   "hesaru":"name",
#   "naayi":"dog",
#   "bekku":"cat"
# }

# word=input("Enter a word you want meaning of: ")
# print(f"meaning of enter {word} is:"+dectionary[word])

#Q2
# s=set()
# n=8
# for i in range(n):
#   value=int(input("Enter the value :")) 
#   s.add(value)
# for i in s:
#   print(i)

#Q3
# s={18,"18"}
# print(s)

# #Q4
# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(len(s))#is gives two not three two check this we can compare 20==20.0


#Q5
# s={}
# print(type(s)) <class 'dict'>

#Q6,Q7,Q8
d={}
name=input("Enter your name:")
lang=input("Enter your language")
d.update({name:lang})

name=input("Enter your name:")
lang=input("Enter your language")
d.update({name:lang})

name=input("Enter your name:")
lang=input("Enter your language")
d.update({name:lang})

name=input("Enter your name:")
lang=input("Enter your language")
d.update({name:lang})

print(d)