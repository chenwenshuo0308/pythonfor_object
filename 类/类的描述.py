class Person:
    """
    人类，定义了年龄、性别、姓名等属性
    定义吃东西起名字等动作

    """
    age = 18
    name = ""
    gender = ["男性", "女性"]

    # 实列方法
    def eat(self, food):
        """
        吃东西方法
        :param food:字符串表示吃的东西
        :return:无返回值
        """
        print(self.name + "吃%s" % food)

    # 类方法
    @classmethod
    @property
    def setname(cls, name):
        """

        :param name: 设置名字
        :return:
        """
        cls.name = name
        print(cls.name)

    # 静态方法
    @staticmethod
    def functiion():
        print("静态方法")



#help(Person)
"""
__dict_:类的属性
__bases_:类的所有父类构成元组_doc_:类的文档字符串
__name_:类名
__module_:类定义所在的模块_dict :实例的属性
__class_:实例对应的类

"""

print(Person.__dict__)
print(Person.__base__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__module__)
print(Person.__class__)

"""
__dict_:实例的属性
__class_:实例对应的类
"""
p=Person()
print(p.__class__)