"""
@Time: 2025/4/1 17:24
@Author: fengtianshi@kuaishou.com
@File: app.py
"""
from injector import Injector

from internal.server import HttpServer
from internal.router  import Router

injector = Injector()

app = HttpServer(__name__, router=injector.get(Router))

if __name__ == '__main__':
    app.run(debug=True)