def sol(arr):
    n=len(arr)
    result = float('-inf')
    for i in range(n):
        for j in range(i+1,n):
            prod=1
            for k in range(i,j+1):
                prod *= arr[k]
            result = max(result, prod)
    return result



arr=[1, 5, 10, 0, 7, 8]
print(sol(arr))