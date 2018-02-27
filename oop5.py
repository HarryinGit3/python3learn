class Student(object):
    name = 'Student'
    def __init__(self, name):
        self.name = name


# 实例属性和类属性不要是相同的，不然实例属性会覆盖类属性
s = Student('Bob')
s.score = 90