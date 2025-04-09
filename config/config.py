"""
@Time: 2025/4/8 15:47
@Author: fengtianshi@kuaishou.com
@File: config.py
@DESC: 基于flask-script的配置: https://flask-wtf.readthedocs.io/en/1.2.x/config/
"""


class Config:
    def __init__(self):
        # 关闭wtf的csrf保护
        self.WTF_CSRF_ENABLED = False
