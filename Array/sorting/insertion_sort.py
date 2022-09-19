# Method Implementation
def insertionSort(array):
  n = len(array)
  for i in range(1, n):
    key = array[i]
    j = i - 1
    while (j >= 0) and (key < array[j]):
      array[j+1] = array[j]
      j -= 1
    array[j+1] = key
  return array

# Driver code
array = [20, 50, 30, 70, 13, 5, 90]
result = insertionSort(array)
print("Array after selection Sort array is:", result)

# Time complexity: (Comparisions + Swaps)
# Best case scenario: O(n-1) + 0 => O(n)
# Worst case scenario: n(n-1)/2 => n^2-n/2 => O(n^2)

# Algorithm:
# Iterate from arr[1] to arr[N] over the array. 
# Compare the current element (key) to its predecessor. 
# If the key element is smaller than its predecessor, compare it to the elements before.
# Move the greater elements one position up to make space for the swapped element.
