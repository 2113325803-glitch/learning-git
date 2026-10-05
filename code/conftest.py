import pytest

# 全局公共配置：服务器基础地址
BASE_URL = "http://127.0.0.1:8000"

@pytest.fixture(scope="session")   # 会话级别：在所有测试用例执行之前执行一次
def api_base_url():
    """"
    提供所有测试用例使用的全局基础
    """
    return BASE_URL


