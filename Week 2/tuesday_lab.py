# WEEK 2 - BACKTRACKING (ALL IN ONE)



import sys
input = sys.stdin.readline


# 1) N Queens
def n_queens():
    n = int(input())
    board = [["."]*n for _ in range(n)]

    def is_safe(r, c):
        for i in range(r):
            if board[i][c] == "Q":
                return False
        i, j = r-1, c-1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1; j -= 1
        i, j = r-1, c+1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1; j += 1
        return True

    def solve_row(r):
        if r == n:
            for row in board:
                print(" ".join(row))
            return True
        for c in range(n):
            if is_safe(r, c):
                board[r][c] = "Q"
                if solve_row(r+1):
                    return True
                board[r][c] = "."
        return False

    solve_row(0)


# 2) Permutations
def permutations_string():
    s = list(input().strip())
    n = len(s)

    def backtrack(i):
        if i == n:
            print("".join(s))
            return
        for j in range(i, n):
            s[i], s[j] = s[j], s[i]
            backtrack(i+1)
            s[i], s[j] = s[j], s[i]

    backtrack(0)


# 3) Subset Sum
def subset_sum():
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())

    def backtrack(i, curr):
        if curr == target:
            return True
        if i == n or curr > target:
            return False
        return backtrack(i+1, curr+arr[i]) or backtrack(i+1, curr)

    print(backtrack(0, 0))


# 4) Sudoku Solver
def sudoku():
    grid = [list(map(int, input().split())) for _ in range(9)]

    def is_safe(r, c, num):
        for x in range(9):
            if grid[r][x] == num or grid[x][c] == num:
                return False
        sr, sc = r - r%3, c - c%3
        for i in range(3):
            for j in range(3):
                if grid[sr+i][sc+j] == num:
                    return False
        return True

    def solve_cell():
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    for num in range(1, 10):
                        if is_safe(i, j, num):
                            grid[i][j] = num
                            if solve_cell():
                                return True
                            grid[i][j] = 0
                    return False
        return True

    solve_cell()
    for row in grid:
        print(*row)


# 5) Rat in Maze
def rat_maze():
    n = int(input())
    maze = [list(map(int, input().split())) for _ in range(n)]
    path = [[0]*n for _ in range(n)]

    def backtrack(r, c):
        if r == n-1 and c == n-1 and maze[r][c] == 1:
            path[r][c] = 1
            return True
        if 0 <= r < n and 0 <= c < n and maze[r][c] == 1 and path[r][c] == 0:
            path[r][c] = 1
            if backtrack(r+1, c) or backtrack(r, c+1):
                return True
            path[r][c] = 0
        return False

    if backtrack(0, 0):
        for row in path:
            print(*row)
    else:
        print("No Path")


def solve():
    choice = int(input().strip())

    if choice == 1:
        n_queens()
    elif choice == 2:
        permutations_string()
    elif choice == 3:
        subset_sum()
    elif choice == 4:
        sudoku()
    elif choice == 5:
        rat_maze()


if __name__ == "__main__":
    solve()



# -------- Assignment 1: N-Queens --------
# Input:
# 4
# Output (One Valid):
# . Q . .
# . . . Q
# Q . . .
# . . Q .

# -------- Assignment 2: String Permutations --------
# Input:
# ABC
# Output:
# ABC
# ACB
# BAC
# BCA
# CAB
# CBA

# -------- Assignment 3: Subset Sum --------
# Input:
# 5
# 3 34 4 12 5
# 9
# Output:
# True

# -------- Assignment 4: Sudoku Solver --------
# Input: 9x9 grid with 0 as empty
# Output: Solved grid

# -------- Assignment 5: Rat in a Maze --------
# Input:
# 4
# 1 0 0 0
# 1 1 0 1
# 0 1 0 0
# 1 1 1 1
# Output: One valid path matrix
