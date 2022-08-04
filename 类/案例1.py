# 计算器实现加减乘除打印结果
class Animal:
    # 属性和方法
    # 设置不同权限的属性和方法,继承当中,进行#在子类当中,能否访问到这些资源
    a = 1
    _b = 2
    __c = 3

    def t1(self):
        print("t1")

    def _t2(self):
        print("t2")

    def __t3(self):
        print("t3")

    def __init__(self):
        print("init,Animal")


class Person(Animal):
    def test(self):
        print("继承的a",self.a)
        print("b",self._b)
       # print(self.__c)

        self.t1()
        self._t2()
        # self.__t3()


p = Person()
p.a=11
print(Person.__base__)
print(type.__base__)
print(p.test())
print(Person.a)

print(p.__dict__)
