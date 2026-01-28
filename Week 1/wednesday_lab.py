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
    # Iterative path compression to find the representative of the set
    # (replaces recursion to avoid depth limits)
    path = []
    while i != parent[i]:
        path.append(i)
        i = parent[i]
    
    # Path compression: make all nodes in path point directly to root
    for node in path:
        parent[node] = i
    return i

def solve():
    try:
        # Read number of test cases
        # Using simple input() inside a loop
        line = input().split()
        if not line: return
        t = int(line[0])

        for _ in range(t):
            # Read N
            try:
                line = input().split()
                if not line: break
                n = int(line[0])
            except EOFError:
                break

            jobs = []
            max_deadline = 0

            # Read N jobs
            for _ in range(n):
                d_str, p_str = input().split()
                d = int(d_str)
                p = int(p_str)
                jobs.append((d, p))
                
                # Track the maximum deadline to size our DSU array
                if d > max_deadline:
                    max_deadline = d

            # GREEDY STEP 1: Sort all jobs by profit in descending order
            # (lambda x: x[1] sorts by profit)
            jobs.sort(key=lambda x: x[1], reverse=True)

            # GREEDY STEP 2: Use Disjoint Set Union (DSU) to find available slots efficiently.
            # parent[i] stores the next available time slot at or before i.
            # Initially, every time slot i is its own available parent.
            parent = list(range(max_deadline + 1))

            jobs_done = 0
            total_profit = 0

            for d, p in jobs:
                # Find the latest available slot up to deadline d
                available_slot = get_parent(parent, min(d, max_deadline))

                # If the slot is > 0, we can schedule the job
                if available_slot > 0:
                    jobs_done += 1
                    total_profit += p
                    
                    # Union operation:
                    # Mark this slot as occupied by making it point to the slot before it.
                    # This effectively removes 'available_slot' from the set of free slots.
                    parent[available_slot] = get_parent(parent, available_slot - 1)

            print(f"{jobs_done} {total_profit}")

    except EOFError:
        pass

if __name__ == "__main__":
    solve()
