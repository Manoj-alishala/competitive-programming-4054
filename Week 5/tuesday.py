# Efficient Event Scheduling Using Red-Black Tree (simulated with sorted list)
#
# Sample Input:
# 6
# 20 15 25 10 18 30
# 3
# S 18
# D 15
# S 15
#
# Sample Output:
# FOUND
# NOTFOUND

from bisect import bisect_left, insort

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    q = int(input())
    for _ in range(q):
        op, x = input().split()
        x = int(x)

        if op == 'S':  # Search
            i = bisect_left(arr, x)
            print("FOUND" if i < len(arr) and arr[i] == x else "NOTFOUND")

        elif op == 'D':  # Delete
            i = bisect_left(arr, x)
            if i < len(arr) and arr[i] == x:
                arr.pop(i)

        else:  # Insert
            insort(arr, x)

if __name__ == "__main__":
    solve()


# Real-Time Min/Max Query Using Segment Tree
#
# Sample Input:
# 8
# 32 28 30 35 29 31 34 33
# 4
# MIN 2 6
# MAX 1 5
# UPD 3 27
# MIN 2 6
#
# Sample Output:
# 29
# 35
# 27

import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    size = 1
    while size < n:
        size *= 2

    segmin = [10**18]*(2*size)
    segmax = [-10**18]*(2*size)

    # build
    for i in range(n):
        segmin[size+i] = arr[i]
        segmax[size+i] = arr[i]

    for i in range(size-1, 0, -1):
        segmin[i] = min(segmin[2*i], segmin[2*i+1])
        segmax[i] = max(segmax[2*i], segmax[2*i+1])

    def update(idx, val):
        pos = size + idx
        segmin[pos] = val
        segmax[pos] = val
        pos //= 2
        while pos:
            segmin[pos] = min(segmin[2*pos], segmin[2*pos+1])
            segmax[pos] = max(segmax[2*pos], segmax[2*pos+1])
            pos //= 2

    def range_min(l, r):
        l += size
        r += size
        res = 10**18
        while l <= r:
            if l % 2:
                res = min(res, segmin[l]); l += 1
            if not r % 2:
                res = min(res, segmin[r]); r -= 1
            l//=2; r//=2
        return res

    def range_max(l, r):
        l += size
        r += size
        res = -10**18
        while l <= r:
            if l % 2:
                res = max(res, segmax[l]); l += 1
            if not r % 2:
                res = max(res, segmax[r]); r -= 1
            l//=2; r//=2
        return res

    q = int(input())
    for _ in range(q):
        parts = input().split()
        if parts[0] == "MIN":
            l, r = int(parts[1]), int(parts[2])
            print(range_min(l, r))
        elif parts[0] == "MAX":
            l, r = int(parts[1]), int(parts[2])
            print(range_max(l, r))
        else:  # UPD
            i, v = int(parts[1]), int(parts[2])
            update(i, v)

if __name__ == "__main__":
    solve()
