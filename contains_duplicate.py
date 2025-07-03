def sol(arr):
    n=len(arr)
    for i in range(n):
        for j in range(1,n):
            if arr[i] == arr[j]: 
                return True
        return False
    

res = sol([1, 2, 3, 4])
print(res)
