# PROGRAM 16: Identifying Trends and Relationships
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"C:/Users/Deekshith/Downloads/Salarydata.csv")


plt.plot(df['YearsExperience'], df['Salary'], marker='o', linestyle='-')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Trend of Salary vs Experience (Matplotlib)')
plt.show()

# Seaborn Line Chart
sns.lineplot(x=df['YearsExperience'], y=df['Salary'], marker='o')
plt.title('Trend of Salary vs Experience (Seaborn)')
plt.show()


plt.scatter(df['YearsExperience'], df['Salary'], color='blue')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Scatter Plot: Salary vs Experience (Matplotlib)')
plt.show()
sns.scatterplot(x=df['YearsExperience'], y=df['Salary'], color='red')
plt.title('Scatter Plot: Salary vs Experience (Seaborn)')
plt.show()
