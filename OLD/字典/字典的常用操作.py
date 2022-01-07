# 常用操作

## 获取字典视图
#*key（）——获取字典中所有key
#* value（）——获取字典中所有value
#* items（）——获取字典中所有key，value对


scores={'张三':100,'李四': 200,'王五':300}


'''获取字典中所有key'''

keys=scores.key()
print(keys)
print(type(keys))
print(list(keys))#将所有的key组成的视图转成列表


'''获取字典中所有value'''

values=scores.values()
print(values)
print(type(values))
print(list(values))


'''获取字典中所有key，value对'''

items=scores.items()
print(items)
print(list(items))#转换之后的列表元素是由元组组成


## 字典元素的遍历

#* 语法句式

for item in scores:
    print(item)