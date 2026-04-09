# PROGRAM 17: Category and Numeric Relationships
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df4 = pd.read_csv(r"C:/Users/Deekshith/Downloads/salaries14.csv")

plt.bar(df4['experience_level'], df4['salary_in_usd'], width=0.5, edgecolor='white', linewidth=0.4)
plt.xlabel("Experience Level")
plt.ylabel("Salary in USD")
plt.title("Salary vs Experience Level (Matplotlib)")
plt.show()


sns.barplot(x=df4['experience_level'], y=df4['salary_in_usd'], estimator='mean', ci=None)
plt.xlabel("Experience Level")
plt.ylabel("Average Salary in USD")
plt.title("Salary vs Experience Level (Seaborn)")
plt.show()
