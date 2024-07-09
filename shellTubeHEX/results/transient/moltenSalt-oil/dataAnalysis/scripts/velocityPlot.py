import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Read the CSV file into a pandas DataFrame
data1 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-01.csv")
data1v2 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-01NoRes.csv")
data2 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-079479.csv")
data3 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/data/MSOil_0-005.csv")

# Extract the temperature column from the DataFrame
velocity1 = data1["avg(U (Magnitude))"]
velocity1v2 = data1v2["avg(U (Magnitude))"]
velocity2 = data2["avg(U (Magnitude))"]
velocity3 = data3["avg(U (Magnitude))"]

# Plot the temperature data
plt.grid(True) 
time900 = data3["Time"]

plt.plot(time900, velocity3, label='Ushell = 0.005 (m/s), color='black')
plt.plot(time900, velocity1, label='Ushell = 0.01(m/s), color='red')
#plt.plot(time900, velocity1v2, label='Ushell = 0.01 (m/s) - No Resistance, color='green')
plt.plot(time900, velocity2, label='Ushell = 0.079479 (m/s), color='blue')

plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Outlet Average Velocity (magnitude)')
plt.xticks(range(0, int(max(time900)) + 100, 100))
plt.ticklabel_format(style='plain', axis='y')
formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(False)
formatter.set_useOffset(False)
plt.gca().yaxis.set_major_formatter(formatter)
fileName ="VelocityPlotGeneral"
plt.savefig('/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/moltenSalt-oil/dataAnalysis/plots/' + fileName + '.png')
plt.show()