
class Car: 
    def __init__(self, make, model, year): 
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer_reading = 0 
     
    def update_odometer(self, number): 
        if number >= self.odometer_reading: 
            self.odometer_reading = number 
        else: 
            print(f"You can't roll back an odometer.")
    
    def increment_odometer(self, number): 
        self.odometer_reading += number  

    def read_odometer(self): 
        print(f"This car has {self.odometer_reading} km on it.") 

    def get_descriptive_name(self): 
        long_name = f"{self.year} {self.make} {self.model}"  
        return long_name 

    # fill_gas_tank >>> Tank is now full. 
    def fill_gas_tank(self): 
        print("Tank is now full!") 



class Battery: 
    def __init__(self, battery_size=40):
        self.battery_size = battery_size 
        self.battery_duration = 120  

     
    def get_range(self): 
        if self.battery_size ==40: 
            range = 150 
        elif self.battery_size == 65: 
            range = 225 
        print(f"This car can go about {range}kmh on full charge.") 

    def describe_battery(self): 
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}kwh battery") 





class ElectricCar(Car):  
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  
   

    def fill_gas_tank(self):
        print("This car does not have a gas tank.") 



my_electric_car = ElectricCar("nissan", "leaf", 2024)
print(my_electric_car.battery.get_range())  



# my_new_car = Car("Audi", "a4", 2024) 
# print(my_new_car.get_descriptive_name()) 
# print(my_new_car.read_odometer()) 
# my_new_car.update_odometer(50000) 
# print(my_new_car.read_odometer()) 
# my_new_car.increment_odometer(20) 
# print(my_new_car.read_odometer())