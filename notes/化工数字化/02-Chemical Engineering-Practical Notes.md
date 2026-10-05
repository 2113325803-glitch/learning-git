#  🥽 化工数字化项目实战笔记

## 模块一： Python 基础与 OOP（化工实验数据建模）
### 1.核心概念
- 类与对象：类是“化工图纸”，对象是“化工实验数据”。
- 继承与魔术方法： '__init__'初始化，'__str__'打印，'__repr__'表示，'__add__'加法，'__sub__'减法，'__mul__'乘法，'__truediv__'除法，'__eq__'等于，'__ne__'不等于，'__lt__'小于，'__le__'小于等于，'__gt__'大于，'__ge__'大于等于。
### 2. 语法速查（字典式记录）
| 方法/语句 | 作用 | 示例 |
|-----------|------|------|
|`class Experiment:`|定义化工实验类|`class Experiment:`|
|`def __init__(self, name, data):`|初始化实验数据|`def __init__(self, name, data):`|
|`self.name = name`|设置实验名称|`self.name = name`|
|`self.data = data`|设置实验数据|`self.data = data`|
|`def __str__(self):`|打印实验数据|`def __str__(self):`|

### 3.数据结构
- **字典（dict）**: `{"温度": 150, "压力": 2.5}`,用于临时组装数据传给pandas。
- **列表（list）**: `["温度", "压力"]`,用于存储实验数据的名称。或者`["实验1", "实验2", "实验3"]`,用于存储多个实验数据的名称。
  
- **元组（tuple）**: `("温度", "压力")`,用于存储实验数据的名称。

### 4.踩坑记录
- [ ] `self` 绝对不能漏写，方法第一个参数永远是 `self`,表示当前对象。
- [ ] `__init__` 方法必须有参数 `self`，否则无法实例化对象。
- [ ] `__str__` 方法必须返回一个字符串，否则无法打印对象。
- [ ] `__repr__` 方法必须返回一个字符串，否则无法表示对象。
- [ ] `__add__` 方法必须返回一个对象，否则无法进行加法运算。
- [ ] `__sub__` 方法必须返回一个对象，否则无法进行减法运算。

## 模块二： MySQL 数据库 （化工数据持久化）

### 1. 核心概念

- 主键 (PRIMARY KEY)：唯一标识一条实验记录。
- 事务 (Transaction):`connect.commit()` 才是真正写入硬盘。
- 查询 (Query): `cursor.execute("SELECT * FROM experiments")` 才是真正从硬盘读取数据。
- 插入 (Insert): `cursor.execute("INSERT INTO experiments (name, data) VALUES (%s, %s)", (name, data))` 才是真正写入硬盘。

### 2. 语法速查
| 类别 | SQL 语句 | 备注 |
|------|----------|------|
| DDL | `CREATE TABLE experiments (...)` | 建表 |
| DML | `INSERT INTO experiments (...) VALUES (...)` | 插入 |
| DQL | `SELECT * FROM experiments WHERE yield_rate > 80` | 条件查询 |
| DML | `UPDATE experiments SET yield_rate = 85 WHERE name = '实验1'` | 更新 |
| DML | `DELETE FROM experiments WHERE name = '实验1'` | 删除 |
| DDL | `ALTER TABLE experiments ADD COLUMN new_column_name TYPE` | 添加列 |


### 3. 逻辑流转
Python 代码 -> `pymysql.connect()` -> `cursor.execute(SQL)` -> `conn.commit()` -> `cursor.close()` -> `conn.close()`。

### 4. 踩坑记录
- [ ] 密码必须换成自己的（本地学习环境），且不能明文提交到 GitHub。
- [ ] `DELETE/UPDATE/INSERT` 必须 `commit()`。
- [ ] 数据库连接必须在 `charset` 指定 `utf8mb4` 防止中文乱码。

## 模块三：Pandas 数据分析（化工数据清洗）
### 1. 核心概念
- DataFrame：内存里的“Excel 表格”。
- 数据清洗：剔除收率 < 0 或 > 100 的异常实验值。

### 2. 语法速查
| 操作 | 语法 | 示例 |
|------|------|------|
| 创建 | `pd.DataFrame(list_of_dicts)` | `df = pd.DataFrame(data)` |
| 筛选 | `df[df["列名"] 条件]` | `df[df["收率(%)"] > 80]` |
| 统计 | `.mean()`, `.max()` | `df["收率(%)"].mean()` |

### 3. 避坑记录
- [ ] Windows 终端打印中文表格会错位，必须加 `pd.set_option('display.unicode.east_asian_width', True)`。


```mermaid
graph TD
    A[用户在终端输入: 温度, 压力] --> B[Python 创建 Experiment 对象]
    B --> C[调用 storage.save_experiments]
    C --> D[执行 SQL: DELETE 清空旧表 + INSERT 插入新数据]
    D --> E[conn.commit 落盘]
    E --> F[返回提示: 添加成功]










