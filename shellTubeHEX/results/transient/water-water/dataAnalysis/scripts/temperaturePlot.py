import pandas as pd
import matplotlib.pyplot as plt

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

# Plot the temperature data
plt.grid(True) 

time900 = data3["Time"]
time900NoBaffles = data4["Time"]

# Choose the data to plot (Please select pairs 1-4, 2-5, 3-6)

plt.plot(time900, temperature1, label='uin = 0.01, Baffles', color='red')
plt.plot(time900NoBaffles, temperature4, label='uin = 0.01, No Baffles', color='red', linestyle='dashed')
plt.plot(time900, temperature2, label='uin = 0.03, Baffles', color='blue')
plt.plot(time900, temperature5, label='uin = 0.03, No Baffles', color='blue', linestyle='dashed')
plt.plot(time900, temperature3, label='uin = 0.05, Baffles', color='green')
plt.plot(time900, temperature6, label='uin = 0.05, No Baffles', color='green', linestyle='dashed')


plt.legend(fontsize= 12)
plt.xlabel('Time (s)', fontsize= 20)
plt.ylabel('Temperature (K)', fontsize= 20)
plt.title('Shell Outlet Average Temperature - Baffles & No Baffles', fontsize= 20)
plt.xticks(range(0, int(max(time900)) + 100, 100), fontsize= 20)
plt.yticks(fontsize= 20)
fileName ="TemperatureGeneral"
plt.savefig('/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/water-water/dataAnalysis/plots/test/'+fileName+'.png')
plt.show()


