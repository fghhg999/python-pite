# 字典

#* 什么是字典
#使用{ }定义 成对存储 键值对 键必须是不可变序列
#语法句式：





scores={'张三':100,'李四': 200,'王五':300}


#python内置的数据结构之一，与列表一样是一个可变序列
#以键值对的方式存储数据，字典是一个无序的序列
#在往字典中存储数据的时候要经过hash（）函数的工序，把键放入其中进行计算，所以字典的顺序是根据hash（）函数计算得来，因此键必须是不可变序列

#*字典的实现原理
#* 字典的实现原理与查字典类似，查字典是先根据部首或拼音查找相应的页码，python中的字典是根据key查找value所在的位置

# 字典的创建

#* 最常用的方式：使用花括号


scores={'张三':100,'李四': 200,'王五':300}
print(scores)
print(type(scores))


#* 使用内置函数dict()


dict(name='jack',age=20)

student=dict(name='jack',age=22)
print(student)


#* 空字典
d={}
print(d)


## 字典元素的获取

#* 使用[ ]     举例：scores['张三']
#* get()方法   举例：scores('张三')

#取值与使用get（）取值的区别
#如果字典中不存在指定的key，抛出keyError异常
#get（）方法取值，如果字典中不存在指定的key，并不会抛出keyError异常而是返回None，可以通过参数设置默认的value，以便指定的key不存在时返回


scores={'张三':100,'李四': 200,'王五':300}
'''第一种方法'''
print(scores['张三'])
#print(scores['王二麻子']) #'''keyError'''


'''第二种方法，使用get（）方法'''
print(scores.get('张三'))
print(scores.get('王朝马汉'))#None
print(scores.get('王二麻子',400))#400是在查找‘王二麻子’所对的value不存在时，提供的一个默认值
