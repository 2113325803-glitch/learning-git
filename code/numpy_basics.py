import numpy as np

# ============ 1. 创建数组的三种方式 ============

# 方式一：从 Python 列表创建
temperatures = np.array([120.0, 140.0, 160.0, 180.0, 200.0])   #array() 会自动推断数据类型
print("温度数组:", temperatures)
print("数据类型:", temperatures.dtype)  # 自动推断为 float64

# 方式二：生成等差数列（化工里做温度梯度实验常用）
temps = np.linspace(100, 200, 11)  # 从100到200，等分11个点 
print("温度梯度:", temps)

# 方式三：生成全 0、全 1 数组
zeros = np.zeros((3, 4))  # 3行4列全0矩阵
print("全0矩阵:\n", zeros)

# ============ 2. 数组运算（元素级运算，比for循环快100倍） ============

yields = np.array([65.0, 78.5, 92.0, 89.0, 75.0])

# 全部加10，不写for循环！
yields_plus = yields + 10
print("收率+10:", yields_plus)

# 全部求平方（用于计算方差）
yields_squared = yields ** 2
print("收率平方:", yields_squared)

# 两个数组对应元素相加
another = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
print("两个数组相加:", yields + another)

# ============ 3. 统计计算（化工数据分析常用） ============

print("平均收率:", np.mean(yields))
print("最大收率:", np.max(yields))
print("最小收率:", np.min(yields))
print("标准差:", np.std(yields))       # 反映数据的离散程度
print("方差:", np.var(yields))         # 标准差的平方

# ============ 4. 索引与切片（跟列表类似） ============

print("第一个温度:", temperatures[0])
print("最后一个温度:", temperatures[-1])
print("前三个温度:", temperatures[:3])
print("反转数组:", temperatures[::-1])

# ============ 5. 布尔索引（超强功能！） ============

# 找出收率大于80的数据
high_yield = yields[yields > 80]
print("收率>80的实验:", high_yield)

# 同时满足多个条件
good = yields[(yields > 75) & (yields < 95)]
print("75<收率<95的数据:", good)