""" 
Problem 1. 
In the House Prices - Advanced Regression Techniques competition, 
you need to use information like the number of bedrooms and bathrooms 
to predict the price of a house. Inspired by this competition, 
you'll write your own function to do this.

In the next code cell, create a function get_expected_cost() 
that has two arguments:

beds - number of bedrooms
baths - number of bathrooms
It should return the expected cost
of a house with that number of bedrooms and bathrooms. Assume that:

the expected cost for a house with 0 bedrooms and 0 bathrooms is 80000.
each bedroom adds 30000 to the expected cost
each bathroom adds 10000 to the expected cost.
For instance,

a house with 1 bedroom and 1 bathroom has an expected 
cost of 120000, and
a house with 2 bedrooms and 1 bathroom has an 
expected cost of 150000.

"""
# 80000 start paket 

def get_expected_cost(beds=0, baths=0): 
    cost = 80000 + beds*30000 + baths*10000 
    return cost 

result = get_expected_cost(3,2) # 80000 
print(result) 


