""" 
Problem 2. 
You are thinking about buying a home and want to get an idea of how 
much you will spend, based on the number of bedrooms and bathrooms. 
You are trying to decide between four different options:

Option 1: house with two bedrooms and three bathrooms
Option 2: house with three bedrooms and two bathrooms
Option 3: house with three bedrooms and three bathrooms
Option 4: house with three bedrooms and four bathrooms
Use the get_expected_cost() function you defined in question 1 to 
set option_1, option_2, option_3, and option_4 to the expected cost of each option. 
"""
from problem1 import get_expected_cost 

option1 = get_expected_cost(2,3) 
option2 = get_expected_cost(3,2)
option3 = get_expected_cost(3,3)
option4 = get_expected_cost(3,4) 
print(f"Najjeftinija kuca je: {min(option1, option2,option3,option4)}") 
