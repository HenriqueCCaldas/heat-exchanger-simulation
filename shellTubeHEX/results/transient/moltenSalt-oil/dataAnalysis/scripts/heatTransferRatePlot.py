import pandas as pd
import matplotlib.pyplot as plt
import math as math 
from matplotlib.ticker import ScalarFormatter

# Read the CSV file into a pandas DataFrame

data1 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil.csv")

# Extract the temperature column from the DataFrame
temperature1 = data1["avg(T)"]

velocity1 = data1["avg(U (Magnitude))"]

time900 = data1["Time"]

cp = 1396.018 + (0.172 * temperature1)  # J/kg*K
density = 2263.723 - (0.636 * temperature1)  # kg/m^3
area = 0.04 * 0.04 * math.pi  # m^2
initialTemperature =  563.15 # K

print(temperature1)
Q1 = cp * density * ((temperature1 - initialTemperature) * velocity1) * area * 1/1000 # W to kW

plt.plot(time900, Q1, label='Ushell = 0.01(m/s), Re=1000', color='red')

plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Heat Transfer Rate (kW)')
plt.title('Heat Transfer Rate - Molten Salt & Thermal Oil ')
plt.xticks(range(0, int(max(time900)) + 100, 100))

plt.grid(True)

fileName ="heatTransferRate"
plt.savefig('/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/plots/' + fileName + '.png')
plt.show()