import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data1 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/water-water/dataAnalysis/data/baffles/outletResultsBaffleRe1000.csv")
data2 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/water-water/dataAnalysis/data/baffles/outletResultsBaffleRe3000.csv")
data3 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/water-water/dataAnalysis/data/baffles/outletResultsBaffleRe5000.csv")

data4 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/water-water/dataAnalysis/data/noBaffles/outletResultsNoBaffleRe1000.csv")
data5 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/water-water/dataAnalysis/data/noBaffles/outletResultsNoBaffleRe3000.csv")
data6 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/water-water/dataAnalysis/data/noBaffles/outletResultsNoBaffleRe5000.csv")

# Extract the temperature column from the DataFrame
temperature1 = data1["avg(T)"]
temperature2 = data2["avg(T)"]
temperature3 = data3["avg(T)"]
temperature4 = data4["avg(T)"]
temperature5 = data5["avg(T)"]
temperature6 = data6["avg(T)"]

diff1 = temperature1 - temperature4
diff2 = temperature2 - temperature5
diff3 = temperature3 - temperature6
# Plot the temperature datax
plt.grid(True) 

time900 = data3["Time"]
time900NoBaffles = data4["Time"]

# Choose the data to plot (Please select pairs 1-4, 2-5, 3-6)

plt.plot(time900, diff1, label='Ushell = 0.01(m/s)', color='red')
plt.plot(time900, diff2, label='Ushell = 0.03 (m/s)', color='blue')
plt.plot(time900, diff3, label='Ushell = 0.05 (m/s)', color='green')

plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.title('Outlet Average Temperature - Baffles vs No Baffles')
plt.xticks(range(0, int(max(time900)) + 100, 100))

fileName ="temperatureDifferenceBaffleNoBaffle"
plt.savefig('/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/water-water/dataAnalysis/plots/general/'+fileName+'.png')
plt.show()

