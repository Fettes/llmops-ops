"""
@Time: 2025/4/8 15:37
@Author: fengtianshi@kuaishou.com
@File: app_schema.py
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """ 基础聊天接口验证 """
    # 必填，长度最大为2000
    query = StringField(
        'query',
        validators=[
            DataRequired(message='用户提问是必填项'),
            Length(max=2000, message='用户提问长度不能超过2000')
        ]
    )
