# 整数类型 浮点数没有太多区别
a = 1
b = 1.2e-5
print(a, '\n', b)

# 字符串 用""或者''都可以 \是转义字符  \\就是表示\
print('I\'m ok')
print('\\\n\\')
print(r'\\\n\\')  # 用r''表示所有的不使用转义字符
print('''line1
line2
line3''')  # '''多行换行
print(r'''hello,\n
world''')

# 布尔型
age = 10
if age >= 18:
    print('adult')
else:
    print('teenager')

# 变量
a = 123
print(a)
a = 'ABC'
print(a)

a = 'ABC'
b = a
a = 'XYZ'
print(b)

# 字符编码 encode和decode
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# list是一种数据类型，是列表，可以嵌套
classmates = ['yin', 'jiang', 'gao']
classmates.append('Adam')  # 添加到最后一个
classmates.insert(1, 'Jack')
classmates.pop()  # 删除最后一个
classmates.pop(1)
print(classmates[-1])

# tuple 元组 元组本身的要素不能更改
classmates = ('Michael', 'Bob', 'Tracy')
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

# cannot modify tuple:
# classmates[0] = 'Adam'


# 循环 for // while // continue // break
# 打印list:
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 打印数字 0 - 9
for x in range(10):
    print(x)

sum = 0
n = 1
while n <= 100:
    sum = sum + n
    n = n + 1
print(sum)

# dict和set
d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))

s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
