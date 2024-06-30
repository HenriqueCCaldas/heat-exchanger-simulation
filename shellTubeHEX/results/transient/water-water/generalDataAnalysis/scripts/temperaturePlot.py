import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data1 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/results/generalDataAnalysis/data/outletResults0-01_900.csv")
data2 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/results/generalDataAnalysis/data/outletResults0-03_900.csv")
data3 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/results/generalDataAnalysis/data/outletResults0-05_900.csv")

# Extract the temperature column from the DataFrame
temperature1 = data1["avg(T)"]
temperature2 = data2["avg(T)"]
temperature3 = data3["avg(T)"] 

# Plot the temperature data
plt.grid(True) 

time900 = data1["Time"]
#time300 = data3["Time"]

plt.plot(time900, temperature1, label='Ushell = 0.01(m/s), Re = 1000', color='red')
plt.plot(time900, temperature2, label='Ushell = 0.03 (m/s), Re = 3000', color='green')
plt.plot(time900, temperature3, label='Ushell = 0.05 (m/s), Re = 5000', color='blue')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.title('Outlet Average Temperature')
plt.xticks(range(0, int(max(time900)) + 100, 100))
plt.show()


