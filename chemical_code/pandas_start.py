import pandas as pd
import numpy as np

# # 告诉 Pandas：中文字符的宽度是英文字符的两倍，请按真实宽度对齐
# pd.set_option('display.unicode.east_asian_width', True)
# pd.set_option('display.width', 1000) # 如果列太多，加宽显示区域

# #===============构造数据=====================================
# data = {                                         #字典里面是键：值    可以通过键来找值，键可以是字符串、数字、列表、元组等
#     "时间(min)": [0,1, 2, 3, 4],                   #值可以是列表、元组、字典、Series等
#     "反应器编号":["R-101","R-101", "R-101", "R-101", "R-101"],
#     "温度(K)":[300.0, 310.5, np.nan, 330.2, 340.0],#第三分钟的传感器故障，数据丢失
#     "压力(atm)":[1.0, 1.2, 1.5, 1.8, 2.0],
#     "进料流量(L/min)":[10.0, 10.2, 10.1, 10.0, 9.9]
    
# }

# #将字典转换为Pandas的dataframe
# df = pd.DataFrame(data)
# print("原始数据：")
# print(df)

# # ================= 2. 数据探查（拿到数据先看基本信息） =================
# print("\n====== 2. 数据基本信息 ======")
# print(f"数据形状（行,列）: {df.shape}")   
# print("\n每列的数据类型和非空数量:")
# print(df.info())


# #=============3. 数据清洗（核心！处理缺失值）================
# print("\n====== 3. 清洗缺失值 ======")
# # 真实车间里，传感器丢数据是常态。我们通常用“前一个有效值”或者“平均值”来填充
# # 这里用“前向填充”（用上一分钟的温度顶替这一分钟）
# df["温度(K)"] = df["温度(K)"].ffill()            # 用np.nan  来告诉.ffill()这是个缺失值， 用上一分钟的温度顶替这一分钟
# print("填充后的温度列：")
# print(df["温度(K)"])

# # ================= 4. 条件筛选（找异常工况） =================
# print("\n====== 4. 筛选高压工况 ======")
# # 找出压力大于 1.5 atm 的时间点
# high_pressure_condition = df["压力(atm)"] > 1.5
# high_pressure_df = df[high_pressure_condition]
# print(high_pressure_df)

# # ================= 5. 统计与聚合（写日报必备） =================
# print("\n====== 5. 统计汇报数据 ======")
# avg_temp = df["温度(K)"].mean()
# max_pressure = df["压力(atm)"].max()
# print(f"平均温度: {avg_temp:.2f} K")
# print(f"最高压力: {max_pressure:.2f} atm")

# #===============加了excel表===================

# 注意前面加个小写字母 r，防止 Windows 路径里的反斜杠报错
df_excel = pd.read_excel(r"D:\Users\21133\Documents\GitHub\learning-git\chemical_code\化工测试数据.xlsx")
print(df_excel.head(12))


# print("\n====== 分组统计：每台反应器的平均温度 ======")
# # groupby 的意思是：按“反应器编号”把数据切分成几个小组，然后对“温度”求平均
# avg_temp_by_reactor = df_excel.groupby("反应器编号")["温度"].mean()
# print(avg_temp_by_reactor)

# print("\n====== 分组统计：每台反应器的最高压力 ======")
# max_pressure_by_reactor = df_excel.groupby("反应器编号")["压力"].max()
# print(max_pressure_by_reactor)

# result = df_excel.groupby("反应器编号")[["温度", "压力"]].mean().reset_index()
# print(result)
# #reset_index() 的作用就是：“把索引打回原形，变成普通的一列”。这样 result 就和原来的 DataFrame 一模一样整齐了，拿出去写报告更方便。




# 第一句：不重置索引（反应器编号变成行标签）
result_with_index = df_excel.groupby("反应器编号")[["温度", "压力"]].mean()
print("====== 带索引的表格 ======")
print(result_with_index)
print(f"索引名字是: {result_with_index.index.name}") # 看看行标签叫什么

# 第二句：重置索引（反应器编号变回普通列）
result_normal = df_excel.groupby("反应器编号")[["温度", "压力"]].mean().reset_index()
print("\n====== 重置索引后的表格 ======")
print(result_normal)


















