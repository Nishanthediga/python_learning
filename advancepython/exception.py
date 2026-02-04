# try:
#   a=int(input("Enter a number to print"))
#   b=int(input("Enter a another number"))
#   print(a/b)
# except ValueError as v:
#   print(v)
# except Exception as e:print(e)

# a=int(input("Enter a number to print"))
# b=int(input("Enter a another number"))

# if(b==0):
#   raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
# else:
#   print(a/b)
  
# print("Hello world")
def fun():
  try:
    a=int(input("Enter a number to print"))
    b=int(input("Enter a another number"))
    print(a/b)
    return
  
  except ValueError as v:
    print(v)
    return
  except Exception as e:
    print(e)
    return
  finally:
    print("I am inside the finally block")
fun()

