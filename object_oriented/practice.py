class Programmer:
  company="Microsoft"
  def __init__(self,name,salary,pin):
    self.name=name
    self.salary=salary
    self.pin=pin

p=Programmer("Nish",100000,8277)
print(p.name,p.salary,p.pin,p.company)

r=Programmer("Rish",100000,7277)
print(r.name,r.salary,r.pin,r.company)