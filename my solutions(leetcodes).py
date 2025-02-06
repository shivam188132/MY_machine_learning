import pandas as pd

# Read the Excel file
df = pd.read_excel("C:\Users\shiva\Downloads\Amazon Sale Report.xlsx", engine='openpyxl')  # Ensure openpyxl is installed

# Convert to CSV
df.to_csv("Amazon report.csv", index=False, encoding='utf-8')
