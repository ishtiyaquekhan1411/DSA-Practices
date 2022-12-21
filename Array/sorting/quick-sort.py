# Algorithm
# 1. Select pivot and rearrange it using partitions in such a way that elements less than pivot should be on left side and greater than should be on right side.
# 2. Divide Array in subarrays of left elements from pivot and right elements from pivot.
# 3. Divide the array in subarrays considering the first step until we get subarrays containing single element in subarrays.
# 4. After the process gets completed the array will be sorted.

# Method Implementation
def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if (array[j] <= pivot):
      i += 1
      array[j], array[i] = array[i], array[j]

  array[i+1], array[high] = array[high], array[i+1]
  return i+1

def quickSort(array, low, high):
  if low < high:
    pivot = partition(array, low, high)

    quickSort(array, low, pivot - 1)
    quickSort(array, pivot + 1, high)

# Driver Code
array = [20, 50, 30, 70, 13, 5, 90, 45]
size = len(array)
quickSort(array, 0, size - 1)
print("Array after quick Sort array is:", array)

# Algorithm:
# Divide + Conquer + Combine => O(n) + Recurrence Relation (left subarray i + right subarray n - i - 1) + O(1)
# => T(i) + T(n - i - 1) + O(n) => T(i) + T(n - i - 1) + cn
# Recurrence relation: T(n) = T(i) + T(n - i - 1) + cn where T(n) = c -> if n = 1
#
# 1. Worst case scenario:
# In worst case scenario (sorted array), we will have to divide array in subproblem where one subproblem will have n - 1 elements and other with 0 elements.
# T(n - 1) + T(0) + cn where i = 0 for other subproblem.
# After solving with substitution => c(n(n+1)/2) = O(n^2)
#
# 2. Best case scenario:
# T(n) = T(n/2) + T(n - 1 - n/2) + cn
# T(n/2) + T(n - 1 - n/2) + cn => 2T(n/2) + cn => O(nlogn)
#
# 3. Average case scenario:
# O(nlogn)