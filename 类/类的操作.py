class Student:
    def __init__(self, number):
        self.__number = number

    @property
    #将属性的方法关联到属性中
    def student_number(self):
        print('number:', self.__number)


student = Student(34)
print(Student.__dict__)
# print((student.number))
# student.student_number=12#只读属性无法赋值
student.student_number
print(Student.__base__)