# -------- Tuesday: Segment Tree for Range Minimum Query --------
# Input:
# 1
# 6
# 2 -1 4 0 3 -5
# 3
# 0 3
# 2 5
# 1 4
# Output:
# -1
# -5
# -1

import sys
input = sys.stdin.readline


# ---------- Tuesday: RMQ ----------
def tuesday():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))

        size = 1
        while size < n:
            size *= 2
        seg = [10**18] * (2 * size)

        # build
        for i in range(n):
            seg[size + i] = arr[i]
        for i in range(size - 1, 0, -1):
            seg[i] = min(seg[2*i], seg[2*i+1])

        # query
        def range_min(l, r):
            l += size
            r += size
            res = 10**18
            while l <= r:
                if l % 2 == 1:
                    res = min(res, seg[l])
                    l += 1
                if r % 2 == 0:
                    res = min(res, seg[r])
                    r -= 1
                l //= 2
                r //= 2
            return res

        q = int(input())
        for _ in range(q):
            l, r = map(int, input().split())
            print(range_min(l, r))


# ---------- Wednesday: Range Sum + Point Update ----------
def wednesday():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))

        size = 1
        while size < n:
            size *= 2
        seg = [0] * (2 * size)

        # build
        for i in range(n):
            seg[size + i] = arr[i]
        for i in range(size - 1, 0, -1):
            seg[i] = seg[2*i] + seg[2*i+1]

        # update
        def update(idx, val):
            pos = size + idx
            seg[pos] = val
            pos //= 2
            while pos >= 1:
                seg[pos] = seg[2*pos] + seg[2*pos+1]
                pos //= 2

        # query
        def range_sum(l, r):
            l += size
            r += size
            res = 0
            while l <= r:
                if l % 2 == 1:
                    res += seg[l]
                    l += 1
                if r % 2 == 0:
                    res += seg[r]
                    r -= 1
                l //= 2
                r //= 2
            return res

        q = int(input())
        for _ in range(q):
            parts = list(map(int, input().split()))
            if parts[0] == 1:
                _, i, x = parts
                update(i, x)
            else:
                _, l, r = parts
                print(range_sum(l, r))


def solve():
    # Enter:
    # 1 -> Tuesday RMQ
    # 2 -> Wednesday Sum + Update
    choice = int(input().strip())

    if choice == 1:
        tuesday()
    elif choice == 2:
        wednesday()


if __name__ == "__main__":
    solve()

# -------- Wednesday: Segment Tree with Point Updates (Range Sum) --------
# Input:
# 1
# 5
# 1 3 5 7 9
# 4
# 2 1 3
# 1 2 10
# 2 1 3
# 2 0 4
# Output:
# 15
# 20
# 30
