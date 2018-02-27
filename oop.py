#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 面向对象
__author__ = 'Harryin'


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s:%s" % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


# 面向对象开始
if __name__ == '__main__':
    bart = Student("yin", 33)
    bart.print_score()
    print("************")
    print(bart.name, "\n", bart.score)
    print("************")
    print(bart.name, bart.get_grade())
    print("************")
    print(bart.print_score(), bart.get_grade())
    print("************")
    print(bart.get_grade())
    print("************")
    print(bart.print_score())
