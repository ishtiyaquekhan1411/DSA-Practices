## Binary Search Algorithm with iterative approach
## Function definition
def binarySearch(array, search_element, start, end):
  while start <= end:
    mid = start + (end - start)//2
    if array[mid] == search_element:
      return mid
    elif array[mid] < search_element:
      ## Right side of the mid
      ## Search space - mid+1 to j
      start = mid + 1;
    else:
      ## Left side of the mid
      ## Search space - i to mid - 1
      end = mid - 1;

array = [10, 24, 65, 78, 89]
start = 0
end = len(array) - 1
search_element = 24
result = binarySearch(array, search_element, start, end)
print("Searching element is present at the location (with iterative):", result)

## Binary Search Algorithm with recursive approach
## Function definition
def binarySearch(array, search_element, start, end):
  while start <= end:
    mid = start + (end - start)//2
    if array[mid] == search_element:
      return mid
    elif array[mid] < search_element:
      ## Right side of the mid
      ## Search space - mid+1 to j
      ## Recursion - calling the same function again inside the method definition
      return binarySearch(array, search_element, mid + 1, end)
    else:
      ## Left side of the mid
      ## Search space - i to mid - 1
      return binarySearch(array, search_element, start, mid - 1)
  return -1

## Driver code
array = [20, 30, 40, 50, 60 ,70, 90]
start = 0
end = len(array) - 1
search_element = 70
result = binarySearch(array, search_element, start, end)
print("Searching element is present at the location (with recurive):", result)