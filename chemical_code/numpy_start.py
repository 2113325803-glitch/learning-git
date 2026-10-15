import numpy as np 
T_array = np.array([300.0,320.0,340.0,360.0,380.0])
print("温度数组：",T_array)
print(f"温度数组：{T_array}")

n = 1.0
v = 10.0
R = 0.08206

P_array = (n * T_array * R) / v
print("压力数组：",P_array)
print(f"压力数组：{P_array}")
print(f"最大压力：{np.max(P_array)}")
print(f"最小压力：{np.min(P_array)}")
print(f"平均压力：{np.mean(P_array)}")


T_subset = T_array[:3]
print("前三个温度子数组：",T_subset)
print(f"子数组：{T_subset}")

H_pressure = P_array[P_array > 100.0]
print("大于100的压力子数组：",H_pressure)
print(f"子数组：{H_pressure}")

print("温度数组的长度：",len(T_array))
print("温度数组的维度：",T_array.ndim)
print("温度数组的形状：",T_array.shape)