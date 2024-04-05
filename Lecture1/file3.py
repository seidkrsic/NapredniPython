
i = 1 
while i<=10: 
    print(i, end=" ") 
    i = i + 1 
for i in range(1,11): 
    print(i, end=" ")

"""
# brojeve od 1 do 10 
i = 1 
while i<=10: 
    print(i, end=" ") 
    i = i + 1 

# koristeci for petlju 
    
for i in range(1,11): 
    print(i, end=" ") 

"""
planets = ["Mercury", 
           "Venus", 
           "Earth", 
           "Mars", 
           "Jupiter", 
           "Saturn",       
           "Uranus", 
           "Neptune"     
] 
# .append() 

short_planets = [] 
for planet in planets: 
    if len(planet) < 6: 
        planet = planet.upper() + "!" 
        short_planets.append(planet)

print(short_planets) # [VENUS!, "EARTH!", "MARS!"] 

