import pytest
from base_api import BaseApi

def test_predict_optimal(api_base_url):
    """测试：调用预测接口，验证返回的最优温度和收率"""
    api = BaseApi(api_base_url)
    payload = {"catalyst": "催化剂A"}
    
    response = api.post("/predict_optimal", json_data=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    # 断言返回的基本信息
    assert data["status"] == "success"
    assert data["catalyst"] == "催化剂A"
    
    # 断言预测结果在合理的化工范围内
    assert 100 < data["optimal_temp"] < 200   # 温度在 100-200℃ 之间
    assert 0 < data["optimal_yield"] <= 100   # 收率在 0-100% 之间
    
    print(f"预测成功：最优温度 {data['optimal_temp']}℃，最高收率 {data['optimal_yield']}%")
    api.close()