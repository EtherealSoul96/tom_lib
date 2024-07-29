from math import pi, tau
# from random import random

# for i in range(10):
#     a1 = round(random() * tau, 2)
#     a2 = round(random() * tau, 2)
#     print(a1, a2, (a2-a1) % tau, (a1-a2) % tau)


class Angle():

    __slots__ = "a"

    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return Angle(self.a + float(other))

    def __radd__(self, other):
        return Angle(self.a + float(other))

    def __sub__(self, other):
        return Angle(self.a - float(other))

    def __rsub__(self, other):
        return Angle(float(other) - self.a)

    def __neg__(self):
        return Angle(-self.a)

    def __mul__(self, other):
        return self.a * float(other)

    def __rmul__(self, other):
        return self.a * float(other)

    def __truediv__(self, other):
        # return Angle(float(self) / float(other))
        return Angle(self.a / float(other))

    def __rtruediv__(self, other):
        # return Angle(float(other) / self.balanced())
        return Angle(float(other) / self.a)

    def __float__(self):
        return self.a % tau

    def __eq__(self, other):
        return self.a % tau == float(other) % tau

    def __lt__(self, other):
        return 0 < float(other - self) < pi

    def __gt__(self, other):
        return 0 < float(self - other) < pi

    def __le__(self, other):
        return 0 <= float(other - self) < pi

    def __ge__(self, other):
        return 0 <= float(self - other) < pi

    def __str__(self):
        return str(float(self))

    def between(self, a0, a1):
        a0 = float(a0)
        a1 = float(a1)

        if a0 < a1:
            return     a0 <= float(self) <= a1
        else:
            return not a1 <= float(self) <= a0

    def __abs__(self):
        float_self = float(self)
        if float_self < pi:
            return float_self

        return tau - float_self

    def balanced(self):

        return ((self.a + pi) % tau) - pi


        # float_self = float(self)
        # if float_self < pi:
        #     return float_self
        #
        # return float_self - tau



# a1 = Angle(pi/2)
# a2 = Angle(3*pi/2+0.01)
#
# print(min(Angle(1*tau/3), Angle(2*tau/3)))
