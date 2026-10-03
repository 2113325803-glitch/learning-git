# 【化工数字化】模块二：多组实验数据的自动化可视化（Pandas + Matplotlib）

> **笔记定位**：掌握从数据库读取多组数据，利用 Pandas 进行分组筛选与排序，最终用 Matplotlib 生成多组对比图的全链路自动化逻辑。

---

## 🎯 一、业务目标与场景
在化工研发中，我们需要对比不同催化剂（或不同反应条件）对产品收率的影响。
- **输入**：MySQL 数据库中存储的原始实验记录。
- **处理**：按“催化剂种类”分组，按“温度”升序排列，剔除乱序数据。
- **输出**：一张包含多条折线（不同颜色）的对比趋势图，并自动保存为图片。

---

## 🧠 二、核心程序思路（Data Pipeline 数据流水线）
**核心思想**：拒绝硬编码（不写死画几条线），利用循环动态感知数据的组别，实现代码的高可扩展性。

 ```mermaid
 graph TD
    A[MySQL 数据库] -->|读取| B[Python 对象列表]
    B -->|转换为字典列表| C[Pandas DataFrame]
    C -->|提取分组依据| D[获取所有催化剂种类 .unique]
    D -->|循环遍历 enumerate| E[布尔索引筛选 df_df条件]
    E -->|排序 sort_values| F[提取 X/Y 轴数据]
    F -->|绘制 plt.plot| G[多条对比折线图]
    G -->|保存 savefig| H[生成 PNG 图片并展示]
    
```

## 三、数据结构演变（语言逻辑底层）

### 1.原始形态：Python对象列表
```python
[Experiment(exp_id='A-120', temperature=120.0, yield_rate=65.0, catalyst='催化剂A'), 
 Experiment(exp_id='A-140', temperature=140.0, yield_rate=78.5, catalyst='催化剂A'), ...]
```
特点：面向对象，通过.属性访问，但很难按“列”批量处理

### 2.过渡形态：字典列表
```python
[{'exp_id': 'A-120', 'temperature': 120.0, 'yield_rate': 65.0, 'catalyst': '催化剂A'}, 
{'exp_id': 'A-140', 'temperature': 140.0, 'yield_rate': 78.5, 'catalyst': '催化剂A'}, ...]
```
特点：字典的key将可以直接成为Pandas表格的列名

### 3.最终形态：Pandas DataFrame
```test
+--------+--------+--------+
| 温度(℃) | 收率(%) | 催化剂|
+--------+--------+--------+
| 120.0  | 65.0   | 催化剂A |
| 140.0  | 78.5   | 催化剂A |
| 120.0  | 80.0   | 催化剂B |
+--------+--------+--------+
```
特点：DataFrame支持多列操作，如分组、排序、筛选等，便于后续数据处理
```python
df = pd.DataFrame(data=experiments, columns=['exp_id', 'temperature', 'yield_rate', 'catalyst'])
```
特点：Pandas DataFrame支持多列操作，如分组、排序、筛选等，便于后续数据处理

## 四、核心语法用法与语言逻辑

### 1.Pandas基础操作

| 语法 | 作用 | 备注 |
|------|-----|------|
| `pd.DataFrame(data=experiments, columns=['exp_id', 'temperature', 'yield_rate', 'catalyst'])` | 创建DataFrame | 从字典列表创建DataFrame |
| `df['catalyst'].unique()` | 获取所有催化剂种类 | 返回一个数组，包含所有唯一的催化剂种类 |
| `df.sort_values(by='temperature')` | 按温度升序排序 | 通过by参数指定排序依据 |
| `df[df['catalyst'] == '催化剂A']` | 筛选特定催化剂的数据 | 通过布尔索引筛选数据 |
| `df.groupby('catalyst')['yield_rate'].mean()` | 按催化剂分组并计算平均收率 | 使用groupby方法按列分组，然后使用agg方法计算平均值 |

### 2.python基础语法

