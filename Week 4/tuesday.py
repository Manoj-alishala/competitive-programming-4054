# Rainfall Measurement Using Fenwick Tree
#
# Sample Input:
# 6
# 5 12 7 10 6 8
# 3
# Q 4
# U 3 9
# Q 4
#
# Sample Output:
# 34
# 36

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0]*(n+1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    bit = Fenwick(n)

    for i, v in enumerate(arr, start=1):
        bit.update(i, v)

    q = int(input())
    for _ in range(q):
        op = input().split()

        if op[0] == 'Q':
            d = int(op[1])
            print(bit.query(d))
        else:  # U i x
            i = int(op[1])
            x = int(op[2])
            delta = x - arr[i-1]
            arr[i-1] = x
            bit.update(i, delta)


if __name__ == "__main__":
    solve()


#-----Problem 2 ------------

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0]*(n+1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    bit = Fenwick(n)

    for i, v in enumerate(arr, start=1):
        bit.update(i, v)

    q = int(input())
    for _ in range(q):
        op = input().split()

        if op[0] == 'Q':
            d = int(op[1])
            print(bit.query(d))
        else:  # U i x
            i = int(op[1])
            x = int(op[2])
            delta = x - arr[i-1]
            arr[i-1] = x
            bit.update(i, delta)


if __name__ == "__main__":
    solve()

# Online Course Watch-Time Analysis Using Fenwick Tree
#
# Sample Input:
# 5
# 30 40 20 50 10
# 3
# Q 4
# U 2 55
# Q 4
#
# Sample Output:
# 140
# 155
