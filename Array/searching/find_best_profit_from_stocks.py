# Find max profit we can get from stocks based on per day price.
def findMaxProfit(stocks):
  # Initialization
  minPrice = float('inf')
  maxProfit = 0

  for price in range(len(stocks)):
    if stocks[price] < minPrice:
      minPrice = stocks[price]
    elif stocks[price] - minPrice > maxProfit:
      maxProfit = stocks[price] - minPrice
  return maxProfit

## Driver code
stocks = [7, 1, 5, 3, 6, 4]
maxProfit_value = findMaxProfit(stocks)
print("The max profit of buying and selling the stocks is:", maxProfit_value)