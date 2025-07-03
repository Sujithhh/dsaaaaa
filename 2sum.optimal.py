def sol(a, target):
    n= len(a)
    for i in range(n):
        for j in range(1,n):
            if a[i]+a[j]==target:
                return i , j
    return -1,-1


res = sol([1, 2, 3, 4, 5], 7)
print(res)