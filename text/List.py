
bicycles = ['tre','cannondale','redline','specialized']
# ~ python访问最后一个元素的特殊规则
print(bicycles[-1])

for bicycle in bicycles:
	print(bicycle)
	
for value in range(1,6):
	print(value)
	
# ~ 1-10的平方的列表
squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)
	print(squares)
sum(squares)
min(squares)
max(squares)

# ~ 元组
dimensions=(200,100)
print(dimensions)
# ~ dimensions[0]=0
# ~ print(dimensions)

