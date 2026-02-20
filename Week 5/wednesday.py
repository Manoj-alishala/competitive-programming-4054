# Community Detection using DSU
#
# Sample Input:
# 7
# 5
# 0 1
# 1 3
# 2 4
# 5 6
# 3 4
# 3
# 0 4
# 2 6
# 5 6
#
# Sample Output:
# YES
# NO
# YES


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return
        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        elif self.rank[pb] < self.rank[pa]:
            self.parent[pb] = pa
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1


def solve():
    n = int(input())
    dsu = DSU(n)

    f = int(input())   # friendships
    for _ in range(f):
        u, v = map(int, input().split())
        dsu.union(u, v)

    q = int(input())   # queries
    for _ in range(q):
        u, v = map(int, input().split())
        print("YES" if dsu.find(u) == dsu.find(v) else "NO")


if __name__ == "__main__":
    solve()

# City Road Connectivity using DSU
#
# Sample Input:
# 8
# 5
# 1 2
# 2 3
# 4 5
# 6 7
# 5 6
# 3
# 1 3
# 1 7
# 4 7
#
# Sample Output:
# YES
# NO
# YES


class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0]*(n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return
        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        elif self.rank[pb] < self.rank[pa]:
            self.parent[pb] = pa
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1


def solve():
    n = int(input())
    dsu = DSU(n)

    r = int(input())   # roads
    for _ in range(r):
        u, v = map(int, input().split())
        dsu.union(u, v)

    q = int(input())   # queries
    for _ in range(q):
        u, v = map(int, input().split())
        print("YES" if dsu.find(u) == dsu.find(v) else "NO")


if __name__ == "__main__":
    solve()
