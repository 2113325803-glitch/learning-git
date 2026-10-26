import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. 页面基本设置（写在最上面）
# 提示：st.set_page_config(page_title="...", layout="wide")
st.set_page_config(page_title="化工数字孪生控制台", layout="wide")

# 2. 缓存模型训练（避免每次拖滑块都重新训练）
# 提示：使用 @st.cache_resource 装饰器
@st.cache_resource
def train_model():
    # 这里用之前的随机数据模拟训练过程
    np.random.seed(42)
    X = np.random.rand(100, 2) * [50, 1] + [100, 0]  # 温度100-150，压力0-1
    # 假设真实规律
    y = 0.9 - 0.002 * X[:, 0] + 0.1 * X[:, 1]
    model = LinearRegression()
    model.fit(X, y)
    return model

# 加载模型
model = train_model()

# 3. 网页布局
st.title("🏭 反应器软测量与数字孪生监控大屏")
st.markdown("---")

# 左侧侧边栏输入
st.sidebar.header("工艺参数输入")
# 提示：使用 st.sidebar.slider() 让用户输入温度和压力
temp = st.sidebar.slider("反应器温度 (℃)", min_value=100.0, max_value=150.0, value=120.0)
press = st.sidebar.slider("反应器压力 (MPa)", min_value=0.0, max_value=1.0, value=0.5)

# 4. 实时预测与显示
# 将输入数据整理成二维数组
input_data = np.array([[temp, press]])
prediction = model.predict(input_data)[0]

# 在网页上显示结果
st.subheader("AI 软测量预测结果")
# 提示：使用 st.metric 显示数字
st.metric(label="预测产品纯度", value=f"{prediction:.2%}")

# 5. 异常报警逻辑
if prediction < 0.85:
    # 提示：使用 st.error 显示红色错误框
    st.error("⚠️ 警告：预测纯度低于工艺设定值（85%），请检查操作参数！")
else:
    st.success("✅ 工况正常，纯度达标。")