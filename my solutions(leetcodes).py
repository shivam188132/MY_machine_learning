# [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        #    👆
def max_subarray_sum_brute_force(arr):
    n = len(arr)
    max_sum = float('-inf')
    
    for i in range(n): #i = (0,9) i =0,1,2,3
        for j in range(i, n): # (3,9) j=3
            curr_sum = 0
            for k in range(i, j + 1): #(3,4) k=3
                curr_sum += arr[k] # 4
                                   # 2
            max_sum = max(max_sum, curr_sum) #(4, __) --> -2,-1,-1,0,0,1,2,2,2,2,2,2,2,3,4,4,4,4,4,4,4,4,4
    
    return max_sum
