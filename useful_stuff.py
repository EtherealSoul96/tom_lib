
from time import time

t0 = time()
def time_flag():
    global t0
    t1 = time()
    t2 = t1 - t0
    t0 = t1
    return t2

# def print_time_flag(text=""):
#     print(str(text), time_flag())


# works just like the print function but at the end it adds the time between the present and the last call
class print_time_flag:
    # t = time()
    groups = {None: time()}
    def __init__(self, *args, group=None):

        new_t = time()

        if group not in print_time_flag.groups:
            print(*args, 0)

        else:
            print(*args, new_t-print_time_flag.groups[group])

        print_time_flag.groups[group] = new_t




def rl(l):
    return range(len(l))

def print_list(l):
    for e in l:
        print(e)

def avg(l):
    return sum(l)/len(l)

# def float_range(start, finish, step):
#     num = start
#     while

class CircularList(list):
    def __init__(self, l):
        self.length = len(l)
        super().__init__(l)

    def __getitem__(self, item):
        return super().__getitem__(item % self.length)

    def __setitem__(self, key, value):
        super().__setitem__(key % len(self), value)

def my_sum(l):
    # tot = 0  # this is the problem
    # for value in l:
    #     tot += value
    # return tot

    # if len(l) == 0:
    #     return 0

    result = l[0]
    for e in l[1:]:
        result += e
    return result

def my_avg(l):
    return my_sum(l) / len(l)

def sign(n):
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0

def vector_list_to_normal_list(l):
    l2 = []
    for e in l:
        l2.append(e.x)
        l2.append(e.y)
    return l2

