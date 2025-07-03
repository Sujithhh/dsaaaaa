def sol(a, target):
    n= len(a)
    for i in range(n):
        for j in range(n):
            if i ==j:
                continue
            if a[i]+a[j]==target:
                return i , j
    return -1,-1


res = sol([1, 2, 3, 4, 5], 9)
print(res)

# Time Complexity: O(n²)

# The outer loop runs n times.

# The inner loop also runs n times (excluding one comparison when i == j, but that's still effectively n-1).

# So total comparisons ≈ n * (n - 1) → which is O(n²) in Big-O notation.