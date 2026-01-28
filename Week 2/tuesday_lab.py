"""
Sample Input:
3 50
60 10
100 20
120 30

Sample Output:
220
"""

def solve():
    try:
        line = input().split()
        if not line:
            return
        
        n = int(line[0])
        W = int(line[1])

        dp = [0] * (W + 1)

        for _ in range(n):
            value, weight = map(int, input().split())
            for w in range(W, weight - 1, -1):
                dp[w] = max(dp[w], dp[w - weight] + value)

        print(dp[W])

    except EOFError:
        pass

if __name__ == "__main__":
    solve()
