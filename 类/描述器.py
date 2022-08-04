import sys


class Person:
    """

    """

    def __init__(self, name):
        self.__age = None
        self.__name = name

    @property
    def age(self):
        """
        描述器得到属性
        :return:
        """
        return self.__age

    @age.setter
    def setage(self, value):
        """
        描述器设置属性
        :return:
        """
        self.__age = value

    @age.deleter
    def delt(self):
        """

        描述器删除属性
        :return:
        """
        del self.__age


# wang = Person("Wang")
# help(Person)
# print((wang.__dict__))


# 使用类实现属性
# 资料描述器实现get set 方法
# 非资料描述器 实现Get方法
# 资料描述器》实例属性（方法）》非资料描述器
class Age:
    def __get__(self, instance, owner):
        print("get")

    def __set__(self, instance, value):
        print("set")

    def __delete__(self, instance):
        print("delete")


class Student:
    age = Age()  # 只有一个age实例，多个person实例共享


# print(Student.age)
# lyh=Student()
# lyh.age=18
# #需要通过实例化才能生效
# print(lyh.age)

class check():
    def __init__(self, func):
        self.f = func

    def __call__(self, *args, **kwargs):
        self.f()
        print("验证")


@check
def fashuoshuo():
    print("发说说fss")


# fashuoshuo = check(fashuoshuo)

#fashuoshuo()
#--几个监听对象生命周期的方法--
#
class Human :
    #def __new__(cls, *args,**kwargs):
       # print("新建了一个对象,但是，被我拦截了")
    def __init__(self):

        print("初始化方法")
        self.name = "sz"

    def __del__(self):

        print("这个对象被释放了")
        pass

p= Human()#del p
# # print(p)
# print(p.name)
#
# print(sys.getrefcount(Human))
# del(p)
print(sys.getrefcount(Human))
import  gc
gc.collect()
print(gc.ref)
print(sys.getrefcount(Human))

print(gc.isenabled())
print(gc.get_threshold())