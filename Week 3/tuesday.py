# -------- Tuesday: Count Subsets with Given Sum --------
# Input:
# 1
# 4 5
# 1 2 3 4
# Output:
# 2

import sys
from bisect import bisect_left
from collections import Counter

input = sys.stdin.readline


def get_sums(arr):
    n = len(arr)
    sums = []
    for mask in range(1 << n):
        s = 0
        for i in range(n):
            if mask & (1 << i):
                s += arr[i]
        sums.append(s)
    return sums


# Tuesday Assignment
def tuesday():
    T = int(input())
    for _ in range(T):
        N, S = map(int, input().split())
        arr = list(map(int, input().split()))

        mid = N // 2
        left = get_sums(arr[:mid])
        right = get_sums(arr[mid:])

        freq = Counter(right)
        ans = 0
        for x in left:
            ans += freq[S - x]

        print(ans)


# Wednesday Assignment
def wednesday():
    T = int(input())
    for _ in range(T):
        N, S = map(int, input().split())
        arr = list(map(int, input().split()))

        mid = N // 2
        left = get_sums(arr[:mid])
        right = sorted(get_sums(arr[mid:]))

        best = 10**18

        for x in left:
            target = S - x
            idx = bisect_left(right, target)

            if idx < len(right):
                best = min(best, abs(x + right[idx] - S))
            if idx > 0:
                best = min(best, abs(x + right[idx-1] - S))

        print(best)


def solve():
    # enter:
    # 1 -> Tuesday problem
    # 2 -> Wednesday problem
    choice = int(input().strip())

    if choice == 1:
        tuesday()
    elif choice == 2:
        wednesday()


if __name__ == "__main__":
    solve()

# -------- Wednesday: Closest Subset Sum --------
# Input:
# 1
# 4 10
# 1 4 7 12
# Output:
# 1
