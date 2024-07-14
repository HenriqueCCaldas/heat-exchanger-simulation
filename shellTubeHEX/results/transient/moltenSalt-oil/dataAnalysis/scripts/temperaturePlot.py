import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-005.csv")
data2 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-01.csv")
#data1v2 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-01NoRes.csv")
data3 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-03.csv")
data4 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-079479.csv")

# Extract the temperature column from the DataFrame
temperature1 = data1["avg(T)"]
#temperature1v2 = data1v2["avg(T)"]
temperature2 = data2["avg(T)"]
temperature3 = data3["avg(T)"]

# Plot the temperature data
plt.grid(True) 

time900 = data1["Time"]
time900v2 = data3["Time"]

# Choose the data to plot (Please select pairs 1-4, 2-5, 3-6)

plt.plot(time900, temperature1, label='Ushell = 0.005 (m/s)', color='red')
plt.plot(time900, temperature2, label='Ushell = 0.01(m/s)', color='blue')
plt.plot(time900v2, temperature3, label='Ushell = 0.03 (m/s)', color='green')
#plt.plot(time900, temperature4, label='Ushell = 0.079479 (m/s)', color='green')


plt.legend()
plt.xlabel('Time (s)', fontsize = 12)
plt.ylabel('Temperature (K)',  fontsize = 12)
plt.title('Outlet Average Temperature - Molten Salt & Thermal Oil',  fontsize = 12)
plt.xticks(range(0, int(max(time900)) + 100, 100),  fontsize = 12)
plt.yticks( fontsize = 12)
fileName ="TemperaturePlotGerenalIpdated"
plt.savefig('/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/plots/' + fileName + '.png')
plt.show()


