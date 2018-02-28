# 使用__slots__ Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：但对其子类不影响
class Student(object):
    __slots__ = ('name', 'age')


class MStudent(Student):
    pass


if __name__ == '__main__':
    s = Student()
    s.name = 'yin'
    s.age = 23
    try:
        s.score = 99
    except AttributeError as e:
        print('AttributeError:', e)
    m = MStudent()
    m.score = 98
    print('m.score=', m.score)
