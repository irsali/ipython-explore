stock_prices = [10, 7, 5, 8, 11, 9]

def get_max_profit(prices: []):
    arr = []
    index = 0

    for item in prices:
        index += 1
        if index < len(prices):
            to_check_prices = prices[index:]
            till_max = max(to_check_prices)
            diff = till_max - item
            arr.append([item, till_max, diff ])

    print(arr)

    profit_list = [ j[2] for j in arr ]
    
    profit = max(profit_list)
    print(profit_list)
    print(profit)

    return profit

get_max_profit(stock_prices)


