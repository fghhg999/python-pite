#计算机的控制流程
##顺序结构、选择结构（if语句）、循环结构（while语句、for-in语句）
###一、顺序结构
#程序从上到下顺序地执行代码，中间没有任何判断和跳转，直接到程序结束
'''把大象症状进冰箱一共需要几步？'''
print('----程序开始----')
print('---打开冰箱门---')
print('---把大象塞进冰箱---')
print('---关上冰箱门---')

###对象的布尔值
#python一切皆对象，所有对象都有一个布尔值
#获取对象的布尔值；使用内置函数bool()
'''测试对象的布尔值'''
print(bool(False))#F
print(bool(0))#F
print(bool(0.0))#F
print(bool(None))#F
print(bool(''))#f
print(bool(""))#F
print(bool([]))#空列表
print(bool(list()))#空列表
print(bool(()))#空元组
print(bool(tuple()))#空元组
print(bool({}))#空字典
print(bool(dict()))#空字典
print(bool(set()))#空集合
print('以上对象外的布尔值均为false')

###二、选择结构
#程序根据判断条件的布尔值选择性地执行部分代码
#明确的让计算机知道在什么条件下，该去做什么
####单分支结构
'''if表达式：
条件执行体'''
money=1000
s=int(input('请输入取款金额：'))
if money>=s:
    money=money-s
    print('取款成功，余额为：',money)

####双分支结构
time=int(input('请输入一个时间：'))    
if time<=int(30):
    print('坐出租车上班')
else:
    print('走路去上班')


####多分支结构
jin=int(input('输入金额:'))
if jin<=10 and jin>=0:
    print('今天吃土')
elif jin>10 and jin<=20 :
    print('今天可以吃好点')
elif jin>20 and jin<=50:
    print('今天要当土豪')
elif jin>=100 :
    print('不吃了')
elif jin<0:
    print('I need to rob bank')

#会员   嵌套结构if
#外层判断是否是会员
answer=input('您是会员吗？y/n')
money=float(input('请输入您的购物金额：'))
if answer=='y':
    if money>=300:
        print("打七折，应付金额为：",money*0.7)
    elif money>=200:
            print("打八折，应付金额为：", money*0.8)
    elif money>=100:
        print("打9折，应付金额为：",money*0.9)
    elif money<100:
        print("打9.5折，应付金额为：",money*0.95)
else:#非会员
    if money>=300:
        print("打9折，应付金额为：",money*0.9)
    elif money>=200:
            print("打9.5折，应付金额为：", money*0.95)
    elif money>=100:
        print("不打折，应付金额为：",money)
    
#条件表达式
'''从键盘录入两个整数，比较两个整数的大小'''
num_a=int(input('请输入第一个整数：'))
num_b=int(input('请输入第二个整数：'))
#比较大小
'''if num_a>=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)
'''

print('使用条件表达式进行比较')
print(str(num_a)+'大于等于'+str(num_b)  if num_a>=num_b   else  str(num_a)+'小于'+str(num_b)     ) 

## pass语句
#语句什么作用都不作，只是一个占位符，用在语法上需要语句的地方
#什么时候使用：先打搭建好语法结构，还没有想好代码怎么写的时候
#那些语句一起使用：
'''if语句的条件执行体
   for_in语句的循环体
   定义函数时的函数体'''
answer=input('您是会员吗？y/n')
if answer=='y':
   pass
else:
    pass
