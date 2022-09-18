# Method Implementation
def selectionSort(array):
  n = len(array)
  for i in range(n):
    min_idx = i
    # Range from i + 1 to n
    for j in range(i+1, n):
      if array[j] < array[min_idx]:
        min_idx = j
    # Swaps after every pass
    array[i], array[min_idx] = array[min_idx], array[i]
  return array

# Driver code
array = [20, 50, 30, 70, 13, 5, 90]
result = selectionSort(array)
print("Array after selection Sort array is:", result)
