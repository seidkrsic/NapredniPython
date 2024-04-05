

# racunamo drugu kolika mu je plata 
# 15e po satu 
# placa porez od 12% 
# on nama govori koliko je sati radio 

"""
12% od 200 = 12/100 * 200 
0.12 * plata 
"""

def get_pay(num_of_hours):  
    pay_pretax = num_of_hours * 15 
    tax = pay_pretax * 0.12 
    pay = pay_pretax - tax 
    return pay 


result = get_pay(40)  
print(result) 