import os
import pandas as pd
import matplotlib.pyplot as plt

# 魔法代码：强制切换到当前文件所在目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 中文字体设置
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_excel("化工测试数据.xlsx")

# 1. 创建画布和主坐标轴 (ax1)
fig, ax1 = plt.subplots(figsize=(10, 6))

# 2. 绘制左轴：温度（红色实线）
color_temp = 'tab:red'
ax1.set_xlabel('时间 (min)', fontsize=12)
ax1.set_ylabel('温度 (K)', color=color_temp, fontsize=12)    
# marker='o' 表示用圆点标记数据点
ax1.plot(df["时间"], df["温度"], color=color_temp, marker='o', linewidth=2, label='温度')
#.plot()这个是matplotlib中的一个函数，用于绘制折线图，参数包括：x轴数据，y轴数据，颜色，标记，线宽，标签等
ax1.tick_params(axis='y', labelcolor=color_temp)
ax1.grid(True, linestyle='--', alpha=0.5)  # 加个网格，看起来更专业

# 3. 创建副坐标轴 (ax2)，共享 X 轴
ax2 = ax1.twinx()  # twinx 的意思是“双胞胎X轴”，即共享X轴，但独立Y轴

# 4. 绘制右轴：压力（蓝色虚线）
color_pressure = 'tab:blue'
ax2.set_ylabel('压力 (atm)', color=color_pressure, fontsize=12)
# linestyle='--' 表示虚线，marker='s' 表示方形标记
ax2.plot(df["时间"], df["压力"], color=color_pressure, marker='s', linestyle='--', linewidth=2, label='压力') #label:设置图例标签
ax2.tick_params(axis='y', labelcolor=color_pressure)

# 5. 合并图例（把两条线的图例放在一起显示）
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

# 6. 设置全局标题
plt.title("反应器温度与压力随时间变化对比图", fontsize=14, fontweight='bold')

# 7. 显示图片
plt.show()