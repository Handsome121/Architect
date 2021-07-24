# Django之ORM操作

####  Django 模型（数据库）

Django 模型是与数据库相关的，与数据库相关的代码一般写在 `models.py` 中，Django 支持 sqlite3,PostgreSQL、MySQL、SQLite、Oracle。等数据库，使用对应的数据库只需要在settings.py中配置即可，不用更改models.py中的代码，丰富的API极大的方便了使用。

MySQL 是 Web 应用中最常用的数据库,，接下来对MySQL的使用进行介绍，如果没有安装mysql 驱动，可以执行以下命令安装：

```python
pip install mysqlclient
```

#### 数据库配置

 对MySQL的配置只需要在项目文件夹下的 `settings.py` 文件中找到 DATABASES 配置项，将其信息修改为：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'user',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}
```

 上面的变量必须使用大写，它们与 MySQL 中对应数据库和用户的设置相同。Django 根据这里的设置，与 MySQL 中相应的数据库和用户连接起来。

在Django中是默认使用mysqldb模块连接数据库的，这时候要用pymysql模块来替换mysqldb连接数库，有两种方式：
方式一：在项目名文件夹下面的__ init __ .py
方式二：在app应用文件夹下面的__ init __ .py

```python
import pymysql
pymysql.install_as_MySQLdb()  # 告诉django用pymysql代替mysqldb连接数据库
```

#### 创建模型

 要想使用模型必须要创建app应用，创建好app后就可以在app文件夹下的models.py定义模型。

```python
from django.db import models
class User(models.Model):
    # user表的主键字段名就是id,id字段可以不写默认会帮你创建一个主键id字段
    id = models.AutoField(primary_key=True)
    # varchar(32) name字段是varchar(32)   CharField在定义的时候必须要加max_length参数
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.name
```

  以上的类名代表了数据库中的一张表，且继承了models.Model，类里面的属性代表数据表中的字段(name)，数据类型则有CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。 

#### 常用字段类型

以下列表描述了一些更常用的字段类型。

- **CharField**： 是用来定义短到中等长度的字段字符串。你必须指定max_length要存储的数据。
- **TextField**：用于大型任意长度的字符串。你可以max_length为该字段指定一个字段，但仅当该字段以表单显示时才会使用（不会在数据库级别强制执行）。
- **IntegerField**：是一个用于存储整数（整数）值的字段，用于在表单中验证输入的值为整数。
- **DateField** **和 DateTimeField**：用于存储／表示日期和日期／时间信息（分别是Python.datetime.date和datetime.datetime对象。这些字段可以另外表明（互斥）参数auto_now=Ture （在每次保存模型时将该字段设置为当前日期），auto_now_add（仅设置模型首次创建时的日期）和default（设置默认日期，可以被用户覆盖）。
- **EmailField**：用于存储和验证电子邮件地址。
- **FileField** 和 **ImageField**：分别用于上传文件和图像（ImageField 只需添加上传的文件是图像的附加验证）。这些参数用于定义上传文件的存储方式和位置。
- **AutoField**：是一种 IntegerField 自动递增的特殊类型。如果你没有明确指定一个主键，则此类型的主键将自动添加到模型中。
- **ForeignKey**：用于指定与另一个数据库模型的一对多关系（例如，汽车有一个制造商，但制造商可以制作许多汽车）。字段的参数有 to：设置要关联的表，to_field：设置要关联的表的字段，on_delete：当删除关联表中的数据时，当前表与其关联的行的行为。
- **ManyToManyField**： 用于指定 多对多关系（例如，一本书可以有几种类型，每种类型可以包含几本书）。
- **ForeignKeys**：可以用更复杂的方式来描述组之间的关系。具有参数on_delete来定义关联记录被删除时会发生什么（例如，值models.SET_NULL将简单地设置为值NULL）。

#### 常见字段参数

**字段参数**：
		**null**：用于表示某个字段可以为空。

**unique**：如果设置为unique=True 则该字段在此表中必须是唯一的 。

**db_index**：如果db_index=True 则代表着为此字段设置索引。

**default**：为该字段设置默认值。

除了我们前面说过的普通类型字段，Django还定义了一组关系类型字段，用来表示模型与模型之间的关系。

####  ForeignKey

 多对一的关系，通常被称为外键。外键字段类的定义如下： 

```python
class ForeignKey(to, on_delete, **options)[source]
```

外键需要两个位置参数，一个是 to 关联的模型，另一个是 on_delete 选项。实际上，在目前版本中，on_delete 选项也可以不设置，在Django2.0版本后，该选项会设置为必填。

在数据库后台，Django会为每一个外键添加 _id 后缀，并以此创建数据表里的一列。

**参数说明**：

外键还有一些重要的参数，说明如下：

**on_delete**

当一个被外键关联的对象被删除时，Django将模仿 on_delete 参数定义的SQL约束执行相应操作。该参数可选的值都内置在 django.db.models 中，包括：

- CASCADE：模拟SQL语言中的 ON DELETE CASCADE 约束，将定义有外键的模型对象同时删除！
- PROTECT：阻止上面的删除操作，但是弹出 ProtectedError 异常
- SET_NULL：将外键字段设为null，只有当字段设置了 null=True 时，方可使用该值。
- SET_DEFAULT：将外键字段设为默认值。只有当字段设置了default参数时，方可使用。
- DO_NOTHING：什么也不做。
- SET()：设置为一个传递给SET()的值或者一个回调函数的返回值。注意大小写。

**limit_choices_to**

该参数用于限制外键所能关联的对象，只能用于Django的ModelForm（Django的表单模块）和admin后台，对其它场合无限制功能。其值可以是一个字典、Q对象或者一个返回字典或Q对象的函数调用，如下例所示：

```python
staff_member = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    limit_choices_to={'is_staff': True},
)
```

这样定义，则ModelForm的 staff_member 字段列表中，只会出现那些 is_staff=True 的Users对象，这一功能对于admin后台非常有用。

**related_name**

用于关联对象反向引用模型的名称。通常情况下，这个参数可以不设置，Django会默认以模型的小写加上 _set 作为反向关联名，

如果你不想为外键设置一个反向关联名称，可以将这个参数设置为“+”或者以“+”结尾，如下所示：

```py
user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='+',
)
12345
```

**related_query_name**

反向关联查询名。用于从目标模型反向过滤模型对象的名称。

**to_field**

默认情况下，外键都是关联到被关联对象的主键上（一般为id）。如果指定这个参数，可以关联到指定的字段上，但是该字段必须具有 unique=True 属性，也就是具有唯一属性。

**db_constraint**

默认情况下，这个参数被设为True，表示遵循数据库约束，这也是大多数情况下你的选择。如果设为False，那么将无法保证数据的完整性和合法性。在下面的场景中，你可能需要将它设置为False：

- 有历史遗留的不合法数据，没办法的选择
- 你正在分割数据表

当它为False，并且你试图访问一个不存在的关系对象时，会抛出DoesNotExist 异常。

**swappable**

控制迁移框架的动作，如果当前外键指向一个可交换的模型。使用场景非常稀少，通常请将该参数保持默认的True。

####  ManyToManyField

多对多关系在数据库中也是非常常见的关系类型。比如一本书可以有好几个作者，一个作者也可以写好几本书。多对多的字段可以定义在任何的一方，请尽量定义在符合人们思维习惯的一方，但不要同时都定义。

```py
class ManyToManyField(to, **options)[source]
1
```

**参数说明**：

除了上面的外键的参数外还有一下参数。

**through**（定义中间表）

如果你自定义多对多关系的那张额外的关联表，可以使用这个参数！参数的值为一个中间模型。

**through_fields**

through_fields 参数接收一个二元元组(‘field1’, ‘field2’)，field1是指向定义有多对多关系的模型的外键字段的名称，另外一个则是指向目标模型的外键字段的名称，通俗的说，就是 through_fields 参数指定从中间表模型Membership中选择哪两个字段，作为关系连接字段。

**db_table**

设置中间表的名称。不指定的话，则使用默认值。

#### OneToOneField

一对一关系类型的定义如下：

```py
class OneToOneField(to, on_delete, parent_link=False, **options)[source]
1
```

从概念上讲，一对一关系非常类似具有 unique=True 属性的外键关系，但是反向关联对象只有一个。该关系的第一位置参数为关联的模型，其用法和前面的多对一外键一样。如果你没有给一对一关系设置 related_name 参数，Django将使用当前模型的小写名作为默认值。

OneToOneField 一对一关系拥有和多对一外键关系一样的额外可选参数，只是多了一个parent_link参数。

####  自定义字段

```python
class MyCharField(models.Field):
    def __init__(self,max_length,*args,**kwargs):
        self.max_length = max_length
        super().__init__(max_length=max_length,*args,**kwargs)
    def db_type(self, connection):
        return 'char(%s)'%self.max_length
