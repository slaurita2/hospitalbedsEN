# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
df = pd.read_csv('hospital_beds.csv')

# Filter rows with bed data (remove empty rows)
df = df[df['Country Name'].notna() & df['Country Code'].notna()]

# Convert bed columns to numbers (float)
df['2019'] = pd.to_numeric(df['2019'], errors='coerce')

# Sort the DataFrame by the bed column in descending order
df_sorted = df.sort_values(by='2019', ascending=False)

# Take the top 10 countries for visualization
top_countries = df_sorted.head(10)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_countries['Country Name'], top_countries['2019'], color='blue')
plt.xlabel('Countries')
plt.ylabel('Beds per 1,000 people')
plt.title('Top 10 Countries with Most Hospital Beds per 1,000 People (2019)')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for clarity
plt.tight_layout()

# Show the chart
plt.show()
