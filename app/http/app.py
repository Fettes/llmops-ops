"""
@Time: 2025/4/1 17:24
@Author: fengtianshi@kuaishou.com
@File: app.py
"""
from dotenv import find_dotenv, load_dotenv
from injector import Injector

from config import Config
from internal.router import Router
from internal.server import HttpServer

# 将环境变量加载到环境中
load_dotenv(find_dotenv('.env'))

injector = Injector()
conf = Config()

app = HttpServer(__name__, conf=conf, router=injector.get(Router))

if __name__ == '__main__':
    app.run(debug=True)
