'''
@author: Yiz56865
'''


class Field(object):
    def __init__(self, name, column_type):
        self.__name = name
        self.__column_type = column_type

    def __str__(self):
        return 'class: {}, name: {}, type: {}'.format(self.__class__.__name__, self.__name, self.__column_type)

    @property
    def name(self):
        return self.__name

class StringFiled(Field):
    def __init__(self, name):
        super(StringFiled, self).__init__(name, 'varchar(100)')


class IntField(Field):
    def __init__(self, name):
        super(IntField, self).__init__(name, 'bigint')


if __name__ == "__main__":
    f = Field('abc', 'def')
    print(f)
    s = StringFiled('xxx')
    print(s)
    i = IntField('yyy')
    print(i)