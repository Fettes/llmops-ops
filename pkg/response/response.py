"""
@Time: 2025/4/8 17:08
@Author: fengtianshi@kuaishou.com
@File: response.py
"""
from dataclasses import field, dataclass
from typing import Any

from flask import jsonify

from .http_code import HttpCode


@dataclass
class Response:
    """ 基础HTTP接口响应格式 """
    code: HttpCode = HttpCode.SUCCESS

    message: str = ""
    data: Any = field(default_factory=dict)


def json_response(data: Response = None):
    """ 基础响应接口 """
    return jsonify(data), 200


def json_response_success(data: Any = None):
    """ 成功接口响应 """
    return json_response(Response(code=HttpCode.SUCCESS, message="", data=data))


def json_response_error(data: Any = None):
    """ 失败接口响应 """
    return json_response(Response(code=HttpCode.FAIL, message="", data=data))


def json_response_validate_error(errors: dict = None):
    """ 参数校验失败接口响应 """
    first_key = next(iter(errors))
    if first_key is not None:
        msg = errors.get(first_key)[0]
    else:
        msg = ""
    return json_response(Response(code=HttpCode.VALIDATION_ERROR, message=msg, data=errors))


def message(code: HttpCode, msg: str = ""):
    """ 基础的消息响应，固定返回消息提示，数据固定为空字典 """
    return json_response(Response(code=code, message=msg, data={}))


def message_success(msg: str = ""):
    """ 成功消息响应 """
    return message(code=HttpCode.SUCCESS, msg=msg)


def message_error(msg: str = ""):
    """ 失败消息响应 """
    return message(code=HttpCode.FAIL, msg=msg)


def message_not_found(msg: str = ""):
    """ 404消息响应 """
    return message(code=HttpCode.NOT_FOUND, msg=msg)


def message_unauthorized(msg: str = ""):
    """ 401消息响应 """
    return message(code=HttpCode.UNAUTHORIZED, msg=msg)


def message_forbidden(msg: str = ""):
    """ 403消息响应 """
    return message(code=HttpCode.FORBIDDEN, msg=msg)
