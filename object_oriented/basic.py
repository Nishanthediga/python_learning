class Car:
  total_car=0
  def __init__(self,brand,model):
    self.__brand=brand
    self.model=model
    Car.total_car+=1
  def fullName(self):
    return f"{self.__brand} {self.model}"
  def get_brand(self):
    return self.__brand
  @staticmethod
  def general_description():
    return "Cars are means of general transportation"

class ElectricCar(Car):
  def __init__(self,brand,model,battery_seze):
    self.battery_size=battery_seze
    super().__init__(brand,model)
    
# my_car=Car("Toyota","Corolla") 
# print(my_car.fullName())

# my_car=ElectricCar("Tesla","Model S","85kWH")
# my_car.brand="Toyota"
# print(my_car.fullName())
# print(my_car.get_brand())

test1=ElectricCar("Tesla","Model S","85kWH")
safari=Car("Tata","safari")
suzuki=Car("Maruthi","suzuki")

print(Car.total_car)
print(Car.general_description())

print(isinstance(test1,Car))
print(isinstance(test1,ElectricCar))