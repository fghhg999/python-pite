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