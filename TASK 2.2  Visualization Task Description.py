import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "/content/Untitled Folder.csv"
df = pd.read_csv(file_path)

# Descriptive Statistics (optional)
print("\nDescriptive Statistics:")
for column in ["Age", "Income", "Credit_Score", "Account_Balance", "Loan_Amount"]:
    print(f"\n{column}:")
    print(f"Mean: {df[column].mean():.2f}")
    print(f"Median: {df[column].median():.2f}")
    print(f"Mode: {df[column].mode()[0]:.2f}")
    print(f"Standard Deviation: {df[column].std():.2f}")

# Visualization

# 1. Distribution of Age
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], kde=True, bins=10, color='skyblue')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 2. Boxplot of Income
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Income'], color='lightgreen')
plt.title('Boxplot of Income')
plt.xlabel('Income')
plt.show()

# 3. Scatter Plot of Income vs. Loan Amount
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Income', y='Loan_Amount', data=df, color='coral')
plt.title('Income vs. Loan Amount')
plt.xlabel('Income')
plt.ylabel('Loan Amount')
plt.show()

# 4. Correlation Heatmap
plt.figure(figsize=(10, 6))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# 5. Pairplot for Age, Income, Credit Score, and Loan Amount
sns.pairplot(df[['Age', 'Income', 'Credit_Score', 'Loan_Amount']], diag_kind='kde')
plt.suptitle('Pairplot of Selected Features', y=1.02)
plt.show()


OUTPUT:

Descriptive Statistics:

Age:
Mean: 36.68
Median: 37.00
Mode: 37.00
Standard Deviation: 10.39

Income:
Mean: 49683.18
Median: 50076.00
Mode: 50076.00
Standard Deviation: 9018.29

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
Mean: 15272.38
Median: 16515.00
Mode: 16515.00
Standard Deviation: 5873.08
Descriptive Statistics:



