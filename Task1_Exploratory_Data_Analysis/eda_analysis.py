import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("sales_data.csv")

print("\n===== FIRST 5 ROWS =====")
print(data.head())

print("\n===== DATA INFORMATION =====")
print(data.info())

print("\n===== STATISTICAL SUMMARY =====")
print(data.describe())

print("\n===== MISSING VALUES =====")
print(data.isnull().sum())

# Correlation
print("\n===== CORRELATION =====")
print(data[["Sales", "Profit"]].corr())

# Sales Trend
plt.figure(figsize=(8,5))
plt.plot(data["Month"], data["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Profit Trend
plt.figure(figsize=(8,5))
plt.bar(data["Month"], data["Profit"])
plt.title("Monthly Profit Analysis")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# Heatmap
plt.figure(figsize=(5,4))
sns.heatmap(
    data[["Sales","Profit"]].corr(),
    annot=True
)
plt.title("Correlation Heatmap")
plt.show()

print("\nEDA Completed Successfully!")