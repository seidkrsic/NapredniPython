""" 
1. Restaurant: Make a class called Restaurant. 
The __init__() method for Restaurant should store two attributes: 
a 
restaurant_name 
and a 
cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of 
information, and a method called open_restaurant() that prints a message 
indicating that the restaurant is open.
Make an instance called restaurant from your class. 
Print the two attributes individually, and then call both methods.
"""

class Restaraunt: 
    def __init__(self,restaurant_name,cuisine_type): 
        self.restaraunt_name = restaurant_name 
        self.cuisine_type = cuisine_type 
        self.number_served = 0 
    
    def set_number_served(self, number): 
        self.number_served = number 

    def increment_number_served(self, number): 
        self.number_served += number  


    def describe_restaurant(self): 
        print(f"{self.restaraunt_name} with {self.cuisine_type}")

    def open_restaurant(self): 
        print(f"{self.restaraunt_name} is open now.")


class IceCreamStand(Restaraunt): 
    """Implementation of IceCreamStand type of restaraunt""" 

    def __init__(self, restaurant_name, cuisine_type, flavours):
        super().__init__(restaurant_name, cuisine_type)
        # self.flavours = ["vanilla", "strawberry", "lemon"] 
        self.flavours = flavours

    def display_flavours(self):
        """Here we print flavours"""
        for flavour in self.flavours: 
            print(flavour) 


iceCreamStand = IceCreamStand("Slatka Magija","ICE CREAMSSSS", ["vanilla", "strawberry", "lemon"] ) 
iceCreamStand.display_flavours() 


restoran1 = Restaraunt("ASTORIA", "Italian Food") 
print(restoran1.cuisine_type)
restoran1.open_restaurant()
restoran1.describe_restaurant()
# # create restaraunt 
# restoran2 = Restaraunt("Rostiljijada", "Local Food") 
# # describe restaraunt 
# restoran2.describe_restaurant() 
# restoran2.open_restaurant()





