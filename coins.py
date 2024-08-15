def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    coin_counts = {}
    
    for coin in coins:
        coin_counts[coin] = amount // coin
        amount = amount % coin
    
    return coin_counts


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)  # Initialize DP table
    dp[0] = 0  # No coins needed for an amount of 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    coin_counts = {coin: 0 for coin in coins}
    i = amount
    while i > 0:
        for coin in coins:
            if dp[i] == dp[i - coin] + 1:
                coin_counts[coin] += 1
                i -= coin
        break

    return coin_counts


resultG = find_coins_greedy(113)
print(resultG)


result = find_min_coins(113)
print(result)  # Виведе: {50: 2, 10: 1, 2: 1, 1: 1}
