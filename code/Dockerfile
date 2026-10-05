# 1. 指定基础镜像：使用官方提供的轻量级 Python 3.13 环境
FROM python:3.13-slim

# 2. 设置容器内的工作目录（相当于进到某个文件夹）
WORKDIR /app

# 3. 复制依赖清单（为了利用 Docker 的缓存机制）
COPY requirements.txt .

# 4. 安装依赖（因为国内网络，可以加上清华源加速）
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 5. 把当前目录下的所有代码复制进容器
COPY . .

# 6. 暴露端口（告诉外面，这个容器使用的是 8000 端口）
EXPOSE 8000

# 7. 启动命令：当容器运行时，自动执行这行
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]