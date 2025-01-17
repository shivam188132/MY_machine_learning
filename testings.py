def generate_coffecients(numRows):
    cofficient=[]
    def calc_factorial(numRows):
        
        fact =1
        for i in range(1, numRows+1):
            fact = fact*numRows
        return fact 
    if numRows==0:
        cofficient = [1]
    for i in range(numRows):
        for j in range(numRows+1):
            

            cofficient.append(
                calc_factorial()
            ) 

    return cofficient

# 1
    

print(generate_coffecients(0))