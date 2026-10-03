#用代码发请求 → 检查返回是否成功 → 再翻数据库确认数据真的写进去了。
# 这比手动点 ApiFox 靠谱的地方：以后代码一改，
# 运行一遍 pytest 就能自动测，不用每次手动戳。
import pytest  #pytest 是测试框架，专门用来跑“测试函数”（function名以test_开头就会被自动执行）
import requests #requests 是 HTTP 客户端库，专门用来发送 HTTP 请求
#相当于“代码版的Apifox”
from storage import load_experiments

# 你的 FastAPI 服务地址（uvicorn 启动后就是它）
#这个是接口地址
API_URL = "http://127.0.0.1:8000/add_experiment"
#

def test_api_add_and_verify():
    """测试：调用 API 添加化工数据，并断言数据库里确实存在"""
    # 1. 准备测试数据
    payload = {
        "exp_id": "API-CHEM-001",
        "temperature": 150.0,
        "pressure": 2.5,
        "catalyst": "API测试催化剂",
        "yield_rate": 88.8
    }

    # 2. 调用接口（发 POST 请求）
    response = requests.post(API_URL, json=payload)

    # 3. 断言接口返回成功
    assert response.status_code == 200
    assert response.json()["status"] == "success"

    # 4. 去数据库里“查账”（大厂测试开发核心技能）
    db_experiments = load_experiments()
    found = False
    for exp in db_experiments:
        if exp.exp_id == "API-CHEM-001":
            assert exp.temperature == 150.0
            assert exp.yield_rate == 88.8
            found = True
            break
    assert found, "数据库里没找到通过 API 插入的数据！"