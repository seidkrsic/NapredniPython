

def elementwise_greater_than(L, tresh): 
    """ 
    elementwise_greater_than([1,2,3,4,5], 2)
    [False, False, True, True, True] 

    """
    result_list = [] 
    for element in L: 
        if element > tresh: 
            result_list.append(True)
        else: 
            result_list.append(False) 
    
    return result_list

result = elementwise_greater_than([1,2,3,4,5], 2) 
print(result) 

