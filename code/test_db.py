# ==========================================================================
import pytest
import allure
from base_api import BaseApi
from storage import load_experiments

@allure.feature("化工实验数据管理")
@allure.story("新增实验数据接口")
def test_api_add_and_verify(api_base_url):
    """测试：调用 API 添加化工数据，并断言数据库里确实存在"""
    
    # 用 @allure.step 把测试步骤详细记录下来
    with allure.step("1. 初始化 API 机器人"):
        api = BaseApi(api_base_url)
    
    with allure.step("2. 准备测试数据"):
        payload = {
            "exp_id": "ALLURE-001",
            "temperature": 160.0,
            "pressure": 3.0,
            "catalyst": "Allure测试催化剂",
            "yield_rate": 95.5
        }
    
    with allure.step("3. 调用添加接口"):
        response = api.post("/add_experiment", json_data=payload)
    
    with allure.step("4. 断言接口返回"):
        assert response.status_code == 200
        assert response.json()["status"] == "success"
    
    with allure.step("5. 去数据库查账（核心）"):
        db_experiments = load_experiments()
        found = False
        for exp in db_experiments:
            if exp.exp_id == "ALLURE-001":
                assert exp.temperature == 160.0
                assert exp.yield_rate == 95.5
                found = True
                break
        assert found, "数据库里没找到通过 API 插入的数据！"
    
    api.close()