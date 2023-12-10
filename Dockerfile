# 使用官方 Python 基础镜像
FROM python:3.10

# 设置工作目录
WORKDIR /app

# 将依赖文件复制到容器中
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 将代码复制到容器中
COPY . .

# 指定要运行的命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
