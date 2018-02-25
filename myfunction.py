import math

# 内置函数 https://docs.python.org/3/library/functions.html
# 定义函数 isinstance是用来检查参数类型的
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

if __name__ =='__main__':
    x, y = move(100, 100, 60, math.pi / 6 )
    print(x,y)

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1, x2

def calc(*nums):
    sum = 0
    for n in nums:
        sum = sum + n*n
    return sum

def foo(x,y,z,*args,**kw):
    print(x)
    print(y)
    print(z)
    print(args)
    print(kw)