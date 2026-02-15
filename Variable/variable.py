#变量的定义
#例子
name = '小明'         # 定义了一个变量，变量名是'name', 它的值是'zs'
age = 20
height = 180.5
'''
pr:
    1. 等号两边都要保留一个空格
    2. 变量名可以自定义，但要满足'标识符'命名规则。
'''

num1 = 100
num2 = 200
num3 = num1 + num2
num_type = type(num1)
print(type(num1))
print("小明的总分是%d分" % num1)
print(f"我的名字叫{name}，请多多关照！")
print("苹果单价%.02f元／斤，购买%.02f斤，需要支付%.02f元" % (price,weight,price))