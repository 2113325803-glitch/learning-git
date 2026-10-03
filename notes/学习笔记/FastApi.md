# FastApi

FastApi 是一个快速、简洁且易于使用的 Python 框架，用于构建 Web 应用程序。它基于 Pydantic，一个用于数据验证和转换的库，提供了强大的类型注解支持。
- 一句话：一个让你用写函数的速度写出一个网站接口的Python工具
- 他可以帮你自动检查数据、自动转成JSON返回

## 安装 FastApi

首先，你需要安装 FastApi 和 Pydantic。你可以使用 pip 来安装它们：

```bash
pip install fastapi uvicorn pydantic
```

## 创建 FastApi 应用

创建一个新的 Python 文件，例如 `main.py`，并编写以下代码：

```python
from fastapi import FastAPI

app = FastAPI()     #建一个“网站”容器

@app.get("/") 
def read_root(数据):
    、、、
    return {"message": "Hello World"}
```

这个代码创建了一个简单的 FastApi 应用，当访问根路径 `/` 时，返回一个 JSON 响应。

## 运行 FastApi 应用

你可以使用 `uvicorn` 来运行 FastApi 应用。在终端中运行以下命令：

```bash
uvicorn main:app --reload
```
这将启动一个开发服务器，并在浏览器中打开 `http://127.0.0.1:8000/`，你应该会看到返回的 JSON 响应。

## 创建 API 路由
你可以使用 `@app.get`、`@app.post`、`@app.put`、`@app.delete` 等装饰器来创建不同的 API 路由。例如：
- `{@app.post("/b")}`:就是"路由"：规定"浏览器/代码发 POST 请求到 /b 这个地方时，就执行下面这个函数"。
- `@app.put("/c")}`:就是"路由"：规定"浏览器/代码发 PUT 请求到 /c 这个地方时，就执行下面这个函数"。
```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q} 
    return {"item_id": item_id}
```
在这个例子中，我们创建了一个名为 `/items/{item_id}` 的路由，它接受一个整数参数 `item_id` 和一个可选的字符串参数 `q`。如果 `q` 存在，返回一个包含 `item_id` 和 `q` 的 JSON 响应；否则，返回一个包含 `item_id` 的 JSON 响应。

## 处理异常
你可以使用 `HTTPException` 来处理异常。例如：
 

## 接口文档

- **接口作用** ：别人（比如前端网页）发一条“实验数据”过来，你的服务器就把这条数据存进Mysql数据库中。
 
- **uvicorn** :启动一个开发服务器，监听8000端口，当有人访问8000端口时，就会执行`main.py`文件中的代码。

- **pydantic** :用于数据验证和转换，比如你定义了一个`ExperimentData`类，pydantic会自动检查你发过来的数据是否符合这个类的定义，如果不符合，就会抛出异常。

- **FastAPI** :是一个快速、简洁且易于使用的Python框架，用于构建Web应用程序。它基于Pydantic，一个用于数据验证和转换的库，提供了强大的类型注解支持。FastAPI可以自动检查数据、自动转成JSON返回。

- **HTTPException** :是指HTTP异常，比如404错误、500错误等。FastAPI可以自动处理HTTP异常，返回相应的HTTP响应。



## 线路运行逻辑

```text
前端/测试代码
   │  发 POST 请求，带一段 JSON（exp_id/温度/压力/催化剂/收率）
   ▼
uvicorn 服务器（8000 端口）
   │  FastAPI 收到请求，找到匹配的路由：/add_experiment
   ▼
你写的函数（Pydantic 帮你检查数据格式对不对，不对直接 400 打回）
   │  逻辑没问题 → 调你写好的 storage.save_experiments()
   ▼
storage.py：pymysql 连 MySQL
   │  把数据 INSERT 进 experiments 表，commit 提交
   ▼
数据库 chemical_lab.experiments 表
   │
   ▼
函数 return {"status":"success"}
   │
   ▼
调用方（前端 / 你的 test_db.py）收到 200 + JSON

```
- 核心一句话：FastAPI 是"前台接待"，负责接电话、验明身份、把话转给真正干活的人（你的数据库函数）；你不用自己写最烦的"接听+格式检查"那部分。