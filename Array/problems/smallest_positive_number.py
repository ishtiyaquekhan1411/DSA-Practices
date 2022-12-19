def segregate(numbers, size):
  initial_index = 0
  for number_index in range(size):
    if numbers[number_index] <= 0:
      numbers[initial_index], numbers[number_index] = numbers[number_index], numbers[initial_index]
      initial_index += 1
  return initial_index

def findMissingPositive(numbers, size):
  for number_index in range(size):
    if (abs(numbers[number_index]) - 1) < size and abs(numbers[number_index]) > 0:
      index = abs(numbers[number_index])
      numbers[index - 1] = -numbers[index - 1]

  for number in range(size):
    if numbers[number] > 0:
      return number + 1
  return size + 1

def findMissingNumber(numbers, size):
  # First separate positive and negative numbers
  shift = segregate(numbers, size)
  # Find the missing positive number.
  return findMissingPositive(numbers[shift:], size - shift)

numbers = [0, 2, 3, 4, 5, 6, 7]
size = len(numbers)
result = findMissingNumber(numbers, size)
print("Missing number from array is", result)

# Time Complexity: O(n) => because loop is executed len of array times.