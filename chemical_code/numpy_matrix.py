import numpy as np
"""
数学方程：

2x + 3y = 8 (总物料平衡)

1x - 1y = -1 (组分平衡)

我们可以把方程组写成矩阵的形式：AX = B
A = [[2, 3], [1, -1]]，X = [[x], [y]]，B = [[8], [-1]]


"""
A = np.array([
    [2.0,3.0],
    [1, -1.0]
    
])
B = np.array([8.0, -1.0])

X = np.linalg.solve(A, B)   # 解方程组AX = B

print("方程组的解 X:")
print(f"x = {X[0]:.2f}")
print(f"y = {X[1]:.2f}")
B_check = A @ X
print("验证 A @ X =", B_check)