| 语法 | 作用 | 备注 |
|------|-----|------|
| `enumerate(D)` | 获取所有催化剂种类及其索引 | 返回一个枚举对象，包含每个催化剂种类及其索引 |
| `for i, catalyst in enumerate(D)` | 循环遍历催化剂种类及其索引 | 使用enumerate函数遍历字典，获取每个催化剂种类及其索引 |
| `plt.plot(x, y, label='催化剂A')` | 绘制折线图 | 使用plt.plot函数绘制折线图，并添加标签 |

### 3.Matplotlib基础操作

| 语法 | 作用 | 备注 |
|------|-----|------|
| `plt.figure(figsize=(10, 6))` | 创建图形窗口 | 使用plt.figure函数创建图形窗口，并设置窗口大小 |
| `plt.xlabel('温度')` | 设置X轴标签 | 使用plt.xlabel函数设置X轴标签 |
| `plt.ylabel('收率')` | 设置Y轴标签 | 使用plt.ylabel函数设置Y轴标签 |
| `plt.legend()` | 显示图例 | 使用plt.legend函数显示图例 |
| `plt.savefig('对比趋势图.png')` | 保存图形 | 使用plt.savefig函数保存图形，并指定文件名 |
| `plt.show()` | 显示图形 | 使用plt.show函数显示图形 |
| `plt.plot(x, y, color='red', linestyle='--', marker='o')` | 绘制折线图 | 使用plt.plot函数绘制折线图，并设置颜色、线型和标记 |
| `plt.grid(True, linestyle='--', color='gray')` | 显示网格 | 使用plt.grid函数显示网格，并设置线型和颜色 |

## 五、代码实现

1. **读取数据**：从MySQL数据库中读取实验记录。
2. **转换数据**：将读取的数据转换为字典列表。
3. **处理数据**：按“催化剂种类”分组，按“温度”升序排列，剔除乱序数据。
4. **绘制图表**：绘制多条对比折线图，并保存为图片。


```python
import matplotlib.pyplot as plt          #这句导入matplotlib.pyplot库，用于绘图
import pandas as pd                       #这句导入pandas库，用于数据处理
from storage import load_experiments       # 这句导入storage模块中的load_experiments函数，用于从数据库加载实验数据

# 1. 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']         # 设置字体为SimHei，解决中文乱码问题
plt.rcParams['axes.unicode_minus'] = False          # 解决负数的中文乱码问题

# 2. 从数据库加载数据
experiments = load_experiments()
data = []
for exp in experiments:              # 遍历每个实验数据，将数据转换为字典格式，便于后续处理
    data.append({            #
        "温度(℃)": exp.temperature,
        "收率(%)": exp.yield_rate,
        "催化剂": exp.catalyst
    })

df = pd.DataFrame(data)        # 将数据转换为DataFrame格式
#DataFrame格式：{'温度(℃)': [25, 30, 35, 40, 45], '收率(%)': [80, 85, 90, 95, 100], '催化剂': ['催化剂A', '催化剂A', '催化剂A']}

# 3. 画图准备
plt.figure(figsize=(10, 6))     # 设置图形大小
#figsize=(10, 6)：设置图形大小为10x6英寸

# 4. 按“催化剂”分组，分别画线          unique()：返回所有唯一的催化剂种类
catalysts = df["催化剂"].unique()  # 拿到所有催化剂的种类：['催化剂A', '催化剂B']
colors = ['blue', 'red']  # 为不同的线指定颜色

for i, catalyst in enumerate(catalysts):          # 遍历每个催化剂     enumerate()：返回索引和值
    # 筛选出当前催化剂的数据，并按温度排序
    group = df[df["催化剂"] == catalyst].sort_values(by="温度(℃)")

    # 画线
    plt.plot(
        group["温度(℃)"],
        group["收率(%)"],
        marker='o',
        color=colors[i],
        linewidth=2,
        label=catalyst  # 图例名称
    )

# 5. 配置图表
plt.title("不同催化剂的温度-收率对比图", fontsize=16)
plt.xlabel("温度 (℃)", fontsize=12)
plt.ylabel("收率 (%)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()  # 显示图例

# 6. 保存并展示
plt.savefig("catalyst_comparison.png")
plt.show()
print("对比图已生成并保存为 catalyst_comparison.png")
               
                
```


