import numpy as np
v_array = np.array([5.0,10.0,15.0,20.0])

n = 2.0
T = 350.0
R = 0.08206

P_array = (n * R * T ) / v_array
h_array = P_array[P_array > 5.0]
print(f"Pressure greater than 5.0 atm: {h_array} atm")
print()
avg_pressure = np.mean(P_array)
print(f"Average pressure: {avg_pressure} atm")

