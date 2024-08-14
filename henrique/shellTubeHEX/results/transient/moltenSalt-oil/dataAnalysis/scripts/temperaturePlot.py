import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-005.csv")
data2 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-01.csv")
data1v2 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-01NoRes.csv")
data3 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-03.csv")
data4 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-05.csv")
data5 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-079479.csv")

# Extract the temperature column from the DataFrame
temperature1 = data1["avg(T)"]
temperature2 = data2["avg(T)"]
temperature2v2 = data1v2["avg(T)"]
temperature3 = data3["avg(T)"]
temperature4 = data4["avg(T)"]
temperature5 = data5["avg(T)"]

# Plot the temperature data
plt.grid(True) 

time900 = data1["Time"]
time900v2 = data3["Time"]

# Choose the data to plot (Please select pairs 1-4, 2-5, 3-6)

plt.plot(time900, temperature1, label='Uin = 0.005 (m/s)', color='red')
plt.plot(time900, temperature2, label='Uin = 0.010(m/s)', color='blue')
#plt.plot(time900, temperature2v2, label="Uin = 0.010 (m/s), No Resistance", color="red", linestyle = "dashed")
plt.plot(time900v2, temperature3, label='Uin = 0.030 (m/s)', color='green')
plt.plot(time900v2, temperature4, label='Uin = 0.050 (m/s)', color='black')
plt.plot(time900, temperature5, label='Uin= 0.079 (m/s)', color='orange')


plt.legend(fontsize = 12)
plt.xlabel('Time (s)', fontsize = 20)
plt.ylabel('Temperature (K)',  fontsize = 20)
plt.title('Shell Outlet Average Temperature - Molten Salt & Thermal Oil',  fontsize = 20)
plt.xticks(range(0, int(max(time900)) + 100, 100),  fontsize = 20)
plt.yticks( fontsize = 20)
fileName ="TemperaturePlotResistances"
plt.savefig('/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/plots/' + fileName + '.png')
plt.show()


