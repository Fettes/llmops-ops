"""
@Time: 2025/4/1 17:10
@Author: fengtianshi@kuaishou.com
@File: app_handler.py
"""
import os

from flask import request
from openai import OpenAI

from internal.exception import FailException
from internal.schema import CompletionReq
from pkg.response import json_response_success, json_response_validate_error


class AppHandler:
    """ 应用控制器 """

    def completion(self):
        """ 聊天接口 """
        # 1. 提取从接口中获取的输入
        req = CompletionReq()
        if not req.validate():
            return json_response_validate_error(req.errors)
        query = request.json.get("query")

        # 2. 构建DeepSeek客户端，并发起请求
        client = OpenAI(
            api_key=os.getenv("API_KEY_FREE"),
            base_url=os.getenv("API_URL_FREE"),
        )

        # 3. 得到请求响应，然后将Deepseek的响应传递给前端
        response = client.chat.completions.create(
            model="deepseek-v3",
            messages=[
                {"role": "system", "content": "你是一个DeepSeek开发的聊天机器人，请根据用户的输入回复对应的信息"},
                {"role": "user", "content": query},
            ],
            stream=False
        )
        content = response.choices[0].message.content

        return json_response_success(content)

    def ping(self):
        raise FailException("ping接口已下线")
        # return {"ping": "pong"}
