## Find 2 element from array whose sum is equal to given number.
## Solved by greedy-approach(two pointers appraoch) big-oh(n)
# Other approaches are linear approach (big-oh(n^2)) or (linear + binary search) big-on(nlogn)

def find_two_number_of_target_sum(array, target_sum):
  left = 0
  right = len(array) - 1

  while left <= right:
    if array[left] + array[right] == target_sum:
      # Element found
      return (array[left], array[right])
    elif array[left] + array[right] > target_sum:
      right -= 1
    else:
      left += 1
  # Element not found
  return (-1, -1)

# Driver code
array = [20, 40, 60, 80, 90, 120, 240]
target_sum = 210
result = find_two_number_of_target_sum(array, target_sum)
print("Two numbers of taget sum is:", result)

# Time Complexity: Big-oh(n)
# Brute Force approach: Big-oh(n^2) < Big-oh(nlogn) < Big-oh(n)