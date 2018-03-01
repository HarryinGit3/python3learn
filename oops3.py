class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name:%s)' % self.name

    __repr__ = __str__


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    # 让class能够类似list那样进行循环
    def __iter__(self):
        return self

    # 可以让其能够像list那样取到第几个数
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                    a, b = b, a + b
            return L

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a


if __name__ == '__main__':
    print(Student('Yin'))
    for n in Fib():
        print(n)
    f = Fib()
    print(f[8])
