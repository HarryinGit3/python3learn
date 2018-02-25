import myfunction
import sys
# 设置函数所在路径 然后直接使用
sys.path.append('C:\\code\\python3\\learn\\python3learn')
a = myfunction.my_abs(-11)
x1,x2 = myfunction.quadratic(1, -3, 2)
print(a)
print(x1,x2)
