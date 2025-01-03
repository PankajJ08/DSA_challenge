nums = [0,1,2,2,3,0,4,2]
val = 2

n = len(nums)
idx = 0
k = 0

for i in range(0, n):
    if nums[i] != val:
        nums[idx] = nums[i] 
        idx += 1
        k += 1

print(k, nums)
