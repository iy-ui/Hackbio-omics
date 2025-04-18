print("Hello, Hackbio!")

python
import pandas as pd

data_set = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv"
data = pd.read_csv(data_set, sep="\t")

data.head()


### 1. Growth Curves for Each Strain

python
import matplotlib.pyplot as plt

# Define the strains and their corresponding columns
strains = {
    "Strain1": ["A1", "B1", "C1"],
    "Strain2": ["A2", "B2", "C2"],
    # Add other strains as needed
}

# Plotting
plt.figure(figsize=(10, 6))
for strain, columns in strains.items():
    for col in columns:
        plt.plot(data['time'], data[col], label=f'{strain} {col}')
plt.xlabel('Time (minutes)')
plt.ylabel('OD600')
plt.title('Growth Curves of Different Strains')
plt.legend()
plt.show()


### 3. Determine Time to Reach Carrying Capacity

Assuming carrying capacity is the maximum OD600 value for each strain:

python
# Function to calculate time to carrying capacity
def time_to_carrying_capacity(strain_columns):
    max_od = data[strain_columns].max().max()  # Maximum OD600 value
    time_at_max_od = data['time'][data[strain_columns].idxmax().max()]  # Time at max OD600
    return time_at_max_od

# Calculate for each strain
time_to_capacity = {strain: time_to_carrying_capacity(columns) for strain, columns in strains.items()}
print(time_to_capacity)


### 4. Generate Scatter Plot of Time to Carrying Capacity

python
# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(time_to_capacity.keys(), time_to_capacity.values(), color='blue')
plt.xlabel('Strains')
plt.ylabel('Time to Carrying Capacity (minutes)')
plt.title('Time to Reach Carrying Capacity for Each Strain')
plt.grid(True)
plt.show()


### 5. Generate Box Plot for Knock-out vs Knock-in Strains

Assuming knock-out strains are labeled with 'KO' and knock-in with 'KI':

python
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


### 6. Statistical Analysis: T-test

python
from scipy.stats import ttest_ind

# Perform t-test
t_stat, p_value = ttest_ind(knock_out_times, knock_in_times)
print(f"T-statistic: {t_stat}, P-value: {p_value}")


### Observations

- *Growth Curves*: The overlaid growth curves allow for a visual comparison of how different strains grow over time.
- *Time to Carrying Capacity*: The calculated times indicate how quickly each strain reaches its maximum growth.
- *Statistical Analysis*: The t-test results (p-value) help determine if there's a significant difference between knock-out and knock-in strains in terms of growth rate.
