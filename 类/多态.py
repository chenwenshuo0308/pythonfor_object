import abc


class Animal:
    name = ""

    @abc.abstractmethod
    def jiao(self):
        print("jiao%s" % self.name)


class Dog(Animal):
    name = "dog"

    def jiao(self):
        print("wangwangwang:%s" % self.name)


class Cat(Animal):
    name = "cat"

    # def jiao(self):
    # print("miaomiaomiao:%s" % self.name)


def test(obj):
    obj.jiao()


# c = Cat()
# d = Dog()
# c.jiao()
# test(c)
# test(d)


# 抽象类
# 奖ANimal设置为抽象类

a=Animal()
test(a)
