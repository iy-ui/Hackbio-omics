print("Hello, Hackbio!")

import pandas as pd

#load the dataset
df_link = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv"
df = pd.read_csv(df_link, sep="\t")

print(df.head())


### 1. Growth Curves for Each Strain

import matplotlib.pyplot as plt

# Define the strains and their corresponding columns
strains = {
    "Strain1": ["A1", "B1", "C1"],
    "Strain2": ["A2", "B2", "C2"],
    "Strain3": ["A3", "B3", "C3"],
    "Strain4": ["A4", "B4", "C4"]
}

plt.figure(figsize=(10, 6))
for strain, columns in strains.items():
    for col in columns:
        plt.plot(df['time'], df[col], label=f'{strain} {col}')
plt.xlabel('Time (minutes)')
plt.ylabel('OD600')
plt.title('Growth Curves of Different Strains')
plt.legend()
plt.show()


### 2. Time to Reach Carrying Capacity


# Function to calculate time to carrying capacity
def time_to_carrying_capacity(strain_columns):
    max_od = df[strain_columns].max().max()  # Maximum OD600 value
    time_at_max_od = df['time'][df[strain_columns].idxmax().max()]  # Time at max OD600
    return time_at_max_od

# Calculate for each strain
time_to_capacity = {strain: time_to_carrying_capacity(columns) for strain, columns in strains.items()}
print(time_to_capacity)


### 3. Scatter Plot of Time to Carrying Capacity

# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(time_to_capacity.keys(), time_to_capacity.values(), color='blue')
plt.xlabel('Strains')
plt.ylabel('Time to Carrying Capacity (minutes)')
plt.title('Time to Reach Carrying Capacity for Each Strain')
plt.grid(True)
plt.show()


### 4. Box Plot for Knock-out vs Knock-in Strains

# Sample data for box plot
# Replace with actual data
knock_out_times = [time_to_capacity['Strain1'], time_to_capacity['Strain2']]
knock_in_times = [time_to_capacity['Strain3'], time_to_capacity['Strain4']]

# Box plot
plt.figure(figsize=(8, 5))
plt.boxplot([knock_out_times, knock_in_times], labels=['Knock-out', 'Knock-in'])
plt.ylabel('Time to Carrying Capacity (minutes)')
plt.title('Comparison of Time to Carrying Capacity')
plt.show()


### 5. Statistical Analysis: T-test

from scipy.stats import ttest_ind

# Perform t-test
t_stat, p_value = ttest_ind(knock_out_times, knock_in_times)
print(f"T-statistic: {t_stat}, P-value: {p_value}")


# Observations

#Growth Curves*: The overlaid growth curves allow for a visual comparison of how different strains grow over time.
#Time to Carrying Capacity*: The calculated times indicate how quickly each strain reaches its maximum growth.
#Statistical Analysis*: The t-test results (p-value) help determine if there's a significant difference between knock-out and knock-in strains in terms of growth rate.
