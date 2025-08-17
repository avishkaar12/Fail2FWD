
def max_profit(prices):
    min_price = float('inf')  # Start with a very big number for the lowest price
    max_profit = 0            # Start with zero for the most money we can make
    for price in prices:
        min_price = min(min_price, price)  # Always keep the lowest price so far
        max_profit = max(max_profit, price - min_price)  # Always keep the highest profit so far
    return max_profit  # When finished, show the most money we can make
prices = list(map(int, input("Type prices with spaces: ").split()))
print("The most money you can make is:", max_profit(prices))
