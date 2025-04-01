"""
@Time: 2025/4/1 16:57
@Author: fengtianshi@kuaishou.com
@File: injector_test.py
"""
from injector import Injector, inject

class ServiceA:
    name: str = "ServiceA"

@inject
class ServiceB:
    def __init__(self, service_a: ServiceA):
        self.service_a = service_a

    def print(self):
        print(f"ServiceA的名字：{self.service_a.name}")

injector = Injector()
service_b = injector.get(ServiceB)
service_b.print()
