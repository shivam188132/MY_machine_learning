# [-2,      1,      -3,     4,      -1,     2,      1,      -5,     4]

#[-2,1,-3,4,-1,2,1,-5,4]
def max_subarray_sum_better(arr):
    n = len(arr) # 9
    max_sum = float('-inf')
    
    for i in range(n): # i=0
        curr_sum = 0
        for j in range(i, n): # (0,9) j=0,1,2
            curr_sum += arr[j]  # -2+1-3,4,-1
            max_sum = max(max_sum, curr_sum) # -2,-1,-5,-1,
    
    return max_sum

print(max_subarray_sum_better([-2,1,-3,4,-1,2,1,-5,4]))
