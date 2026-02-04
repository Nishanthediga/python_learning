# from typing import List,Union,Tuple,Dict 
# n:int=10
# name:str="Nishanth"

# def sum(a:int,b:int)->int:
#   return a+b

#match case
def http_server(status):
  match status:
    case 200:
      return "OK"
    case 404:
      return "Not found"
    case 500:
      return "Internal Server Error"
    case _:
      return "Unknown status"
    
print(http_server(404))
print(http_server(600))



