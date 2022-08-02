"""
class Person:
    def __init__(self, name):
        self.__age = None
        self.__name = name

    def getage(self):
        return self.__age

    sex = ["男", "女"]

    def setage(self, age):
        self.__age = age
        print("age :")

    age=property(getage, setage)

#property第一种使用方法
zhangsan=Person("zhangsan")
zhangsan.age=13
print(zhangsan.age)
print(zhangsan.__dict__)
"""

"""
class Person:
    def __init__(self, name):
        self.__age = None
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


zhangsan = Person("zhangsan")
zhangsan.age = 13
print(zhangsan.age)
"""


# _____________________经典类property能读，但不能set属性

class Person:
    def __setattr__(self, key, value):
        # print(key, value)
        if key == "age" and key in self.__dict__.keys():
            print("只读属性不能修改啊")
        else:
            self.__dict__[key] = value
            print("可以修改")


p = Person()
p.age = 18
print(p.age)
