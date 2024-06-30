import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data1 = pd.read_csv("outletResultsT1-1.csv")
data2 = pd.read_csv("outletResultsT1-2.csv")
data3 = pd.read_csv("outletResultsT1-3_900.csv")

# Extract the temperature column from the DataFrame
velocity1 = data1["avg(U (Magnitude))"]
velocity2 = data2["avg(U (Magnitude))"]
velocity3 = data3["avg(U (Magnitude))"]

# Plot the temperature data
plt.grid(True) 
time300 = data1["Time"]
time900 = data3["Time"]

plt.plot(time900, velocity3, label='Ushell = 0.01(m/s)', color='red')
plt.plot(time300, velocity1, label='Ushell = 0.05 (m/s)', color='green')
plt.plot(time300, velocity2, label='Ushell = 0.1 (m/s)', color='blue')


plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Outlet Average Velocity (magnitude)')
plt.xticks(range(0, int(max(time900)) + 100, 100))
plt.savefig('velocityPlot.png')
plt.show()