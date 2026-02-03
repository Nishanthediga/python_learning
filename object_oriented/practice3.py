class TwoVector:
  def __init__(self,i,j):
    self.i=i
    self.j=j
  
  def show(self):
    print(f"The vector is {self.i}i + {self.j}j")
    
class ThreeVector(TwoVector):
  def __init__(self,i,j,k):
    super().__init__(i,j)
    self.k=k
    
  def show(self):
    print(f"The vector is {self.i}i + {self.j}j + {self.k}k")
    
a=TwoVector(2,4)
b=ThreeVector(5,4,7)
a.show()
b.show()