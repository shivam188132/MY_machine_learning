def calc(nums):
    low = float('+inf')
    for x in nums:
        if x < low:
            low = x

    high = float('-inf')
    for x in nums:
        if x > high:
            high = x
            
    return low, high
    

# a=calc([1,2,3, 5, 4,7])
# print(a)
nums=[1,2,3, 5, 3,4]
br_i = 0
smaller = []
for i in range(-1,-len(nums)-1,-1):
    print(i, nums[i])
    if nums[i-1]<nums[i]:
        smaller.append(nums[i])
        br_i = nums[i-1]
        nums[i-1] = nums[i]
        nums[i] = 
        break
# print(nums)
        



    