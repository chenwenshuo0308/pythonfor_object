class Person:
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

    def __ren(self):
        print("私有方法，类内部使用")


zhangsan = Person()
zhangsan.setname(zhangsan)
print(zhangsan.name,zhangsan.age)
# zhangsan.eat("蛋糕")
# print(Person.eat)
#实列方法
# Person.eat("lisi","牛子")

# # zhangsan.name = "Zhangsan"
# #类方法
# zhangsan.setname("zhangsan")
# zhangsan.eat("粑粑")
# # Person.eat()#Person.eat() missing 1 required positional argument: 'self'
# # Person.getname()
# # Person.functiion()
# #静态方法
# Person.functiion()
# zhangsan.functiion()
# print(zhangsan.age)
# print(zhangsan.__dict__)
#print(Person.__dict__)
#私有化方法
#print(Person.__ren)
#print(Person._Person__ren)