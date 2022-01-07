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
