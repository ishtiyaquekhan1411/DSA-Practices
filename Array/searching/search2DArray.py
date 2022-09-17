# Function definition
def search2DArray(array, target):
  ## Number of rows
  rows = len(array)
  if rows == 0:
    return False
  ## number of columns
  columns = len(array[0])
  left, right = 0, rows * columns - 1
  ## binary search implementation
  while (left <= right):
    mid = left + (right - left)//2
    ## row_number -> mid//n
    ## column_number -> mid%n
    mid_element = array[mid//columns][mid%columns] # [row number][column number]
    if mid_element == target:
      return (mid//columns, mid%columns)
    elif mid_element > target:
      right = mid - 1
    else:
      left = mid + 1
  return False

## Driver Code
array = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
result = search2DArray(array, target)
print("Find element location", result)

# Optimized solution Time Complexity: Big-oh(log m*n) - depends on 2 values
# Brute force approach: linear search Big-oh(m*n) < Log m*n