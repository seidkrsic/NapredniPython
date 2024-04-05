


def get_pay_with_more_inputs(num_of_hours, hourly_wage, tax_bracket): 
    pay_before_tax = num_of_hours * hourly_wage 
    tax = tax_bracket/100 * pay_before_tax 
    pay = pay_before_tax - tax 
    return pay 

result = get_pay_with_more_inputs(32, 20, 12) 
print(result) 
