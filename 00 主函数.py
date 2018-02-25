import myfunction
import sys
if __name__ =='__main__':
    # 设置函数所在路径 然后直接使用 主函数都在myfunciton中
    sys.path.append('C:\\code\\python3\\learn\\python3learn')
    a = myfunction.my_abs(-11)
    x1,x2 = myfunction.quadratic(1, -3, 2)
    print(a)
    print(x1,x2)
    nums = [1,3,5]
    print(myfunction.calc(*nums))
    print(myfunction.foo(1,2,3,4,5,name='harryin'))