# Create a function called divisible_by_ten() that has one parameter named num.
# The function should return True if num is divisible by 10, and False otherwise. 
# Consider using modulo operator % to check for divisibility.

def divisible_by_ten(num):
    result = num % 10 
    return result == 0
