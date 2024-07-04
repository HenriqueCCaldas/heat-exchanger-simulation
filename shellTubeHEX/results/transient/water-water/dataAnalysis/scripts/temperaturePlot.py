import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data1 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/water-water/generalDataAnalysis/data/baffles/outletResultsBaffleRe1000.csv")
data2 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/water-water/generalDataAnalysis/data/baffles/outletResultsBaffleRe3000.csv")
data3 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/water-water/generalDataAnalysis/data/baffles/outletResultsBaffleRe5000.csv")

data4 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/water-water/generalDataAnalysis/data/noBaffles/outletResultsNoBaffleRe1000.csv")
data5 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/water-water/generalDataAnalysis/data/noBaffles/outletResultsNoBaffleRe3000.csv")
data6 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/water-water/generalDataAnalysis/data/noBaffles/outletResultsBaffleRe5000.csv")

# Extract the temperature column from the DataFrame
temperature1 = data1["avg(T)"]
temperature2 = data2["avg(T)"]
temperature3 = data3["avg(T)"]
temperature4 = data4["avg(T)"]
temperature5 = data5["avg(T)"]
temperature6 = data6["avg(T)"]

# Plot the temperature data
plt.grid(True) 

time900 = data3["Time"]
time900NoBaffles = data4["Time"]

# Choose the data to plot (Please select pairs 1-4, 2-5, 3-6)

#plt.plot(time900, temperature1, label='Ushell = 0.01(m/s), Re = 1000', color='red')
#plt.plot(time900, temperature2, label='Ushell = 0.03 (m/s), Re = 3000', color='green')
plt.plot(time900, temperature3, label='Ushell = 0.05 (m/s), Re = 5000', color='blue')
#plt.plot(time900NoBaffles, temperature4, label='Ushell = 0.01(m/s), Re = 1000, No Baffles', color='blue')
#plt.plot(time900, temperature5, label='Ushell = 0.03 (m/s), Re = 3000, No Baffles', color='purple')
plt.plot(time900, temperature6, label='Ushell = 0.05 (m/s), Re = 5000, No Baffles', color='orange')

plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.title('Outlet Average Temperature')
plt.xticks(range(0, int(max(time900)) + 100, 100))
plt.savefig('temperaturePlot0-05.png')
plt.show()


