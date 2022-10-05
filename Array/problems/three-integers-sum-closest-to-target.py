"""
Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to the target.[Amazon]

You need to return the sum of three integers.
For example:arr = [-1, 2, 1, -4], target = 1
Output: 2
Explanation: [-1+2+1] = 2 (The sum that is closest to the target is 2)
"""
import sys

# Method Implementation (Using two pointers solution)
# Time complexity: O(N^2) => two nested loop (for and while loops)
# Space complexity: O(1) => no extra space needed
def findTripletSum(array, target):
  # First sort the array
  array.sort();

  # Initial max closest sum.
  closestSum = sys.maxsize

  for i in range(len(array) - 2):
    # First pointers fixed to next of current fixed element index.
    start = i + 1
    # Last pointers fixed to last element index.
    end = len(array) - 1

    while start < end:
      # Sum of current element and pointers elements.
      sum = array[i] + array[start] + array[end]

      # If different between target and sum is less than difference between target and closest sum, update closest sum.
      if abs(target - sum) < abs(target - closestSum):
        closestSum = sum
      # If sum is greater than target, decrease last pointer.
      elif sum > target:
        end -= 1
      # Otherwise, increate the first pointer.
      else:
        start += 1

  return closestSum
# Driver Code
array = [-1, 2, 1, -4]
target = 1
result = findTripletSum(array, target)
print("Closest sum of three integers are", result)