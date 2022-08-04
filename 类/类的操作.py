class Student:
    def __init__(self, number):
        self.__number = number

    @property
    #将属性的方法关联到属性中
    def student_number(self):
        print('number:', self.__number)
        return self.__number

    def __getitem__(self, item):
        self.__number += 1
        if self.__number>40:
            raise StopIteration#抛出异常
        return  self.__number
    #getitem优先级更高的迭代器函数
    def __iter__(self):
        print("迭代器")
        return self

    #迭代器方法
    def __next__(self):
        self.__number += 1
        if self.__number > 40:
            raise StopIteration  # 抛出异常
        return self.__number

student = Student(34)
print(Student.__dict__)
# print((student.number))
# student.student_number=12#只读属性无法赋值
# student.student_number
# print(Student.__base__)

#遍历操作
# for s in student :
#     print(s)
print(next(student))
s=iter(student)
print( s is student)
import  collections
print(isinstance(student,collections.abc.Iterator))