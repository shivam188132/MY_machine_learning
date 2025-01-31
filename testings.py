# x = [2,2,3,5,4,0,0]
x = [3,2,1]
def nums(x):
        i = len(x)-1
        
        k = len(x)-1

        while (k>0 and x[k-1]>= x[k]):
            k-=1
        # return k
        if (k == 0):
            x[:] = reversed(x[:])
            return x
            # k =3
        while(i>=k):
            if(x[i]> x[k-1]):
                 temp = x[k-1]
                 x[k-1] = x[i]
                 x[i] = temp
                 break
            else:
                i-=1
        x[k:] = reversed(x[k:])
        return x
            

       
            


        # return x
        


a = nums(x)
print(a)