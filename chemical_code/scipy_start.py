import numpy as np
from scipy.optimize import fsolve

def vdw_error(V, P_target, n, T, a, b):
    """
    V: 体积（要求解的未知数）
    P_target: 目标压力 (atm)
    方程：(P + a*n^2/V^2) * (V - n*b) - n*R*T = 0
    """
    R = 0.08206
    # 注意：fsolve要求传入的V是一个数组，我们取V[0]来算
    v = V[0]
    # 返回计算出的压力与目标压力的差值
    P_calc = (n * R * T) / (v - n * b) - (a * n**2) / (v**2)
    return P_calc - P_target


# 2. 给定参数
n = 2.0        # 2 mol
T = 300.0      # 300 K
P = 100.0      # 100 atm
a = 3.592      # CO2 的范德华常数
b = 0.04267

# 3. 给一个初始猜测值（非常重要！通常用理想气体方程算一个起点）
V_guess = (n * 0.08206 * T) / P  # 大概 0.49 L

# 4. 调用 fsolve 求解
# 注意：fsolve 的第二个参数必须是列表或数组，所以传 [V_guess]
V_solution = fsolve(vdw_error, [V_guess], args=(P, n, T, a, b))

#fsolve的参数解释：
#fsolve的第一个参数是目标函数 vdw_error，它接受一个数组 V 作为输入，并返回计算出的压力与目标压力的差值。
#fsolve 的第二个参数是初始猜测值 V_guess，它是一个列表或数组，因为 fsolve 要求传入的 V 是一个数组。
#fsolve 的第三个参数是 args，它是一个元组，包含其他需要传递给目标函数的参数。这里我们传递了 P, n, T, a, b 这些参数。


#fsolve是一个数值优化方法，用于求解非线性方程组。它通过迭代的方法，不断逼近方程的根，直到满足精度要求。
#fsolve 是通过不断“试错（迭代）”找到让 vdw_error 结果为 0 的那个 V。如果遇到不收敛（报错），多半是因为你给的初始猜测值 V_guess 太离谱
print(f"目标压力: {P} atm")
print(f"需要的体积为: {V_solution[0]:.4f} L")

"""fslove 的第二个参数是个数组  数组里面一个猜疑值 对应一个未知数，不能多个猜疑值求
一个未知数

fslove  可以自动确定未知数是谁，用户给定固定值，那么V[0]就是未知数

如果求对个未知数  就需要多个猜疑值，可以用x1=v[0],x2=v[1]表示未知数
guess = [V_guess1, V_guess2]

未知数在第二个参数 长度等于未知数个数
"""




