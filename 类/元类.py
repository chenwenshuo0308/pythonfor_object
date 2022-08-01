# number = 10
# str1 = "zhanfa"
# print(number.__class__)
# print(str1.__class__)
# print(int.__class__)
# # type就是元类
#
# # 创建一个类（新方法）
# xiaohe = type("pet", (), {"count": 0, "age": 1})
# print(xiaohe.__dict__)
#

class Biology:
    pass


class Animal:
    __metaclass__ = Biology

    pass


class Person(Animal):
    age = 18
    name = ""
    gender = ["男性", "女性"]

    # 实列方法
    def eat(self, food):
        print(self.name + "吃%s" % food)

    # 类方法
    @classmethod
    def setname(cls, name):
        cls.name = name
        print(cls.name)

    # 静态方法
    @staticmethod
    def functiion():
        print("静态方法")

import   类的属性
#from  类的属性 import  Biology
#print(Person.__class__)
# print(Biology.DNA)
# print(Biology._fenlei)
# print(Biology.__sort)
print(类的属性.__a)