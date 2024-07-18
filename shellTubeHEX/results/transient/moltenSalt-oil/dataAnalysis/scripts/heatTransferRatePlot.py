import pandas as pd
import matplotlib.pyplot as plt
import math as math 
from matplotlib.ticker import ScalarFormatter

# Read the CSV file into a pandas DataFrame

data1 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-005.csv")
data2 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-01.csv")
#data1v2 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-01NoRes.csv")
data3 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-03.csv")
data4 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-05.csv")
data5 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-079479.csv")

# Extract the temperature column from the DataFrame
temperature1 = data1["avg(T)"]
#temperature1v2 = data1v2["avg(T)"]
temperature2 = data2["avg(T)"]
temperature3 = data3["avg(T)"]
temperature4 = data4["avg(T)"]
temperature5 = data5["avg(T)"]

velocity1 = data1["avg(U (Magnitude))"]
#velocity1v2 = data1v2["avg(U (Magnitude))"]
velocity2 = data2["avg(U (Magnitude))"]
velocity3 = data3["avg(U (Magnitude))"]
velocity4 = data4["avg(U (Magnitude))"]
velocity5 = data5["avg(U (Magnitude))"]

time900 = data1["Time"]
time900v2 = data3["Time"]

def cp(temperature):
    return 1396.018 + (0.172 * temperature)  # J/kg*K

def density(temperature):
    return 2263.723 - (0.636 * temperature)  # kg/m^3

cp1 = cp(temperature1)  # J/kg*K
density1 = density(temperature1)  # kg/m^3
cp2 = cp(temperature2)  # J/kg*K
density2 = density(temperature2)  # kg/m^3
cp3 = cp(temperature3)  # J/kg*K
density3 = density(temperature3)  # kg/m^3
cp4 = cp(temperature4)  # J/kg*K
density4 = density(temperature4)  # kg/m^3
cp5 = cp(temperature5)  # J/kg*K
density5 = density(temperature5)  # kg/m^3


area = 0.04 * 0.04 * math.pi  # m^2
initialTemperature =  563.15 # K

Q1 = cp1 * density1 * ((temperature1 - initialTemperature) * velocity1) * area * 1/1000 # W to kW
Q2 = cp2 * density2 * ((temperature2 - initialTemperature) * velocity2) * area * 1/1000 # W to kW
Q3 = cp3 * density3 * ((temperature3 - initialTemperature) * velocity3) * area * 1/1000 # W to kW
Q4 = cp4 * density4 * ((temperature4 - initialTemperature) * velocity4) * area * 1/1000 # W to kW
Q5 = cp5 * density5 * ((temperature5 - initialTemperature) * velocity5) * area * 1/1000 # W to kW   

plt.plot(time900, Q1, label='Uin = 0.005(m/s)', color='red')
#plt.plot(time900, Q1v2, label='Ushell = 0.01(m/s) - No Resistance', color='green')
plt.plot(time900, Q2, label='Uin = 0.01(m/s)', color='blue')
plt.plot(time900v2, Q3, label='Uin = 0.03(m/s)', color='green')
plt.plot(time900v2, Q4, label='Uin = 0.05(m/s)', color='black')
plt.plot(time900, Q5, label='Uin = 0.079(m/s)', color='orange')

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