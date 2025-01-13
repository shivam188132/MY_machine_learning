import pandas as pd

# Example DataFrame
data = {
    'A': [1, -2, 3, -4, 0],
    'B': [0, 5, -6, 7, 8],
    'C': [-1, -2, -3, -4, -5]
}
df = pd.DataFrame(data)

# Function to count positive, negative, and zero values for each column
def count_values(df):
    result = {}
    for col in df.columns:
        positives = (df[col] > 0).sum()
        negatives = (df[col] < 0).sum()
        zeros = (df[col] == 0).sum()
        result[col] = {'Positive': positives, 'Negative': negatives, 'Zero': zeros}
    return pd.DataFrame(result)

# Get the counts
counts = count_values(df)
print(counts)
