
from math import sqrt, sin, cos, asin, acos, tau
from tom_lib.angle import Angle
import numpy as np

class Vec():

    __slots__ = "x", "y", "z", "d", "i"

    def __init__(self, x, y, z="2D"):

        if z == "2D":
            self.d = 2
            z = 0
        else:
            self.d = 3

        self.x = x
        self.y = y
        self.z = z

        # self.some_list = [0,1,2,3,4,5]

    def __iter__(self):
        yield self.x
        yield self.y
        if self.d == 3:
            yield self.z


    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        elif key == 2:
            self.z = value

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if type(other) == Vec:
            return Vec(self.y * other.z - self.z * other.y,
                       self.z * other.x - self.x * other.z,
                       self.x * other.y - self.y * other.x)
        else:
            return Vec(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        try:
            return Vec(self.x / other, self.y / other, self.z / other)
        except ZeroDivisionError as err:
            print("MOD ZEROOOOOOOO!!!!")
            print(err)

    def __neg__(self):
        return -1 * self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y and self.z != other.z

    def normalize(self):
        mod = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (0.5)

        try:
            # print(self, mod, "hi")

            self.x /= mod
            self.y /= mod
            self.z /= mod

            return self
        except ZeroDivisionError as err:
            print("MOD ZEROOOOOOOO!!!!")
            raise err

    def normalized(self):
        return Vec(*self).normalize()

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def angle(self):

        if abs(self) == 0:
            return Angle(0)

        v = self/abs(self)

        if asin(v.y) >= 0:
            # return acos(v.x)
            return Angle(acos(v.x))
        else:
            # return tau-acos(v.x)
            return Angle(-acos(v.x))

    def rotated(self, angle):
        return Vec(cos(angle)*self.x - sin(angle)*self.y,
                   sin(angle)*self.x + cos(angle)*self.y)

    def rotate(self, angle):
        old_x = self.x
        self.x = cos(angle) * self.x - sin(angle) * self.y
        self.y = sin(angle) * old_x  + cos(angle) * self.y

    def rotated_90(self):
        return Vec(-self.y, self.x)
    def rotated_270(self):
        return Vec(self.y, -self.x)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1 / 2)

    def __str__(self):
        # return str((round(self.x,2), round(self.y, 2), round(self.z)))
        return str((self.x, self.y, self.z))

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __bool__(self):
        return bool(self.x) or bool(self.y) or bool(self.z)

    @staticmethod
    def versor(a):
        return Vec(cos(a), sin(a))

    def proyect(self, v):
        return v * self.dot(v)/abs(v)**2

    def reflect(self, v):
        return


