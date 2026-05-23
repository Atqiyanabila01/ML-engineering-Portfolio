import pandas as pd

df = pd.read_csv('titanic_clean.csv')

print("=" * 50)
print("FILTERING AND AGGREGATION")
print("=" * 50)

# Filter by passenger class
first_class = df[df['Pclass'] == 1]
print(f"\nFirst class passengers: {len(first_class)}")

# Aggregate by sex
by_sex = df.groupby('Sex').agg({
    'PassengerId': 'count',
    'Age': 'mean',
    'Fare': 'mean'
}).round(2)
print(f"\nPassengers by sex:\n{by_sex}")

# Aggregate by passenger class
by_class = df.groupby('Pclass').agg({
    'PassengerId': 'count',
    'Survived': 'mean',
    'Age': 'mean'
}).round(2)
print(f"\nBy passenger class:\n{by_class}")

# Save results
by_sex.to_csv('by_sex.csv')
by_class.to_csv('by_class.csv')
print("\nResults saved.")