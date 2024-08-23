import pandas as pd
import numpy as np

# Load the dataset
file_path = "/Untitled Folder.csv"
df = pd.read_csv(file_path)

# Display initial data info
print("Initial Data Info:")
print(df.info())

# Handling missing values
# Fill missing values for numeric columns with the median
df.fillna(df.median(), inplace=True)

# Detecting and handling outliers
# Define a function to identify outliers using the IQR method
def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] < lower_bound) | (df[column] > upper_bound)]

# Replace outliers with the median value
for column in ["Income", "Credit_Score", "Account_Balance", "Loan_Amount"]:
    outliers = detect_outliers(df, column)
    if not outliers.empty:
        median_value = df[column].median()
        df.loc[outliers.index, column] = median_value

# Save the cleaned DataFrame to a new CSV file
cleaned_file_path = "/tmp/Untitled Folder.csv"
df.to_csv(cleaned_file_path, index=False)

print(f"\nCleaned dataset saved to {cleaned_file_path}")

# Descriptive Statistics
print("\nDescriptive Statistics:")

for column in ["Age", "Income", "Credit_Score", "Account_Balance", "Loan_Amount"]:
    print(f"\n{column}:")
    print(f"Mean: {df[column].mean():.2f}")
    print(f"Median: {df[column].median():.2f}")
    print(f"Mode: {df[column].mode()[0]:.2f}")
    print(f"Standard Deviation: {df[column].std():.2f}")


OUTPUT:

Initial Data Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 50 entries, 0 to 49
Data columns (total 6 columns):
 #   Column           Non-Null Count  Dtype  
---  ------           --------------  -----  
 0   Customer_ID      50 non-null     int64  
 1   Age              50 non-null     float64
 2   Income           50 non-null     float64
 3   Credit_Score     50 non-null     float64
 4   Account_Balance  50 non-null     float64
 5   Loan_Amount      50 non-null     float64
dtypes: float64(5), int64(1)
memory usage: 2.5 KB
None

Cleaned dataset saved to /content/sample_data.csv

Descriptive Statistics:

Age:
Mean: 36.68
Median: 37.00
Mode: 37.00
Standard Deviation: 10.39

Income:
Mean: 49681.92
Median: 50076.00
Mode: 50076.00
Standard Deviation: 7839.94

Credit_Score:
Mean: 693.88
Median: 698.00
Mode: 698.00
Standard Deviation: 42.49

Account_Balance:
Mean: 20650.18
Median: 21712.00
Mode: 21712.00
Standard Deviation: 6283.83

Loan_Amount:
Mean: 14978.64
Median: 16515.00
Mode: 16515.00
Standard Deviation: 5409.06
