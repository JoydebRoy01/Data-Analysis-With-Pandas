import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data.csv')

print(df.head())

print(df.describe())

mv = df.isnull().sum()
print("Missing values in each column:\n", mv)

# Assuming 'Age' column exists
avg = df['Age'].mean()
print(f'Average of age: {avg}')

uv = df['Age'].nunique()
print(f'unuque values: {uv}')

eng_emp = df[df['Department'] == 'Engineering']
print(eng_emp)

# Find the max salary
max_sal = df['salary'].max()
max_salary_emp = df[df['salary'] == max_sal]
print('Highest salary employee \n:', max_salary_emp)

dep_count = df['Department'].value_counts()
print("Number of employee in each department: \n", dep_count)

sort = df.sort_values(by='Age', ascending=False)
print("Senior to junir employee \n", sort)

df['Experience'] = df['Age'].apply(lambda x: 'Senior' if x > 30 else 'junior')
print("Data with Experience column:\n", df)

plt.figure(figsize=(8, 6))
plt.pie(dep_count, labels=dep_count.index, autopct='%1.1f%%', startangle=140)
plt.title("Department")
plt.show()