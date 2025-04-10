"""
@Time: 2025/4/10 14:17
@Author: fengtianshi@kuaishou.com
@File: conftest.py.py
"""
import os

import pytest

from app.http.app import app


@pytest.fixture
def client():
    """ 获取Flask应用的测试应用，并返回 """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
