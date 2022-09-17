# Time complexity: O(n)
# Space Complexity: O(1) - because we have finite array elements which doesn't depends on n input.
# Defined method linearSearch
def linearSearch(array, element):
  for i in range(len(array)):
    # element found
    if array[i] == element:
      return i
  # No element found
  return -1

# Driver code
array = [20, 45, 27, 47, 55, 67, 75, 88, 90] # List in python
element = 6
# Function calling
result = linearSearch(array, element)
# printing result
print("Searching element is present at index:", result)