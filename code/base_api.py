import requests

class BaseApi:
    def __init__(self, base_url):       # 初始化时传入基础 URL
        self.base_url = base_url
        # 使用 Session 保持会话，提高性能
        self.session = requests.Session()

    def post(self, path, json_data=None):    
        """封装 POST 请求，自动拼接 URL"""
        url = f"{self.base_url}{path}"
        response = self.session.post(url, json=json_data)
        return response

    def get(self, path, params=None):   
        """封装 GET 请求"""
        url = f"{self.base_url}{path}"
        response = self.session.get(url, params=params)
        return response

    def close(self):
        self.session.close()