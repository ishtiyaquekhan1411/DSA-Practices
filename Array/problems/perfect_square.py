# Given a positive integer num, write a program that returns True if num is a perfect
# square else return False. Do not use built-in functions like sqrt. Also, talk about the time
# complexity of your code.
# Test Cases:
# Input: 16
# Output: True
# Input: 14
# Output: False

# Method Implementation
def perfectSquare(number):
  if number < 2:
    return True
  
  # Initialize iteration from 1 to half of number, as sqrt can not be more than n/2.  
  start = 1
  end = number // 2

  while start <= end:
    mid = start + (end - start)//2
    sqrt = mid * mid

    if sqrt == number:
      return True
    elif sqrt < number:
      start = mid + 1
    else:
      end = mid - 1
  return False

# Driver Code
number = int(input("Enter number:"))
result = perfectSquare(number)
print('The number is perfect square:', result)