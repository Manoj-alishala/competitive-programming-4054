# Problem 1

# Sample Input (paste this when running)
# 1
# 3 50
# 60 10
# 100 20
# 120 30

t = int(input())

for _ in range(t):
    n, W = map(int, input().split())
    items = []

    for _ in range(n):
        v, w = map(int, input().split())
        items.append((v / w, v, w))  # (ratio, value, weight)

    # sort by ratio descending
    items.sort(key=lambda x: x[0], reverse=True)

    total_value = 0.0
    capacity = W

    for ratio, value, weight in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            break

    print(f"{total_value:.6f}")


# Output : 240.000000




# Problem 2 

"""
Sample Input:
1
7
4 1 6 2 5 3 2

Expected Output:
1 2 2 3 4 5 6
"""

def merge(left_half, right_half):
    sorted_arr = []
    i = 0
    j = 0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
        else:
            sorted_arr.append(right_half[j])
            j += 1
    
    
    sorted_arr.extend(left_half[i:])
    sorted_arr.extend(right_half[j:])
    
    return sorted_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    return merge(left_sorted, right_sorted)

def solve():
    try:

        input_line = input().strip()
        if not input_line:
            return
        t = int(input_line)
        
        for _ in range(t):
            
            try:
                n = int(input().strip())
            except EOFError:
                break
                
            arr = list(map(int, input().strip().split()))
            
            result = merge_sort(arr)
            
            print(*result)
            
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
