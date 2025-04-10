"""
@Time: 2025/4/1 17:20
@Author: fengtianshi@kuaishou.com
@File: http.py
"""
from flask import Flask

from config import Config
from internal.exception import CustomException
from internal.router import Router
from pkg.response import json_response, Response, HttpCode


class HttpServer(Flask):
    """ HTTP服务引擎 """

    def __init__(self, *args, conf: Config, router: Router, **kwargs):
        # 1. 调用父类构造函数初始化
        super().__init__(*args, **kwargs)

        # 2. 初始化注册配置
        self.config.from_object(conf)

        # 3. 注册错误处理
        self.register_error_handler(Exception, self._register_error_handler)

        # 4. 注册应用路由
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        # 1. 异常信息是不是我们自定义的异常，如果是可以获得code和message信息
        if isinstance(error, CustomException):
            return json_response(
                Response(code=error.code, message=error.message, data=error.data if error.data is not None else {}))
        # 2. 如果不是我们自定义的异常，则有可能是程序，数据库等异常，也可以抛出信息，设置未Fail代码
        if self.debug:
            raise error
        else:
            return json_response(Response(code=HttpCode.FAIL, message=str(error), data={}))
