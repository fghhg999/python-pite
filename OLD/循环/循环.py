## 一、range()函数
#用于生成一个整数序列
### 创建range对象的三种方式
#range(sop)     创建一个（0，stop）之间的整数序列，步长为1
#range(start，stop)     创建一个（start，stop）之间的整数序列，步长为1
#range(start,stop,step)     创建一个(start,stop)之间的整数序列，步长为step
### 返回值是一个迭代器对象
### range类型的优点
#不管range对象表示的整数序列有多长，所以range对象占用的内存空间都是相同的
#因为仅仅需要存储start，stop和step，只有当用到range对象时，才会去计算序列中的相关元素
#in与not in 判断整数数列中是否存在（不存在）指定的整数
#1.
r=range(10)
print(r)#range(0,10)
print(list(r))#[0,1,2,3,,,,10]
#2.
r=range(5,8)
print(list(r))
#3.
r=range(1,10,3)
print(list(r))
print(10 in r)#F
print(2 not in r)#T

## 二、循环结构
#反复做同一件事情，成为循环

a=1
while a<10:
    print(a)
    a+=1

### 循环的分类
#while
#for_in

### 语法结构

### 选择结构的if与循环结构while的区别
#if是判断一次，条件为true执行一次
#while是判断N+1次，条件为true执行N次

### while循环的执行流程
#### 四部循环法
#初始化变量    条件判断    条件执行体    改变变量
#总结：初始化的变量与条件判断的变量与改变的变量为同一个
#while循环的执行流程
#计算0到4之间的累加和
sum=0
a=0
while a<5:
    sum+=a
    a+=1
print('和为：',sum)
#练习:计算1到100之间的偶数和
'''初始化变量'''
sum=0
a=1
'''条件判断'''
while a<=100:
    '''条件执行体（求和）'''
    #条件判断是否是偶数
    if a%2==0:
        sum+=a
    a+=1
print('1-100之间的偶数和为：',sum)

##for-in循环
#in表达从（字符串、序列等）中依次取值，又称为遍历
#for-in遍历的对象必须是可迭代对象
### for-in的语法结构
#for自定义的变量 in可迭代对象：循环体
### for-in的优点
#循环体内不需要访问自定义变量，可以将自定义变量替代为下划线
for item in "python":
    print(item)
#range()产生一个整数序列，也是一个可迭代对象
for i in range(10,50,5):
    print(i)
#如果在循环体中不需要使用到自定变量，可将自定义变量写为“_”
for _ in range(5):
    print('人生苦短，我用python')

print('使用for循环，计算1到100之间的偶数和')
sun=0#用于存储偶数和
for item in range(1,101):
    if item%2==0:
        sum+=item
print('1-100之间的偶数和为：',sum)

#输出100到999之间的水仙花数
#水仙花数指一个三位数其各位数字的立方和等于该数本身,例如153是“水仙花数”
#153=3*3*3+5*5*5+1*1*1
for item in range(100,1000):
    ge=item%10    #个位
    shi=item//10%10    #十位
    bai=item//100    #百位
    if ge**3+shi**3+bai**3==item:
        print(item)

##流程控制语句break
#用于结束循环结构，通常与分支结构if一起使用
'''从键盘区录入密码，最多录入3次，如果正确就结束循环'''
for item in range(3):
    password=input('请输入密码：')
    if password=='8888':
        print('密码正确')
        break   
    else:
        print('密码不正确')

a=0
while a<3:
    #'''条件执行体（循环体）'''
    password=input('请输入密码：')
    if password=='8888':
       print('密码正确')
       break
    else:
        print("密码不正确")
        a+=1
### 流程控制语句continue
#结束当前循环，进入下一次循环，通常与分支结构中的if一起使用

#输出1到50之间的所有5的倍数
for item in range(1,51):
    if item%5==0:
        print(item)

print('--------使用continue--------')
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)

'''else 语句  
与else语句配合使用的三种情况：
for   else    if条件表达式不成立时执行
while    else // for    else没有碰到break时执行else'''
for item in range(3):
    password=input('请输入密码：')
    if password=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print('对不起，三次密码均失败，请三分钟后再输入密码')

a=0
while a>3:
    password=input('请输入密码：')
    if password=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a+=1
else:
    print('对不起，三次密码均失败，请三分钟后再输入密码')


## 嵌套循环
'''循环结构中有嵌套了另外的完整的循环结构，其中内层循环作为外层循环的循环执行'''
'''输出一个三行四列的矩形'''
for i in range(1,4):#行表，执行三次，一次是一行
    for j in range(1,5):
        print('*',end='\t')#不换行输出
    print()#打行

'''直角三角形'''

for i in range(1,10):
    for j in range(1,i+1):
        print('*',end='')
    print()


'''九九乘法表'''
for i in range(1,10):#行数
    for j in range(1,i+1):
        print(i, '*',j,'=',i*j,end='\t')
    print()

## 二重循环中的break和continue
'''用于控制本层循环'''
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            break#替换为continue
            print(j)

