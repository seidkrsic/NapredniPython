

class Dog: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    
    def sit(self): 
        print(f"{self.name} is now sitting.") 

    def roll_over(self): 
        print(f"{self.name} rolled over.")
 
dog1 = Dog("Willie", 6) 
print(dog1.name)  
dog1.sit() 
dog1.roll_over()