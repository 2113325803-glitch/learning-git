from fastapi import FastAPI      #Fast用于快速搭建Web接口（就是“网址+“接口”的读物）
from pydantic import BaseModel     #这个pydantic是一个用于数据验证和转换的库
from storage import save_experiments, load_experiments
from models import Experiment #这个Experiment是用来定义实验数据的模型的

app = FastAPI()     #用来启动服务的 （相当于启动一个服务器，创建一个应用实例，后边的接口都挂在它的上面）

class ExperimentModel(BaseModel):      #用
    exp_id: str              #实验编号
    temperature: float    #温度（小数）
    pressure: float        #压力（小数）
    catalyst: str              #催化剂（字符串）
    yield_rate: float         #产率（小数）

@app.post("/add_experiment")       #当人往/add_experiment这个接口发送POST请求时就
#运行/调用add_experiment（下面的函数）函数
def add_experiment(exp: ExperimentModel):
    """接收化工数据，写入数据库"""
    experiments = load_experiments()
    experiments.append(Experiment(
        exp_id=exp.exp_id, temperature=exp.temperature,
        pressure=exp.pressure, catalyst=exp.catalyst, yield_rate=exp.yield_rate
    ))
    save_experiments(experiments)   #这个函数是用来将实验数据写入数据库
    return {"status": "success", "message": "化工实验数据添加成功"}

#总的来说：Apifox通过POST请求向/add_experiment接口发送数据，
# FastAPI接收数据并调用add_experiment函数，add_experiment函数将数据写入数据库
# ，最后Apifox返回成功信息。这样就实现了化工数据的添加功能。
import numpy as np
from scipy.optimize import curve_fit

# 定义抛物线方程（和之前本地脚本里一样）
def parabola(x, a, b, c):
    return a * x**2 + b * x + c

class PredictRequest(BaseModel):
    catalyst: str  # 前端传过来要预测的催化剂名称

@app.post("/predict_optimal")
def predict_optimal(request: PredictRequest):
    """接收催化剂名称，从数据库取数，拟合后返回最优温度"""
    # 1. 从数据库取出该催化剂的所有实验数据
    experiments = load_experiments()
    target_data = [exp for exp in experiments if exp.catalyst == request.catalyst]
    
    if len(target_data) < 3:
        return {"status": "error", "message": "数据不足，至少需要3组实验数据才能拟合"}
    
    x_data = np.array([exp.temperature for exp in target_data])
    y_data = np.array([exp.yield_rate for exp in target_data])
    
    # 2. 数学拟合（沿用你的 Scipy 逻辑）
    popt, _ = curve_fit(parabola, x_data, y_data)
    a, b, c = popt
    
    # 3. 计算最优温度和理论最高收率
    optimal_temp = -b / (2 * a)
    optimal_yield = parabola(optimal_temp, *popt)
    
    # 4. 把结果包装成 JSON 返回给前端
    return {
        "status": "success",
        "catalyst": request.catalyst,
        "optimal_temp": round(optimal_temp, 2),
        "optimal_yield": round(optimal_yield, 2)
    }