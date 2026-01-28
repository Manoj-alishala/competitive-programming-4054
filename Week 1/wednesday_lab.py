# Problem 1

"""
Sample Input:
1
5
2 100
1 19
2 27
1 25
3 15

Sample Output:
3 142

Explanation:
1. Sort jobs by profit (descending): 
   (2, 100), (2, 27), (1, 25), (1, 19), (3, 15)
2. Pick (2, 100): Slot 2 is free. Profit = 100.
3. Pick (2, 27): Slot 2 is taken. Find latest free slot < 2. Slot 1 is free. Profit = 100 + 27 = 127.
4. Pick (1, 25): Slot 1 is taken. Slot 0 is invalid. Skip.
5. Pick (1, 19): Slot 1 is taken. Skip.
6. Pick (3, 15): Slot 3 is free. Profit = 127 + 15 = 142.
Total: 3 jobs, 142 profit.
"""

def get_parent(parent, i):
    path = []
    while i != parent[i]:
        path.append(i)
        i = parent[i]
    
    for node in path:
        parent[node] = i
    return i

def solve():
    try:
        line = input().split()
        if not line: return
        t = int(line[0])

        for _ in range(t):
            try:
                line = input().split()
                if not line: break
                n = int(line[0])
            except EOFError:
                break

            jobs = []
            max_deadline = 0

            for _ in range(n):
                d_str, p_str = input().split()
                d = int(d_str)
                p = int(p_str)
                jobs.append((d, p))
                
                if d > max_deadline:
                    max_deadline = d

            
            jobs.sort(key=lambda x: x[1], reverse=True)

            parent = list(range(max_deadline + 1))

            jobs_done = 0
            total_profit = 0

            for d, p in jobs:
                available_slot = get_parent(parent, min(d, max_deadline))
                if available_slot > 0:
                    jobs_done += 1
                    total_profit += p
                    
                    parent[available_slot] = get_parent(parent, available_slot - 1)

            print(f"{jobs_done} {total_profit}")

    except EOFError:
        pass

if __name__ == "__main__":
    solve()



# Problem 2

"""
Sample Input:
1
9
-2 1 -3 4 -1 2 1 -5 4

Expected Output:
6
"""

def max_crossing_sum(arr, low, mid, high):
    left_sum = -10**18  
    current_sum = 0
    for i in range(mid, low - 1, -1):
        current_sum += arr[i]
        if current_sum > left_sum:
            left_sum = current_sum
            
    # Include elements on right of mid
    right_sum = -10**18
    current_sum = 0
    for i in range(mid + 1, high + 1):
        current_sum += arr[i]
        if current_sum > right_sum:
            right_sum = current_sum
            
    return left_sum + right_sum

def max_subarray_sum(arr, low, high):
    if low == high:
        return arr[low]
    
    # Divide
    mid = (low + high) // 2
    
    left_max = max_subarray_sum(arr, low, mid)
    right_max = max_subarray_sum(arr, mid + 1, high)
    
    crossing_max = max_crossing_sum(arr, low, mid, high)
    
    return max(left_max, right_max, crossing_max)

def solve():
    try:
        input_line = input().strip()
        if not input_line: return
        t = int(input_line)
        
        for _ in range(t):
            try:
                n = int(input().strip())
                arr = list(map(int, input().strip().split()))
                
                print(max_subarray_sum(arr, 0, n - 1))
            except (EOFError, ValueError):
                break
                
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    solve()
