import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("outletResults.csv")

# Extract the temperature column from the DataFrame
temperature = data["avg(T)"]
# Plot the temperature data
plt.grid(True) 
time = data["Time"]

plt.plot(time, temperature, label='Utube = 0.1 & Ushell = 0.05 (m/s)', color='green')
# Find the rate of change

rate_of_change = temperature.diff() / time.diff().replace(0, pd.NaT)
# Find the indices where the rate of change is lower than 1%

indices = rate_of_change[rate_of_change > 0.005].index
# Mark the points where the rate of change is lower than 1%

plt.scatter(time[indices], temperature[indices], color='red', label='Temperature increase > 0.5%')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.title('Outlet Average Temperature')

plt.show()