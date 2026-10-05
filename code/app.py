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