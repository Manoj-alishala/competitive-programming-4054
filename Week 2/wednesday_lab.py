# WEEK 2 - DYNAMIC PROGRAMMING 
import sys
input = sys.stdin.readline


def fibonacci_memo():
    n = int(input())
    memo = [-1] * (n + 1)

    def fib(x):
        if x <= 1:
            return x
        if memo[x] != -1:
            return memo[x]
        memo[x] = fib(x - 1) + fib(x - 2)
        return memo[x]

    print(fib(n))


def knapsack_01():
    n, W = map(int, input().split())
    dp = [0] * (W + 1)

    for _ in range(n):
        value, weight = map(int, input().split())
        for w in range(W, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    print(dp[W])


def lcs():
    s1 = input().strip()
    s2 = input().strip()
    n, m = len(s1), len(s2)

    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[n][m])


def coin_change():
    n = int(input())
    coins = list(map(int, input().split()))
    amount = int(input())

    INF = 10**18
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    print(dp[amount] if dp[amount] != INF else -1)


def mcm():
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [[0]*n for _ in range(n)]

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = 10**18
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
                dp[i][j] = min(dp[i][j], cost)

    print(dp[1][n-1])


def solve():
    choice = int(input().strip())

    if choice == 1:
        fibonacci_memo()
    elif choice == 2:
        knapsack_01()
    elif choice == 3:
        lcs()
    elif choice == 4:
        coin_change()
    elif choice == 5:
        mcm()


if __name__ == "__main__":
    solve()



# ---------- Assignment 1: Fibonacci using Memoization ----------
# Input:
# 10
# Output:
# 55

# ---------- Assignment 2: 0/1 Knapsack ----------
# Input:
# 3 50
# 60 10
# 100 20
# 120 30
# Output:
# 220

# ---------- Assignment 3: Longest Common Subsequence (LCS) ----------
# Input:
# AGGTAB
# GXTXAYB
# Output:
# 4

# ---------- Assignment 4: Coin Change (Minimum Coins) ----------
# Input:
# 3
# 1 3 4
# 6
# Output:
# 2

# ---------- Assignment 5: Matrix Chain Multiplication ----------
# Input:
# 4
# 10 20 30 40
# Output:
# 18000
