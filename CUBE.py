def cube(number):
    """
    This function takes a number as input and returns its cube.
    
    Parameters:
    number (int or float): The number to be cubed.
    
    Returns:
    int or float: The cube of the input number.
    """
    return number * number * number

def by_three(number):
    """
    This function checks if a number is divisible by three.
    
    Parameters:
    number (int): The number to be checked.
    
    Returns:
    bool: True if the number is divisible by three, False otherwise.
    """
    if number % 3 == 0:
        return cube(number)
    
    else:
        return False

print(by_three(9))
print(by_three(4))    
