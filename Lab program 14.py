# PROGRAM 14: Advanced Visualization with Seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:/Users/Deekshith/Downloads/salaries14.csv")


print("Columns in dataset:\n", df.columns)
print("\nSkewness:\n", df.skew(numeric_only=True))
print("\nKurtosis:\n", df.kurt(numeric_only=True))


sns.histplot(df["salary"])
plt.title("Salary Distribution (Histogram)")
plt.show()


sns.histplot(df["salary"], kde=True)
plt.title("Salary Distribution with KDE")
plt.show()


sns.distplot(df["salary"])
plt.title("Salary Distribution (Distplot)")
plt.show()


df2 = pd.read_csv(r"C:/Users/Deekshith/Downloads/laptop.csv")


sns.pairplot(df2)
plt.suptitle("Pair Plot of Laptop Dataset", y=1.02)
plt.show()
