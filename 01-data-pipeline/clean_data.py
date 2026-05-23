import pandas as pd

url = "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"
df = pd.read_csv(url)

print(f"Original shape: {df.shape}")
print(f"Missing values before:\n{df.isnull().sum()}\n")

# Remove rows with missing values
df_clean = df.dropna()

print(f"Clean shape: {df_clean.shape}")
print(f"Missing values after:\n{df_clean.isnull().sum()}\n")

# Save cleaned data
df_clean.to_csv('titanic_clean.csv', index=False)
print("Cleaned data saved to titanic_clean.csv")