```

#### 字段的枚举

```python
class User(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    info = MyCharField(max_length=32,null=True)  # 使用自定义字段
    choices = ((1,'男'),(2,'女'),(3,'其他'))
    gender = models.IntegerField(choices=choices,default=2)

```

枚举字段的操作：

```python
创建：
models.User.objects.create(...gender=1)
查询：
res = models.User.objects.filter(id=1).first()
print(res.gender)
print(res.get_gender_display())  # 获取编号对应的中文注释
```

####  创建数据表

接下来建创建的模型同步到数据库中形成表结构。先 cd进入 `manage.py` 所在的那个文件夹下，输入下面的命令：

```python
python manage.py makemigrations  # 让 Django 知道我们在我们的模型有一些变更
python manage.py migrate  # 创建表结构,将你的数据模型变动正在同步到数据库中
```

在操作上面的命令前要确保app应用已经在settings中注册。

#### 数据库操作

#### 添加数据

在app应用文件夹下的views.py中添加增加数据的函数来操作数据库。添加数据有以下几种方式：

```python
方式一：通过create函数进行直接添加
user_obj = models.User.objects.create(name='linwow',password='123')
方式二：通过对象调用save()来添加
user_obj = models.User(name='linwow',password='123')
user_obj.save()
方式三：
user_obj = models.User()
user_obj.name = 'linwow'
user_obj.pawword = '123'
user_obj.save()
方式四：首先尝试获取，不存在就创建，可以防止重复
models.User.objects.get_or_create(name='linwow',password='123')
# 返回的是一个元组，(object, True/False)，创建时返回 True, 已经存在时返回 False
```

- 当有一对多，多对一，或者多对多的关系的时候，先把相关的对象查询出来

  ```python
  user_obj = models.User.objects.get(pk=1)
  class_obj = models.Class.objects.get(name="python")
  user_obj.cla_id = class_obj
  user_obj.save()
  ```

#### 拓展：批量插入数据

```python
l = []
for i in range(10000):
    l.append(models.Book2(name='第%s本书'%i))
models.Book2.objects.bulk_create(l)  # 批量插入数据
```

#### 获取数据

Django提供了多种方式来获取数据库的内容，从数据库中查询出来的结果一般是一个集合，这个集合叫做 QuerySet。查询数据需要注意的是你获取到的到底是一个queryset还是一个数据对象

- all()：通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM user

```python
user_list = models.User.objects.all()  # 获取user表所有的数据
这样获取到的是QuerySet对象，只要是QuerySet就可以点query查看获取到当前QuerySet对象的内部sql语句
print(user_list.query) 
```

- filter()：filter相当于SQL中的WHERE，可设置条件过滤结果，filter当条件不存在的情况下会返回一个空的queryset对象

```python
user_list = models.User.objects.filter(id=1) # 获取user表中id为1的数据
queryset对象支持索引取值 但是不推荐你使用  推荐使用自带的.first()获取第一条数据
user_query = models.User.objects.filter(name=linwow).first()
```

- get() ：获取单个对象，用get可以直接获取到数据对象本身但是查询条件不存在的情况下直接报错

```python
user_list = models.User.objects.get(id=1) # 如果数据不存在会报错，一般不推荐使用
```

获取数据方法总结：

```python
获取所有数据：
models.User.objects.all()
切片操作，获取10个人，不支持负索引，切片可以节约内存：
models.User.objects.all()[:10] 
获取对应条件的值，get是用来获取一个对象的：
models.User.objects.get(name=name)
获取满足条件的一些人，就要用到filter：
models.User.objects.filter(name="abc")  # 等于models.User.objects.filter(name__exact="abc") 名称严格等于 "abc" 的人
名称为 abc 但是不区分大小写，可以找到 ABC, Abc, aBC，这些都符合条件
models.User.objects.filter(name__iexact="abc")
名称中包含 "abc"的人：
models.User.objects.filter(name__contains="abc")
名称中包含 "abc"，且abc不区分大小写：
models.User.objects.filter(name__icontains="abc")

正则表达式查询：
models.User.objects.filter(name__regex="^abc")
正则表达式不区分大小写：
models.User.objects.filter(name__iregex="^abc")

排除包含wow的User对象：
models.User.objects.exclude(name__contains="wow")
找出名称含有abc, 但是排除年龄是23岁的
models.User.objects.filter(name__contains="abc").exclude(age=23)

1、如果只是检查User中是否有对象，应该用 user_list = models.User.objects.all().exists()
2、用 len(user_list) 可以得到User的数量，但是推荐用 models.User.objects.count()来查询数量。
3、list(user_list) 可以强行将 QuerySet 变成列表。
4、 去重方法user_list = user_list.distinct()
```

**defer 排除不需要的字段**

在复杂的情况下，表中可能有些字段内容非常多，取出来转化成 Python 对象会占用大量的资源，这时候可以用 defer 来排除这些字段。

```python
models.User.objects.all().defer('addr')
```

**only 仅选择需要的字段**

和 defer 相反，only 用于取出需要的字段，假如只需要查出用户名。

```python
models.User.objects.all().only('addr')
```

#### 更新数据

修改数据可以使用 save() 或 update()，save()的使用方法和新增数据是一样的，下面介绍update的使用方法。

- 批量更新，适用于 .all() .filter() .exclude() 等后面 。
- 单个 object 更新，适合于 .get(), get_or_create(), update_or_create() 等得到的 obj。

```python
基于queryset
models.User.objects.filter(id=1).update(name='lin',password='321')
```

####  删除数据

删除数据库中的对象只需调用该对象的delete()方法即可

- 删除id=1的数据

```python
基于对象
user_obj = models.User.objects.get(id=1)
test1.delete()
基于queryset
models.User.objects.filter(id=1).delete()
```

- 删除所有数据

```python
models.User.objects.all().delete()
```

#### 数据排序

在 Django 应用中，如果希望根据某字段的值对检索结果排序，比如说，按字母顺序。 那么，使用order_by() 这个方法就可以了。

- 可以对任意字段进行排序：

```python
models.User.objects.all().order_by('name')
```

- 如果需要以多个字段为标准进行排序（第二个字段会在第一个字段的值相同的情况下被使用到），使用多个参数就可以:

```python
models.User.objects.all().order_by('name','id')
```

- 可以指定逆向排序，在前面加一个减号 - 前缀：

```python
models.User.objects.all().order_by('-name')
```

