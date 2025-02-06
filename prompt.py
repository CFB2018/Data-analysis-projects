
# Build a prompt where you ask GenAI to generate a code to import the provided data set ot Pandas'df.
# Specify if you are importing the data. Assume the first row is the header in the CSV file.


import pandas as pd

# Specify the path to your CSV file
file_path = "C:\\Users\\marbj610\\Documents\\Repository\\Data-analysis-projects\\laptop_pricing_dataset_mod1.csv"

# Read the CSV file
df = pd.read_csv(file_path)
print(df.head())

# Identify missing values in the data
columns_with_missing_values = df.columns[df.isnull().any()]
