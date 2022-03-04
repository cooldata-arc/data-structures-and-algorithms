"""
基础数据类型
"""
counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串

print (counter)
print (miles)
print (name)

# 多变量赋值 从后向前赋值
a = b = c = 1
print("a={0}; b={1}; c={2}".format(a, b, c))

d, e, f = 1, 2, "baidu"
print ("d={0}; e={1}; f={2}".format(d, e, f))


"""
标准数据类型(6种):
    Number (数字): int、float、bool、complex(复数)。
    String (字符串)
    List   (列表)
    Tuple  (元组)
    Set    (集合)
    Dictionary  (字典)

不可变数据(3 个): Number(数字)、String(字符串)、Tuple(元组);
可变数据(3 个): List(列表)、Dictionary(字典)、Set(集合)。
"""
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

'''
isinstance 和 type 的区别在于:
    type()不会认为子类是一种父类类型。
    isinstance()会认为子类是一种父类类型。
注: Python3 中,bool 是 int 的子类,True 和 False 可以和数字相加, True==1、False==0 会返回 True,但可以通过 is 来判断类型。
'''
print(isinstance(a, int)) # True
print(issubclass(bool, int)) # True


"""
数值运算(特殊的三种):
    / : 除法,得到一个浮点数
    //: 除法,得到一个整数
    **: 乘方
注: 在混合计算时,Python会把整型转换成为浮点数。
"""
a, b = 1, 2
c = a / b   # 0.5
d = a // b  # 0
e = a ** b  # 1
print("c=a/b={0}, d=a//b={1}, e=a**b={2}".format(c, d, e))

"""
String 字符串
变量[头下标:尾下标]
双向索引:
    正向: 0 - (len - 1)
    负向: -1 - (-len)
"""
str = "google"
print(str[0:3])     # 正向截取3个字符
print(str[0:-1])    # 输出第一个到倒数第二个的所有字符
print(str[2:5])    # 输出从第三个开始到第五个的字符
print(str[2:])      # 输出从第三个开始的后的所有字符
print(str * 2)      # 输出字符串两次，也可以写成 print (2 * str)


"""
List   (列表)
    列表可以完成大多数集合类的数据结构实现,列表中元素的类型可以不相同,它支持数字,字符串甚至可以包含列表(所谓嵌套)。
    列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
    和字符串一样,列表同样可以被索引和截取,列表被截取后返回一个包含所需元素的新列表。
变量[头下标:尾下标] 可双向访问截取
"""
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表


"""
Tuple(元组) : 不可变
    虽然tuple的元素不可改变, 但它可以包含可变的对象, 比如list列表。
    构造包含 0 个或 1 个元素的元组比较特,所以有一些额外的语法规则:
        tup1 = ()    # 空元组
        tup2 = (20,) # 一个元素,需要在元素后添加逗号
"""
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

"""
Set(集合):
    可以使用大括号 { } 或者 set() 函数创建集合,注意:创建一个空集合必须用 set() 而不是 { },因为 { } 是用来创建一个空字典。
"""
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 'Google'}
print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

"""
Dictionary(字典): 
    列表是有序的对象集合,字典是无序的对象集合。两者之间的区别在于:字典当中的元素是通过键来存取的,而不是通过偏移存取。
    字典是一种映射类型,字典用 { } 标识,它是一个无序的 键(key) : 值(value) 的集合。

注: 
    * 键(key)必须使用不可变类型。
    * 在同一个字典中,键(key)必须是唯一的。
"""
a = {}
a['one'] = "1 - 菜鸟教程"
a[2]     = "2 - 菜鸟工具"
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

print (a['one'])       # 输出键为 'one' 的值
print (a[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

# 从键值对构造字典
print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))
print(dict(dict(Runoob=1, Google=2, Taobao=3)))

# 字典推导式
print({x: x**2 for x in (2, 4, 6)})