# Method Implementation
def bubbleSort(array):
  n = len(array)
  for i in range(n):
    # range 0 - n - i - 1 to exclude last elements in each iterations.
    for j in range(0, n-i-1):
      if array[j] > array[j+1]:
        # Swap happens
        array[j], array[j+1] = array[j+1], array[j]
  return array

# Driver code
array = [20, 50, 30, 70, 13, 5, 90]
result = bubbleSort(array)
print("Array after bubble Sort array is:", result)

# Time complexity: big-oh(n^2)
# Time complexity: comparisions + swaps => n^2 + n^2 = n^2
# Comparisions: (n-1) + (n-2) + (n-3) ...... 1 => ((n-1)*n)/2 => n^2
# Swaps(worst-case): (n-1) + (n-2) + (n-3) ...... 1 => ((n-1)*n)/2 => n^2

# Algorithm:
# Run a nested for loop to traverse the input array using two variables i and j, such that 0 ≤ i < n-1 and 0 ≤ j < n-i-1
# If arr[j] is greater than arr[j+1] then swap these adjacent elements, else move on
# Print the sorted array