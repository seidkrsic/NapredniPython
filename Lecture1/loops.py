
"""
Petlje --- loops 

for -  petlja 
while - petlja 

""" 

# lista 

planets = ["Mercury", 
           "Venus", 
           "Earth", 
           "Mars", 
           "Jupiter", 
           "Saturn",       
           "Uranus", 
           "Neptune"     
]   

for planet in planets: 
    print(planet, end=" ")

# set 
numbers = (2, 2, 2, 2, 3, 3, 5)  
result = 1 
for num in numbers: 
    result = result * num  # result *= num  

print(result) 

