# Compute and return the square root of x, where x is guaranteed to be a non-negative
# integer. And since the return type is an integer, the decimal digits are truncated and only
# the integer part of the result is returned. Also, talk about the time complexity of your
# code.
# Test Cases:
# Input: 4
# Output: 2
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.8284...., the decimal part is truncated and 2 is
# returned.
# Hint: Try to use a modified binary search approach for an optimized solution

# Method Implementation
def squareRoot(number):
  if number < 2:
    return number

  # To store the result.
  result = 0

  # Initialize iteration from 1 to half of number, as sqrt can not be more than n/2.  
  start = 1
  end = number // 2

  # Whole number (Square root)
  while start <= end:
    mid = (start + end)//2
    sqrt = mid * mid

    # return `mid` if `x` is a perfect square
    if (sqrt == number):
      return mid
    # if `mid×mid` is less than `number`
    elif sqrt < number:
      # discard left search space
      start = mid + 1
      # update result to store floor
      result = mid
    # # if `mid×mid` is more than `number`
    else:
      # discard the right search space
      end = mid - 1
    
  return result

# Driver Code
number = int(input("Enter number:"))
result = squareRoot(number)
print('The square root of number', number,  'is', result)