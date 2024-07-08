import pandas as pd
import matplotlib.pyplot as plt
import math as math 
from matplotlib.ticker import ScalarFormatter

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

velocity1 = data1["avg(U (Magnitude))"]
velocity2 = data2["avg(U (Magnitude))"]
velocity3 = data3["avg(U (Magnitude))"]
velocity4 = data4["avg(U (Magnitude))"]
velocity5 = data5["avg(U (Magnitude))"]
velocity6 = data6["avg(U (Magnitude))"]

time900 = data3["Time"]
time900NoBaffles = data4["Time"]

cp = 4179 # J/kg*K
density = 995.7 # kg/m^3
area = 0.04 * 0.04 * math.pi  # m^2
initialTemperature =  302.8 # K

Q1 = cp * density * ((temperature1 - initialTemperature) * velocity1) * area * 1/1000 # W to kW
Q2 = cp * density * ((temperature2 - initialTemperature) * velocity2) * area * 1/1000 # W to kW
Q3 = cp * density * ((temperature3 - initialTemperature) * velocity3) * area * 1/1000 # W to kW
Q4 = cp * density * ((temperature4 - initialTemperature) * velocity4) * area * 1/1000 # W to kW
Q5 = cp * density * ((temperature5 - initialTemperature) * velocity5) * area * 1/1000 # W to kW
Q6 = cp * density * ((temperature6 - initialTemperature) * velocity6) * area * 1/1000 # W to kW


plt.plot(time900, Q1, label='Ushell = 0.01(m/s), Re=1000', color='red')
plt.plot(time900, Q2, label='Ushell = 0.03 (m/s), Re = 3000', color='blue')
plt.plot(time900, Q3, label='Ushell = 0.05 (m/s), Re = 5000', color='green')
#plt.plot(time900NoBaffles, Q4, label='Ushell = 0.01(m/s), Re = 1000, No Baffles', color='red')
#plt.plot(time900, Q5, label='Ushell = 0.03 (m/s), Re = 3000, No Baffles', color='blue')
#plt.plot(time900, Q6, label='Ushell = 0.05 (m/s), Re = 5000, No Baffles', color='green')


plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Heat Transfer Rate (kW)')
plt.title('Heat Transfer Rate - Without Baffles ')
plt.xticks(range(0, int(max(time900)) + 100, 100))

plt.grid(True)

fileName ="heatTransferRateBaffle"
plt.savefig('/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/water-water/dataAnalysis/plots/general/'+fileName+'.png')
plt.show()