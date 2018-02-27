from functools import reduce


# map map(f,[1,2,3]) 前面是函数名字，后面是输入数据
def f(x):
    return x * x


def add(x, y):
    return x + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2nums(s):
        return digits[s]

    return reduce(fn, map(char2nums, s))


# filter
def is_odd(n):
    return n % 2 == 1


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 函数作为返回值
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


# 这个函数说明在 是使用返函数的时候 不用引用循环变量或者后续会发生变化的变量
def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


if __name__ == '__main__':
    r = map(f, [1, 2, 3, 4])
    print(list(r))
    print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    # reduce 把一个函数作用在一个序列上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，类似递归
    r2 = reduce(add, [1, 3, 5, 7, 9])
    # filter只返回true的元素
    list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break
    print(r2)
    print(char2int('12345'))
    # 这个说明返函数是怎么使用
    f = lazy_sum(1, 2, 3, 4, 5)
    print(f())
