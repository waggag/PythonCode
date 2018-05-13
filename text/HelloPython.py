
print("Hello Python!")
print("人生苦短，我用Python!")
age = 18
name = "王港"
print("名字：%s,年龄：%X" % (name, age))

# input()函数会把用户输入的任何值都作为字符串来对待
password = input("请输入密码:")
print('您输入的密码是：', password)

# 此时a的类型是一个字符串，里面存放了100这3个字符
# 此时b的类型是整型，里面存放的是数字100

a = '100'
b = int(a)
print("a=%d" % b)

# tuple(s)  将序列 s 转换为一个元组
# list(s)   将序列 s 转换为一个列表
a = 'name'
b = "sdhak"
m = list(a)
m.append(b)
print(m)

# If类型
a = int(input('本次考试成绩：'))
if a >= 60:
    print('这门考试终于过了')

# if…else….类型
a = int(input('本次考试成绩：'))
if a >= 60:
    print('这门考试终于过了')
else:
    print('哎，明年继续裸考')

# if…elif…类型
a = int(input('本次考试成绩：'))
if a >= 90:
    print('成绩优秀')
elif a >= 70:
    print('成绩良好')
elif a >= 60:
    print('成绩及格')
elif a < 60:
    print('大吉大利，明年吃鸡')

CarTicket = 1     # 用1代表有车票，0代表没有车票
KnifeLength = 9     # 刀子的长度，单位为cm
if CarTicket == 1:
    print("有车票，可以进站")
    if KnifeLength < 10:
        print("通过安检，可以上车了")
    else:
        print("没有通过安检")
else:
    print('没有车票，不能上车')

# pass语句   pass是空语句，是为了保持程序结构的完整性，起到占位的作用。

# while循环
i = 1
a = 0
while i <= 100:
    a += i
    i += 1
print("1~100的和%d" % a)

# for循环
for i in range(1, 10):
    print(i)


def add(args1, args2):
    num = args1 + args2
    print(num)


add(4, 6)  # 调用函数，需要在小括号内传入实际值


# 修改全局变量
def func1():
    print('我是函数1')
    print('-----------test1执行完毕 - --------')


def func2():
    print('我是函数2\n')
    func1()
    print('-----------test2执行完毕 - --------')


func2()


