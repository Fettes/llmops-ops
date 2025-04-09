"""
@Time: 2025/4/8 17:06
@Author: fengtianshi@kuaishou.com
@File: http_code.py
"""
from enum import Enum


class HttpCode(str, Enum):
    """ HTTP基础业务状态码 """
    SUCCESS = 'success'  # 成功
    FAIL = 'fail'  # 失败
    NOT_FOUND = 'not_found'  # 未找到
    UNAUTHORIZED = 'unauthorized'  # 未授权
    FORBIDDEN = 'forbidden'  # 禁止访问
    VALIDATION_ERROR = 'validation_error'  # 参数校验失败
