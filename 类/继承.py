class D:
    pass


class C(D):
    pass

class B(D):
    pass

class A(B,C):
    pass


import inspect
print(inspect.getmro(A))