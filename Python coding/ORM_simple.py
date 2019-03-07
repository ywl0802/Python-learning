class Field(object):

    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name)
#定义Field类，用于保存数据库表的字段名和字段类型

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self,name):
        super(IntegerField, self).__init__(name, 'bigint')
#在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等
#super()函数使用method resolution order(MRO)方法进行排序,以IntegerField类中出现super函数为例，所得MRO为(IntegerField,StringField,Field)；
#       然后从MRO序列中self所属类开始向右依次寻找__init__函数；
#       一旦找到，就将__init__函数绑定到self对象

class ModelMetaclass(type):     #元类继承的就是type类

    def __new__(cls, name, bases, attrs):    #注意__new__函数的作用对象是类(class)而非实例(self)，规定的是创建实例时的属性而非__init__那样先创建实例再添加属性
        if name=='model':
            return type.__new__(cls, name, bases, attrs)    #返回type.__new__（通过new函数控制的使用type函数实现的类动态创建过程）
        print('Found model: %s' % name)
        mappings = dict()   #创建列
        for k,v in attrs.items():   #类属性dict作为一个list被遍历
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k,v)) #当属性中有Field类的时候 打印对应提示
                mappings[k] = v      #将属性值放入列dic中
        for k in mappings.keys():
            attrs.pop(k)    #删除列中原有的元素
        attrs['__mappings__'] = mappings #保存属性和列的映射关系
        attrs['__table__'] = name #假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict,metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'model' object has no attribute '%s'" % key)
     
    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL:%s' % sql)
        print('ARGS: %s' % str(args))

# testing code:

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()