import pandas as pd


#1.准备数据
data = [
    {"催化剂": "A", "温度": 120, "收率": 65},
    {"催化剂": "A", "温度": 140, "收率": 78},
    {"催化剂": "A", "温度": 160, "收率": 92},
    {"催化剂": "B", "温度": 120, "收率": 80},
    {"催化剂": "B", "温度": 140, "收率": 95},
    {"催化剂": "B", "温度": 160, "收率": 85},
    {"催化剂": "C", "温度": 140, "收率": 70},
    {"催化剂": "C", "温度": 160, "收率": 88},
]
df = pd.DataFrame(data)
#解释这句话:
# data - 是一个包含字典的列表，每个字典代表一条数据
# df = pd.DataFrame(data) - 将列表转换为DataFrame对象，DataFrame是一个二维的表格数据结构，可以进行各种数据操作



print("====原始数据====")
print(df)
print("\n====按温度筛选=====")
print(df[df['温度'] > 140])

#2.分组聚合
#按"催化剂"分组,统计"收率"的平均值,最大值,最小值
summary = df.groupby("催化剂")["收率"].agg(["mean", "max", "min"])
#解释这句话:
# df.groupby("催化剂") - 按"催化剂"列进行分组
# ["收率"] - 选择"收率"列
# .agg(["mean", "max", "min"]) - 对选中的列进行聚合操作，计算平均值、最大值和最小值

print("\n====分组聚合结果====") 
print(summary)

#3.排序
#按"平均收率"降序排序
summary_sorted = summary.sort_values(by="mean", ascending=False)
#解释这句话:
# summary.sort_values(by="mean", ascending=False) - 按"mean"列进行排序，降序排列
# by="mean" - 按"mean"列进行排序   升序排列: ascending=True, 降序排列: ascending=False
#.sort_values() - 排序函数

print("\n====按收率降序排序结果====")
print(summary_sorted)

