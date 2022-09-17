def ternarySearch(array, search_element, start, end):
  while start <= end:
    # Find first mid.
    # Divided into 3 part.
    first_mid = start + (end - start)//3
    # Find second mid.
    second_mid = end - (end - start)//3
    # Element found on first mid
    if array[first_mid] == search_element:
      return first_mid
    # Element found on second mid
    elif array[second_mid] == search_element:
      return second_mid
    # Element found on first part of array
    elif array[first_mid] > search_element:
      return ternarySearch(array, search_element, start, first_mid - 1)
    # Element found on last part of array
    elif array[second_mid] < search_element:
      return ternarySearch(array, search_element, second_mid + 1, end)
    else:
    # Element found on second part of array
      return ternarySearch(array, search_element, first_mid + 1, second_mid - 1)
  return -1

## Driver code
array = [20, 25, 47, 56, 59, 63, 65, 79, 82]
start = 0
end = len(array) - 1
search_element = 79
result = ternarySearch(array, search_element, start, end)
print("Searching element is present at the location (with recurive):", result)

# Time complexity:

# Recurrence Relation: T(n) = T(n/3) + c
# Using substitution method:
Big-oh(logn base3)