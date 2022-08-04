class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def eat(self):
        print("%s在吃饭"%self)

    def play(self):
        print("%s在玩" % self)

    def sleep(self):
        print("%s在吃睡觉" % self)

    def watch(self):
        print("%s在看家"%self)

    def __str__(self):
        return "名字是{}，年龄{}岁的小狗".format(self.__name, self.__age)

d=Animal("汪汪",3)
d.eat()