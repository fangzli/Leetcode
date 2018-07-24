total_money = 15
total_damage = 20
costs = [5,4,7,2,6]
damages = [12,3,10,3,6]
def Solution(total_money, total_damage, costs, damages):
    n = len(costs)
    dp = [[0 for _ in range(total_money + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, total_money + 1):
            if j < costs[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-costs[i-1]] + damages[i-1], dp[i-1][j])
            # print(i, j, dp[i][j])
            if dp[i][j] >= total_damage:
                return True
    print(dp)
    return False


print(Solution(total_money, total_damage, costs, damages))