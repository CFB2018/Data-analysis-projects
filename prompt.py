
# Build a prompt where you ask GenAI to generate a code to import the provided data set ot Pandas' df.
# Specify if you are importing the data. Assume the first row is the header in the CSV file.


import pandas as pd

# Specify the path to your CSV file
file_path = "C:\\Users\\marbj610\\Documents\\Repository\\Data-analysis-projects\\laptop_pricing_dataset_mod1.csv"

# Read the CSV file
df = pd.read_csv(file_path)
print(df.head())

# Identify missing values in the data
columns_with_missing_values = df.columns[df.isnull().any()]
print(columns_with_missing_values)

# Attributes missing: Index(['Screen_Size_cm', 'Weight_kg'], dtype='object')

# RULES for handling missing data:
# Missing entries in columns containing categorical values need to be replaced with the most frequent entries
# Missing entries in columns with continuous data need to be replaced with the mean value of the column
# If a value is missing in the target column, you may need to drop that row

# Replace missing values in the 'Screen_Size_cm' column with the most frequent value
most_frequent_value = df['Screen_Size_cm'].mode()[0]
df['Screen_Size_cm'].fillna(most_frequent_value, inplace=True)

# print(most_frequent_value) #39.624
# print(df['Screen_Size_cm'].dtype) #float64

# Replace missing values in the 'Weight_kg' column with the mean value
mean_value = df['Weight_kg'].mean()
df['Weight_kg'].fillna(mean_value, inplace=True)

# print(df['Weight_kg'].dtype) #float64
#print(mean_value) #1.8622317596566522

# Check for remaining missing values in both columns
missing_screen_size = df['Screen_Size_cm'].isna().sum()
missing_weight = df['Weight_kg'].isna().sum()
print("Remaining missing values in 'Screen_Size_cm': {}".format(missing_screen_size))
print("Remaining missing values in 'Weight_kg': {}".format(missing_weight))

# Normalize the content under CPU_frequency and max value
max_value = df['CPU_frequency'].max()
df['CPU_frequency'] = df['CPU_frequency'] / max_value

# Build the prompt

