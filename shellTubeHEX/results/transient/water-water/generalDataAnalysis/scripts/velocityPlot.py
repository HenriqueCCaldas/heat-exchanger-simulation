import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data1 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/results/generalDataAnalysis/data/outletResults0-01_900.csv")
data2 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/results/generalDataAnalysis/data/outletResults0-03_900.csv")
data3 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/results/generalDataAnalysis/data/outletResults0-05_900.csv")

# Extract the temperature column from the DataFrame
velocity1 = data1["avg(U (Magnitude))"]
velocity2 = data2["avg(U (Magnitude))"]
velocity3 = data3["avg(U (Magnitude))"]

# Plot the temperature data
plt.grid(True) 
time900 = data3["Time"]

plt.plot(time900, velocity1, label='Ushell = 0.01(m/s), Re = 1000', color='red')
plt.plot(time900, velocity2, label='Ushell = 0.03 (m/s), Re = 3000', color='green')
plt.plot(time900, velocity3, label='Ushell = 0.05 (m/s), Re = 5000', color='blue')


plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Outlet Average Velocity (magnitude)')
plt.xticks(range(0, int(max(time900)) + 100, 100))
plt.savefig('velocityPlotTotal.png')
plt.show()