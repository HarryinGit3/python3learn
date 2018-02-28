class Student(object):
    def get_score(self):
        return self.__score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0--100')
        self.__score = value


class Student2(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


if __name__ == '__main__':
    s = Student()
    s.set_score(63)
    print(s.get_score())

    s = Student2()
    s.score = 60
    print('s.score =', s.score)
    # ValueError: score must between 0 ~ 100!
    s.score = 9999
