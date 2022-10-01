# Method of implementation
def powerOfNumber(number, power):
  if power == 1:
    return number
  elif power == 0:
    return 1
  else:
    mid = power//2
    small_result = powerOfNumber(number, mid)
    result = small_result * small_result
    if power % 2 == 0:
      return result
    else:
      return result * number

# Drive code
number = 2
power = 5
result = powerOfNumber(number, power)
print("result for power of number is", result)