
def has_lucky_number(nums): 
    """ 
    returns if a functions has at least one element divisible by 7. 
    Returns True or False 
    """
    for num in nums: 
        if num % 7 == 0: 
            return True 
    
    return False 


result = has_lucky_number([1,2,3,4,5]) 
print(result) 