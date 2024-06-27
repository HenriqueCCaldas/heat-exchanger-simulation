import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data1 = pd.read_csv("outletResultsT1-1.csv")
data2 = pd.read_csv("outletResultsT1-2.csv")

# Extract the temperature column from the DataFrame
temperature1 = data1["avg(T)"]
temperature2 = data2["avg(T)"]

# Plot the temperature data
plt.grid(True) 
time = data1["Time"]

plt.plot(time, temperature1, label='Ushell = 0.05 (m/s)', color='green')
plt.plot(time, temperature2, label='Ushell = 0.1 (m/s)', color='blue')
# Find the rate of change


rate_of_change = temperature1.diff() / time.diff().replace(0, pd.NaT)
# Find the indices where the rate of change is lower than 1%

indices = rate_of_change[rate_of_change > 0.005].index
# Mark the points where the rate of change is lower than 1%

plt.scatter(time[indices], temperature1[indices], color='red', label='Temperature increase > 0.5%')

rate_of_change = temperature2.diff() / time.diff().replace(0, pd.NaT)
# Find the indices where the rate of change is lower than 1%

indices = rate_of_change[rate_of_change > 0.005].index
# Mark the points where the rate of change is lower than 1%

plt.scatter(time[indices], temperature2[indices], color='yellow', label='Temperature increase > 0.5%')

plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.title('Outlet Average Temperature')

plt.show()