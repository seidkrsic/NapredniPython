

def count_negatives(nums):
    """ 
    Returns the number of negative numbers
    For input [-1,2,-3, 5,6] >>> returns 2  
    """
    count = 0 
    for num in nums: 
        if num < 0: 
            count += 1 
    return count 



result = count_negatives([-1, 2, -3, 4, 5])  
print(result) 

