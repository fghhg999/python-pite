# 字典的创建与删除

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


## key的判断

scores={'张三':100,'李四': 200,'王五':300}
print('张三' in scores)
print('张三' not in scores)

#字典元素的删除

del scores['张三']
print(scores)

#* 请空字典的元素
scores.clear()

#* 字典元素的增加
scores['王朝马汉']=500
print(scores)

#* 字典元素的修改
scores['王朝马汉']=800
print(scores)