class Person:
    """
    人类，定义了年龄、性别、姓名等属性和吃东西起名字等动作
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
    def setname(cls, name):
        cls.name = name
        print(cls.name)

    # 静态方法
    @staticmethod
    def functiion():
        print("静态方法")



help(Person)