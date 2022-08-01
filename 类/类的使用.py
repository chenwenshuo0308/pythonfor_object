# 经典类
class Money:
    # def __int__(self):
    __slots__ = ["kind","num"]
    value=100
    pass


class Person:
    sex = ["男", "女"]
    # pass


# 创建对象
# print(Money)
qian = Money()
yuan = Money()
zhangsan = Person()
# print(type(qian))
# print(qian.__class__)
# #对象属性
# 增
# qian.value = 100
# qian.nums = 10
# #qian.kind = ["人民币", "日元", "美元"]
# yuan.kind = ["人民币", "日元", "美元"]
# # print(qian.value)
# # print(qian.__dict__)
# # 查
# print(qian.nums)
# print(qian.color)#'Money' object has no attribute 'color'
# 改
# qian.nums = 20
# print(qian.nums)
# print(qian.kind, id(qian.kind))
# qian.kind.append("英镑")
# print(qian.kind, id(qian.kind))
# # 删#
# print(qian.__dict__)
# del qian.kind
# print(qian.kind, id(qian.kind))
# 类属性
# 增
Money.kind = ["人民币", "日元", "美元"]
Money.value=100
# 查
# print(Money.__dict__)
# print(Money.kind)
# qian.__class__ = Person
# print(qian.kind, id(qian.kind))
# print(qian.sex, id(qian.sex))
# 改
# Money.value = 100
#Money.__dict__["value"]=50
qian.value+=6
#
print(Money.value)
print(qian.value,qian.__dict__)
# # 删#
# del Money.value
# print(qian.value)
