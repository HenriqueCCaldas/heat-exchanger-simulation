import pandas as pd
import matplotlib.pyplot as plt
import math as math 

# Read the CSV file into a pandas DataFrame
data1 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/results/generalDataAnalysis/data/outletResults0-01_900.csv")
data2 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/results/generalDataAnalysis/data/outletResults0-03_900.csv")
data3 = pd.read_csv("/media/henrique/Elements/heatExchangerSimulation/shellTubeHEX/transient/results/generalDataAnalysis/data/outletResults0-05_900.csv")

# Extract the temperature column from the DataFrame
temperature1 = data1["avg(T)"]
temperature2 = data2["avg(T)"]
temperature3 = data3["avg(T)"] 

velocity1 = data1["avg(U (Magnitude))"]
velocity2 = data2["avg(U (Magnitude))"]
velocity3 = data3["avg(U (Magnitude))"]

#time300 = data1["Time"]
time900 = data3["Time"]

cp = 4179 # J/kg*K
density = 995.7 # kg/m^3
area = 0.04 * 0.04 * math.pi  # m^2

Q1 = cp * density * (temperature1 * velocity1) * area
Q2 = cp * density * (temperature2  * velocity2) * area
Q3 = cp * density * (temperature3 * velocity3) * area


plt.plot(time900, Q3, label='Ushell = 0.01(m/s)', color='red')
#plt.plot(time900, Q1, label='Ushell = 0.05 (m/s)', color='green')
#plt.plot(time900, Q2, label='Ushell = 0.1 (m/s)', color='blue')


plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Heat Transfer Rate (W)')
plt.title('Heat Transfer Rate')

plt.show()