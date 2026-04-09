# PROGRAM 15: Correlation Visualization with Seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (Laptop specifications)
df2 = pd.read_csv(r"C:/Users/Deekshith/Downloads/laptop.csv")

# Compute correlation matrix (numeric columns only)
corr_matrix = df2.corr(numeric_only=True)

# Display correlation matrix
print("Correlation Matrix:\n", corr_matrix)

# Visualize correlation matrix with Seaborn heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix Heatmap - Laptop Dataset")
plt.show()