### 2. 数据库连接与数据读取

```python
import mysql.connector

def load_experiments():
    # 连接数据库
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password',
        database='your_database'
    )
    cursor = conn.cursor()

    # 查询实验数据
    cursor.execute("SELECT exp_id, temperature, pressure, catalyst, yield_rate FROM experiments")
    experiments = cursor.fetchall()


```
### 3.Experiment 数据模型类定义（面向对象封装）

```python
class Experiment:
    def __init__(self, exp_id, temperature, pressure, catalyst, yield_rate, id=None):
        self.id = id
        self.exp_id = exp_id            # 实验编号
        self.temperature = temperature  # 温度 (℃)
        self.pressure = pressure        # 压力 (MPa)
        self.catalyst = catalyst        # 催化剂名称
        self.yield_rate = yield_rate    # 收率 (%)

    def __str__(self):
        return f"实验[{self.exp_id}] 温度:{self.temperature}℃ 压力:{self.pressure}MPa 催化剂:{self.catalyst} 收率:{self.yield_rate}%"


```

## 六、总结与反思（经验之谈）

### 1. 数据预处理

- 确保数据库中数据的完整性，避免缺失值或异常值影响分析结果。
- 对数据进行清洗和预处理，如去除重复数据、处理异常值等，以提高分析的准确性和可靠性。

### 2. 图表美化

- 使用合适的图表类型，如折线图、柱状图、散点图等，根据数据特点选择合适的图表类型。
- 添加图表标题、标签和图例，提高图表的可读性和可理解性。
- 调整图表的大小和布局，确保图表的美观性和可读性。
- 使用颜色和线型等视觉元素，区分不同组别和数据点，提高图表的对比度和可读性。
- 使用网格和坐标轴，提高图表的可读性和可理解性。
- 使用注释和说明，提高图表的可读性和可理解性。
- 使用图表工具和库，提高图表的生成效率和质量。
- 使用图表库的高级功能，如动态图表、交互图表、动画图表等，提高图表的交互性和动态性。
- 使用图表库的高级功能，如数据可视化、数据挖掘、数据建模等，提高图表的分析和决策能力。


### 3. 数据库连接与数据读取
- 确保数据库连接的参数正确，避免连接失败或数据读取错误。
- 使用数据库连接池，提高数据库连接的效率和性能。
- 使用数据库连接的上下文管理器，自动管理数据库连接的打开和关闭。
- 使用数据库连接的事务管理，确保数据的一致性和完整性。
- 使用数据库连接的缓存机制，提高数据读取的效率和性能。
- 使用数据库连接的监控和日志记录，提高数据库连接的监控和日志记录能力。
- 使用数据库连接的性能调优策略，提高数据库连接的性能调优能力。

## 七、避坑与注意事项

1.排序是铁律：画折线图前，必须对 X 轴数据（温度）执行 sort_values()。如果数据库数据是乱序的，折线图会变成来回折返的“蜘蛛网”。

2.先存后展：plt.savefig() 一定要写在 plt.show() 前面，否则保存下来是一张白图（画布已被清空）。

3.环境隔离原则：新建项目（如 chemical_lab）必须重新 pip install pandas matplotlib，虚拟环境之间互不干扰。

4.动态颜色分配：利用 enumerate 的索引 i 去取 colors[i]，这样即使后面增加了 10 种催化剂，代码也只需修改 colors 列表，无需改动绘图逻辑。

## 八、大厂面试话术与扩展

面试话术：
“在处理多组化工实验数据对比时，我采用了 Pandas 的布尔索引和排序功能进行数据预处理。通过循环遍历 .unique() 提取的组别，实现了多组折线图的动态绘制，彻底避免了硬编码带来的维护成本，提升了代码的可扩展性。”

扩展：
- 在化工研发中，除了对比不同催化剂对产品收率的影响，还可以对比不同反应条件（如温度、压力、反应时间等）对产品收率的影响。