import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv('user_data.csv')

# Convert 'age' and 'income' columns to numeric values (in case of any string formatting issues)
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['income'] = pd.to_numeric(df['income'], errors='coerce')

# Remove rows with NaN values
df.dropna(inplace=True)

# Analysis 1: Age vs Income
plt.figure(figsize=(10, 5))
plt.bar(df['age'], df['income'], color='blue')
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Age vs Income')
plt.savefig('age_income.png')  # Save the chart
plt.show()

# Analysis 2: Gender distribution in spending categories
expense_columns = ["utilities", "entertainment", "school_fees", "shopping", "healthcare"]

# Convert expense columns to numeric and replace NaN with 0
for col in expense_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# Aggregate by gender
gender_expenses = df.groupby("gender")[expense_columns].sum()

# Plot gender-based spending distribution
gender_expenses.plot(kind="bar", figsize=(10, 5))
plt.title("Spending Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Spending")
plt.legend(title="Expense Categories")
plt.savefig('gender_spending.png')  # Save the chart
plt.show()