class Vec2():

    __slots__ = "x", "y"

    def __init__(self, x=0, y=0):

        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y


    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        raise IndexError("vector index out of range")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        raise IndexError("vector index out of range")

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        try:
            return Vec2(self.x / other, self.y / other)
        except ZeroDivisionError as err:
            print("MOD ZEROOOOOOOO!!!!")
            print(err)

    def __floordiv__(self, other):
        try:
            return Vec2(self.x // other, self.y // other)
        except ZeroDivisionError as err:
            print("MOD ZEROOOOOOOO!!!!")
            print(err)

    # def __iadd__    (self, other):
    #     self.x += other.x
    #     self.y += other.y
    #     return self
    #
    # def __isub__    (self, other):
    #     self.x -= other.x
    #     self.y -= other.y
    #     return self
    #
    # def __imul__    (self, other):
    #     self.x *= other
    #     self.y *= other
    #     return self
    #
    # def __itruediv__(self, other):
    #     self.x /= other
    #     self.y /= other
    #     return self


    def __neg__(self):
        return -1 * self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def normalize(self):

        mod = (self.x ** 2 + self.y ** 2) ** (0.5)

        try:
            # print(self, mod, "hi")

            self.x /= mod
            self.y /= mod

            return self
        except ZeroDivisionError as err:
            print("MOD ZEROOOOOOOO!!!!")
            raise err

    def normalized(self):
        return Vec2(*self).normalize()

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def angle_old(self):

        # if abs(self) == 0:
        if self.abs_2() == 0:
            return Angle(0)

        v = self/abs(self)

        if asin(v.y) >= 0:
            # return acos(v.x)
            return Angle(acos(v.x))
        else:
            # return tau-acos(v.x)
            return Angle(-acos(v.x))

    def angle(self):

        try:

            v = self/abs(self)

            if asin(v.y) >= 0:
                # return acos(v.x)
                return Angle(acos(v.x))
            else:
                # return tau-acos(v.x)
                return Angle(-acos(v.x))
        except Exception:
            return Angle(0)

    def rotated(self, angle):
        c = cos(angle)
        s = sin(angle)
        return Vec2(c * self.x - s * self.y,
                    s * self.x + c * self.y)

    def rotate(self, angle):
        old_x = self.x
        self.x = cos(angle) * old_x - sin(angle) * self.y
        self.y = sin(angle) * old_x + cos(angle) * self.y

    def rotated_90(self):
        return Vec2(-self.y, self.x)

    def rotated_270(self):
        return Vec2(self.y, -self.x)

    def round(self):
        return Vec2(round(self.x), round(self.y))

    def __abs__(self):
        return sqrt(self.x * self.x + self.y * self.y)
        # return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def abs_2(self):
        return self.x * self.x + self.y * self.y
        # return self.x ** 2 + self.y ** 2

    def __str__(self):
        # return str((round(self.x,2), round(self.y, 2), round(self.z)))
        return str((self.x, self.y))

    def __repr__(self):
        return str((self.x, self.y))

    def __hash__(self):
        return hash((self.x, self.y))

    def __bool__(self):
        return bool(self.x) or bool(self.y)

    @staticmethod
    def versor(a):
        return Vec2(cos(a), sin(a))

    def project(self, v):
        return v * self.dot(v)/abs(v)**2

def vector_list_to_normal_list(l):
    return [val for vec in l for val in vec]

class Vec2Array:
    def __init__(self, points=None, dtype=None, arr=None):
        if arr is not None:
            self.arr = arr
        else:
            if points is not None:
                self.arr = np.array([[point.x, point.y] for point in points], dtype=dtype)
            else:
                self.arr = np.zeros((0, 2))

        # self.arr = np.array([
        #     [point.x for point in points],
        #     [point.y for point in points]
        # ])

    def __len__(self):
        return self.arr.shape[0]

    @property
    def x(self):
        return self.arr[:, 0]

    @property
    def y(self):
        return self.arr[:, 1]

    def __add__(self, other):
        if type(other) == Vec2:
            return Vec2Array(arr=self.arr + np.array([other.x, other.y]))
        if type(other) == Vec2Array:
            return Vec2Array(arr=self.arr + other.arr)

    def __mul__(self, other):
        return Vec2Array(arr=self.arr * other)

    def dot(self, other):
        return Vec2Array(arr=self.arr * other.arr)

    def abs2(self):
        return self.x * self.x + self.y * self.y

    def __abs__(self):
        return np.sqrt(self.abs2())

    # maybe use a different function for Vec2 and Vec2Array?
    def append(self, other):
        if type(other) == Vec2:
            # concatenate vs append vs insert
            # self.arr = np.append(self.arr, [*other]).reshape(-1, 2)

            self.arr = np.concatenate((self.arr, [[*other]]), axis=0)
            # np.insert

        else:
            # self.arr = np.append(self.arr, other.arr).reshape(-1, 2)
            self.arr = np.concatenate((self.arr, other.arr), axis=0)

    def __str__(self):
        return str(self.arr)


# listen to Mirela's am of the dream

if __name__ == "__main__":


    a = Vec2Array([
        Vec2(1, 10),
        Vec2(2, 20),
        Vec2(3, 30),
    ])
    b = Vec2Array([
        Vec2(4, 1),
        Vec2(5, 2),
        Vec2(6, 3),
    ])
    c = Vec2Array([Vec2(100, 100)])
    d = Vec2(200, 200)
    e = 5
    f = 5.1

    print(a)
    print(b)
    print(c)
    print()

    a.append(b)
    a.append(d)
    print(a)

    # print(a.x)
    # print(a.y)

    # print(a+b)
    # print(a+c)
    # print(a+d)
    # print(a*e)
    # print(a*f)

    # angular_array = Vec2Array([
    #     Vec2(cos(1), sin(1)),
    #     Vec2(cos(2), sin(2)),
    #     Vec2(cos(3), sin(3)),
    # ]) * 10
    # print(angular_array)
    # print(abs(angular_array))
    # print(angular_array.abs2())
    #
    #
    print()
    a = np.array([0, 1, 2])
    b = np.array([6, 7])
    c = 5

    a = np.concatenate((a, b))
    print(a)

    # print(np.append(a, b))


    from tom_lib.useful_stuff import print_time_flag

    b = Vec2(1.1, 2.2)
    a = Vec2Array()
    print_time_flag("start")
    a.append(b)
    a.append(b)
    a.append(b)
    # a.append(a)
    print(a, len(a))
    for i in range(20):
    # for i in range(10_000):
        # a.append(b)
        a.append(a)
    # print(a)
    print(len(a))
    print_time_flag("1")
    a = a * 3
    print_time_flag("2")
    a = a + b
    # why is sum slower than mult?
    print_time_flag("3")


