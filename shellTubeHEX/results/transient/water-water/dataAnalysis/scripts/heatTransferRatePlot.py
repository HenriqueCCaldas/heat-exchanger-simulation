import pandas as pd
import matplotlib.pyplot as plt
import math as math 

# Read the CSV file into a pandas DataFrame

data1 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/water-water/generalDataAnalysis/data/baffles/outletResults0-01_900.csv")
data2 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/water-water/generalDataAnalysis/data/baffles/outletResults0-03_900.csv")
data3 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/water-water/generalDataAnalysis/data/baffles/outletResults0-05_900.csv")

data4 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/water-water/generalDataAnalysis/data/noBaffles/outletResults0-01.csv")
data5 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/water-water/generalDataAnalysis/data/noBaffles/outletResults0-03.csv")
data6 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/water-water/generalDataAnalysis/data/noBaffles/outletResults0-05.csv")

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

Q1 = cp * density * (temperature1 * velocity1) * area
Q2 = cp * density * (temperature2  * velocity2) * area
Q3 = cp * density * (temperature3 * velocity3) * area
Q4 = cp * density * (temperature4 * velocity4) * area
Q5 = cp * density * (temperature5 * velocity5) * area
Q6 = cp * density * (temperature6 * velocity6) * area


plt.plot(time900, Q3, label='Ushell = 0.01(m/s), Re=1000', color='red')
#plt.plot(time900, Q1, label='Ushell = 0.03 (m/s), Re = 3000', color='green')
#plt.plot(time900, Q2, label='Ushell = 0.05 (m/s), Re = 5000', color='blue')
plt.plot(time900NoBaffles, Q4, label='Ushell = 0.01(m/s), Re = 1000, No Baffles', color='yellow')
#plt.plot(time900, Q5, label='Ushell = 0.03 (m/s), Re = 3000, No Baffles', color='purple')
#plt.plot(time900, Q6, label='Ushell = 0.05 (m/s), Re = 5000, No Baffles', color='orange')


plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Heat Transfer Rate (W)')
plt.title('Heat Transfer Rate')
plt.xticks(range(0, int(max(time900)) + 100, 100))
plt.savefig('/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/water-water/generalDataAnalysis/plots/general/heatTransferRateTotal.png')
plt.show()