'''
@author: Yiz56865
'''
from com.orm.Field import Field, IntField, StringFiled


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)
        else:
            mapping = dict()
            for k, v in attrs.items():
                if isinstance(v, Field):
                    mapping[k] = v
            for k, v in mapping.items():
                attrs.pop(k)
            attrs['__mapping__'] = mapping
            attrs['__table__'] = name
            return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def save(self):
        mapping = self.__mapping__
        fields = []
        values = []
        for k, v in mapping.items():
            fields.append(v.name)
            values.append(self.get(k))
        print('fields:', fields)
        print('values:', values)
        sql = 'insert into {} ({}) values ({})'.format(self.__table__, ','.join(fields), ','.join('?'))
        print('sql:', sql)
        print('value:', values)


class User(Model):
    id = IntField('id')
    name = StringFiled('name')
    email = StringFiled('email')


if __name__ == "__main__":
    u = User(id=123, name="abc", email="xx@yy")
    u.save()