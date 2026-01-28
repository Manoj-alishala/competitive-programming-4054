"""
Sample Input:
5
3 34 4 12 5
9

Sample Output:
True
"""

def subset_sum(arr, n, target):
    if target == 0:
        return True
    if n == 0 or target < 0:
        return False
    return (subset_sum(arr, n - 1, target) or
            subset_sum(arr, n - 1, target - arr[n - 1]))

def solve():
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        target = int(input())
        print(subset_sum(arr, n, target))
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
