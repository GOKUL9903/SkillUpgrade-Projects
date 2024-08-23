import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency

# Load the cleaned dataset
file_path = "/content/Untitled Folder.csv"
df = pd.read_csv(file_path)

# T-Test: Comparing the means of two independent groups
# Example: Comparing Income of customers with low vs. high credit scores
# Let's assume a threshold of 650 for credit score
low_credit_score = df[df['Credit_Score'] < 650]['Income']
high_credit_score = df[df['Credit_Score'] >= 650]['Income']

# Perform t-test
t_stat, p_value = ttest_ind(low_credit_score, high_credit_score)

print("\nT-Test: Comparing Income of Customers with Low vs. High Credit Scores")
print(f"T-Statistic: {t_stat:.2f}")
print(f"P-Value: {p_value:.4f}")
if p_value < 0.05:
    print("Result: Statistically significant difference in Income based on Credit Score")
else:
    print("Result: No statistically significant difference in Income based on Credit Score")

# Chi-Square Test: Testing the relationship between two categorical variables
# Example: Relationship between Age group and Loan Amount category
# Create age group and loan amount category
df['Age_Group'] = pd.cut(df['Age'], bins=[18, 30, 40, 50, 60, 100], labels=['18-30', '31-40', '41-50', '51-60', '60+'])
df['Loan_Category'] = pd.cut(df['Loan_Amount'], bins=[0, 5000, 15000, 30000, 100000], labels=['Low', 'Medium', 'High', 'Very High'])

# Create a contingency table
contingency_table = pd.crosstab(df['Age_Group'], df['Loan_Category'])

# Perform Chi-Square test
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

print("\nChi-Square Test: Relationship between Age Group and Loan Amount Category")
print(f"Chi-Square Statistic: {chi2_stat:.2f}")
print(f"P-Value: {p_value:.4f}")
if p_value < 0.05:
    print("Result: Statistically significant relationship between Age Group and Loan Amount Category")
else:
    print("Result: No statistically significant relationship between Age Group and Loan Amount Category")


OUTPUT:
T-Test: Comparing Income of Customers with Low vs. High Credit Scores
T-Statistic: 1.94
P-Value: 0.0584
Result: No statistically significant difference in Income based on Credit Score

Chi-Square Test: Relationship between Age Group and Loan Amount Category
Chi-Square Statistic: 12.53
P-Value: 0.1852
Result: No statistically significant relationship between Age Group and Loan Amount Category
