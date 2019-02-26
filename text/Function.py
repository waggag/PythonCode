for i in 'names':
    if i == 'e':
        break
    print(i)

first = int(input("输入第一个数字"))
second = int(input("请输入第二个数字"))

# 函数


def add1():
    num1 = 5
    num2 = 8
    num3 = num1 + num2
    print(num3)


def add2(e, b):
    print(e+b)


def add3(e, b):
    return e+b


print(add3(first, second))


def fun1():
    print("First function!")


def fun2():
    fun1()
    print("Second function")


fun2()
fun1()

# ~ 禁止函数修改列表,使用切片，保留未打印的列表
# ~ function_name(list_name[:])

# ~ 传递任意数量的实参

def make_pizza(*toppings):
	"""打印所有的配料"""
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers')
