import pandas as pd
import numpy as np

# Load the dataset
file_path = "/content/bank_customers_data.csv"
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

# Display cleaned data info
print("\nCleaned Data Info:")
print(df.info())

# Save the cleaned DataFrame to a new CSV file
cleaned_file_path = "/content/Untitled Folder.csv"
df.to_csv(cleaned_file_path, index=False)

print(f"\nCleaned dataset saved to {cleaned_file_path}")                                                                    
