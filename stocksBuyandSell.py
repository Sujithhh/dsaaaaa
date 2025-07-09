def maxProduct(nums):
    n = len(nums)
    maxi=0
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]<nums[j]:
                profit = nums[j]-nums[i]
                maxi=max(maxi,profit)
    return maxi


result = maxProduct([7,1,5,3,6,4])
print(result)