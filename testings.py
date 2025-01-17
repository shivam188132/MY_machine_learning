def generate(numRows):

        matrix = []
        def binomial_coefficients(n):
            coefficients = [1]  
            for i in range(1, n + 1):
                coefficients.append(coefficients[i - 1] * (n - i + 1) // i)
            return coefficients
        for i in range(numRows):
            x = binomial_coefficients(i)
            matrix.append(x)
         
        return matrix

print(generate(numRows=10000))