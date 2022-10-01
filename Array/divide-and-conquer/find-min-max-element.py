# Method Implementation
# Brute force approach: O(n^2) or O(n^2)
# Recurrence relation: T(n/2) + c
# Time Complexity: O(n)
def findMinMaxElement(arr, start, end):
  # Base scenario for small case.
  if start == end:
    min_value = arr[start]
    max_value = arr[start]
  elif start == end - 1:
    if arr[start] < arr[end]:
      min_value, max_value = arr[start], arr[end]
    else:
      min_value, max_value = arr[end], arr[start]
  # Big case (divide & conquer).
  else:
    # Divide the problem
    mid = start + (end - start)//2

    # Conquer result
    min1_value, max1_value = findMinMaxElement(arr, start, mid)
    min2_value, max2_value = findMinMaxElement(arr, mid+1, end)

    if min1_value < min2_value:
      min_value = min1_value
    else:
      min_value = min2_value
    if max1_value > max2_value:
      max_value = max1_value
    else:
      max_value = max2_value
  
  # Return min and max value
  return (min_value, max_value)
## Driver code
arr = [20, 19, 45, 65, 21, 44, 89, 92]
# Start index of array
start = 0
# End index of array
end = len(arr) - 1
result = findMinMaxElement(arr, start, end)
print("Min and Max value is", result)