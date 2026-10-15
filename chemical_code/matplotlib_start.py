import os
import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签（SimHei是黑体）
plt.rcParams['axes.unicode_minus'] = False    # 解决负号无法显示的问题



# ================= 魔法代码开始 (保证Python每次运行时，工作目录都是这个文件夹)===================
# 获取当前这个 .py 文件所在文件夹的绝对路径
current_folder = os.path.dirname(os.path.abspath(__file__))
# 强制把终端的工作目录切换到这个文件夹
os.chdir(current_folder)
# ================= 魔法代码结束 =================

# 1. 必须先读取你的数据
df = pd.read_excel("化工测试数据.xlsx")


# 2.准备数据：按反应器编号分组，算出平均温度，并重置索引变成普通列
rus = df.groupby("反应器编号")["温度"].mean().reset_index()

# 3. 创建画布
plt.Figure(figsize=(8,5))  #宽是8，高是5

# 4. 画折线图

plt.plot(rus["反应器编号"],rus["温度"],marker="o",linestyle="-",color="blue")

# 5. 加装饰器：添加标题、x轴标签、y轴标签 网格
plt.title("各反应器平均温度对比图",fontsize=14)
plt.xlabel("反应器编号",fontsize=12)
plt.ylabel("温度(℃)",fontsize=12)
plt.grid(True,linestyle="--",alpha=0.7)


# 6. 显示图片
plt.show()