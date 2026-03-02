import numpy as np

def FizzBuzz(start, finish):
    numbers = np.arange(start, finish + 1)
    
    # Create boolean masks
    fizz = numbers % 3 == 0
    buzz = numbers % 5 == 0
    
    # Initialize result as string version of numbers
    result = numbers.astype(object)
    
    # Apply FizzBuzz logic using vectorized masking
    result[fizz & buzz] = "fizzbuzz"
    result[fizz & ~buzz] = "fizz"
    result[~fizz & buzz] = "buzz"
    
    return result.tolist()
