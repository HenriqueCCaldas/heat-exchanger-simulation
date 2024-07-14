import pandas as pd
import matplotlib.pyplot as plt
import math as math 
from matplotlib.ticker import ScalarFormatter

# Read the CSV file into a pandas DataFrame

data1 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-01.csv")
data1v2 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-01NoRes.csv")
data2 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-079479.csv")
data3 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-005.csv")

# Extract the temperature column from the DataFrame
temperature1 = data1["avg(T)"]
temperature1v2 = data1v2["avg(T)"]
temperature2 = data2["avg(T)"]
temperature3 = data3["avg(T)"]

velocity1 = data1["avg(U (Magnitude))"]
velocity1v2 = data1v2["avg(U (Magnitude))"]
velocity2 = data2["avg(U (Magnitude))"]
velocity3 = data3["avg(U (Magnitude))"]

time900 = data1["Time"]

cp = 1396.018 + (0.172 * temperature1)  # J/kg*K
density = 2263.723 - (0.636 * temperature1)  # kg/m^3
area = 0.04 * 0.04 * math.pi  # m^2
initialTemperature =  563.15 # K


Q1 = cp * density * ((temperature1 - initialTemperature) * velocity1) * area * 1/1000 # W to kW
Q1v2 = cp * density * ((temperature1v2 - initialTemperature) * velocity1v2) * area * 1/1000 # W to kW
Q2 = cp * density * ((temperature2 - initialTemperature) * velocity2) * area * 1/1000 # W to kW
Q3 = cp * density * ((temperature3 - initialTemperature) * velocity3) * area * 1/1000 # W to kW

plt.plot(time900, Q3, label='Ushell = 0.005(m/s)', color='red')
plt.plot(time900, Q1, label='Ushell = 0.01(m/s)', color='blue')
#plt.plot(time900, Q1v2, label='Ushell = 0.01(m/s) - No Resistance', color='green')
plt.plot(time900, Q2, label='Ushell = 0.079479(m/s)', color='green')

plt.legend()
plt.xlabel('Time (s)', fontsize = 12)
plt.ylabel('Heat Transfer Rate (kW)', fontsize = 12)
plt.title('Heat Transfer Rate - Molten Salt & Thermal Oil ', fontsize = 12)
plt.xticks(range(0, int(max(time900)) + 100, 100), fontsize = 12 )
plt.yticks(fontsize = 12)

plt.grid(True)

fileName ="heatTransferRatePlotGeneral"
plt.savefig('/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/plots/' + fileName + '.png')
plt.show()