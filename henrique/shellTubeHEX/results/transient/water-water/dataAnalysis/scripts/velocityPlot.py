import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Read the CSV file into a pandas DataFrame
data1 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/water-water/dataAnalysis/data/baffles/outletResultsBaffleRe1000.csv")
data2 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/water-water/dataAnalysis/data/baffles/outletResultsBaffleRe3000.csv")
data3 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/water-water/dataAnalysis/data/baffles/outletResultsBaffleRe5000.csv")

data4 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/water-water/dataAnalysis/data/noBaffles/outletResultsNoBaffleRe1000.csv")
data5 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/water-water/dataAnalysis/data/noBaffles/outletResultsNoBaffleRe3000.csv")
data6 = pd.read_csv("/home/henrique/OpenFOAM/henrique-11/run/heat-exchanger-simulation/shellTubeHEX/results/transient/water-water/dataAnalysis/data/noBaffles/outletResultsNoBaffleRe5000.csv")

# Extract the temperature column from the DataFrame
velocity1 = data1["avg(U (Magnitude))"]
velocity2 = data2["avg(U (Magnitude))"]
velocity3 = data3["avg(U (Magnitude))"]
velocity4 = data4["avg(U (Magnitude))"]
velocity5 = data5["avg(U (Magnitude))"]
velocity6 = data6["avg(U (Magnitude))"]

# Plot the temperature data
plt.grid(True) 
time900 = data3["Time"]
time900NoBaffles = data4["Time"]

#plt.plot(time900, velocity1, label='Ushell = 0.01(m/s), Re = 1000', color='red')
#plt.plot(time900, velocity2, label='Ushell = 0.03 (m/s), Re = 3000', color='green')
plt.plot(time900, velocity3, label='Ushell = 0.05 (m/s), Re = 5000', color='blue')
#plt.plot(time900NoBaffles, velocity4, label='Ushell = 0.01(m/s), Re = 1000, No Baffles', color='yellow')
#plt.plot(time900, velocity5, label='Ushell = 0.03 (m/s), Re = 3000, No Baffles', color='purple')
plt.plot(time900, velocity6, label='Ushell = 0.05 (m/s), Re = 5000, No Baffles', color='orange')


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
plt.savefig('velocityPlotRe1000.png')
plt.show()