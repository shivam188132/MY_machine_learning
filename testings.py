def my_fc(nums):
        b_i = float('-inf')
        for i in range(-1,-len(nums),-1):
            if nums[i-1] < nums[i]:
                b_i = i-1
                
                break
        if b_i == float('-inf'):
                nums.reverse()
                return nums
        # b_i = -5
        # b_i = -3
        for i in range(-1, b_i, -1):
            if nums[i] > nums[b_i]:
           # [2,2,4,5,3,0,0] 
                nums[b_i], nums[i] =  nums[i], nums[b_i]
            b = nums
            break
            # [3,2,1]
        # [2,2,4,5,3,0,0]
        nums[b_i+1:] = reversed(nums[b_i+1:])

        return nums, b_i, b
a = my_fc([2,3,1])
print(a)