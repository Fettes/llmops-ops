"""
@Time: 2025/4/1 17:20
@Author: fengtianshi@kuaishou.com
@File: http.py
"""
from flask import Flask
from internal.router import Router

class HttpServer(Flask):
    """ HTTP服务引擎 """
    def __init__(self, *args, router: Router, **kwargs):
        super().__init__(*args, **kwargs)

        # 注册应用路由
        router.register_router(self)
