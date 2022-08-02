class Person:
    age = 18

    # name = ""
    # gender = ["男性", "女性"]

    def __init__(self, name, gender):
        self.name = name
        self.cache = {}
        self.item = [1, 2, 3, 4]
        if gender == 1:
            self.gender = "男性"
        else:
            self.gender = "女性"

    # _____信息格式化操作

    def __str__(self):
        return "%s%s%s" % (self.name, self.age, self.gender)

    def __repr__(self):
        return "sad"

    # ____call方法
    def __call__(self, high, **kwargs):
        print("call 方法,第一个参数", high, kwargs)
        return 0

    """
    切片操作
    """

    def __setitem__(self, key, value):
        print("setitem", key, value)
        # if  isinstance(key, slice):
        self.item[key.start:key.stop:key.step] = value

    # else:
    # self.cache[key] = value

    def _getitem_(self, item):
        print("getitem", item)

    def __delitem__(self, key):
        print("delitem", key)
        del self.cache[key]


# zhangsan = Person("zhangsan", 0)
# # print(zhangsan.name,zhangsan.age,zhangsan.gender)
# print(zhangsan)
# print(repr(zhangsan))
# zhangsan(123,habit="playgame")

lisi = Person("lisi", 1)
# lisi(185)
# lisi["name"] = "lisi"
# del lisi["name"]


# lisi[0:3: 1] = ["a", "b", "c"]
# print(lisi.item)

"""
def createPen(p_type ,p_color):
    print("创建了一个%s这个类型的画笔，它是%s颜色"% (p_type,p_color))

# createPen("钢笔","红色")
# createPen("钢笔","绿色")
# createPen("钢笔","黄色")
import functools
gangbiFunc = functools.partial(createPen,p_type="钢笔")
gangbiFunc(p_color="红色")
qianbiFunc = functools.partial(createPen,p_color="黑色")
qianbiFunc("铅笔")

"""


# 比较方法
class A:
    def __init__(self, *args, **kwargs):
        self.number = args[0]
        self.weight = args[1]

    def __eq__(self, other):
        return self.number * self.weight == other.number * other.weight

    def __ne__(self, other):
        print("不相等")
        if self.number * self.weight >= other.number * other.weight:
            return True
        return False


"""
相等__eq__
不相等 __ne__
小于 __lt__
小于或等于__le__
大于__gt__
大于或等于__ge__
"""
import functools


@functools.total_ordering
class B:
    def __init__(self,*args, **kwargs):
        self.number = args[0]
        self.weight = args[1]

    def __eq__(self, other):
        print("eq")
        return 1#self.number * self.weight == other.number * other.weight

    def __lt__(self, other):
        print("lt")
        return 2#self.number * self.weight < other.number * other.weight


# a1 = A(5, 10)
# a2 = A(10, 5)
# a3 = A(5, 7)
# print((a1 == a2))
# print(a3 != a1)
#
# b1 = B(5,6)
# b2 = B(3,4)
# print(B.__dict__)
# print(b1<=b2)


#bool方法
class C:
    def __init__(self,*args, **kwargs):
        self.number = args[0]
        self.weight = args[1]

    def __bool__(self):
        if self.weight>10:
            return  True
        else:
            return  False



ic=C(1,12)
if ic:
    print("调用bool方法")
else:
    print("调用失败")