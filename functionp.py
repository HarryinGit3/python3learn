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


if __name__ == '__main__':
    r = map(f, [1, 2, 3, 4])
    print(list(r))
    print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    # reduce 把一个函数作用在一个序列上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，类似递归
    r2 = reduce(add, [1, 3, 5, 7, 9])
    print(r2)
    print(char2int('12345'))
