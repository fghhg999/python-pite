#字典元素的删除
scores={'张三':100,'李四': 200,'王五':300}
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