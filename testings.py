import pandas as pd
import numpy as np

# Create sample data
data = pd.DataFrame({'Value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

# Perform equal frequency binning into 3 bins
data['Equal_Frequency_Bin'] = pd.qcut(data['Value'], q=3, labels=['Bin 1', 'Bin 2', 'Bin 3'])

print(data)
import matplotlib.pyplot as plt
import seaborn as sns

# Create histogram for data distribution
sns.histplot(data['Value'], bins=10, kde=False, color='blue', label='Original Data')

# Overlay bin ranges
plt.axvline(x=4.5, color='red', linestyle='--', label='Bin 1-Bin 2 Boundary')
plt.axvline(x=7.5, color='green', linestyle='--', label='Bin 2-Bin 3 Boundary')

plt.title('Equal Frequency Binning')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()
