# 私有属性
class Biology:
    # 公有属性
    DNA = 24
    # 私有属性
    _fenlei = ["animal", "Botany"]
    __sort = ["animal", "Botany"]

    def test(self):
        print(Biology.DNA)
        print(self.DNA)


class Animal(Biology):
    # __metaclass__ = Biology
    RNA = 12  # 公有属性
    _race = "animal"

    def test2(self):
        print("保护属性", Biology._fenlei)
        print("私有属性", Biology.__sort)
        print(self._race)


class Person():
    __worthy = ""
    __age = 0
    _race = ""

    def __int__(self):
        self.x = 100

    def setage(self, num):
        self.__age = num

    def getage(self):
        return self.__age

    # age = 10  # 公有属性


#
# b=Biology()
# b.test()
# print(Biology.DNA)
# a = Animal()
# a.test2()
# print(Biology._Biology__sort)#私有化通过名字重整实现

zhangsan = Person()
lisi=Person()
zhangsan.setage(18)

print(zhangsan.getage())
#print(lisi.x)

