
filename = 'programmer.txt'

###实参为w写入内容，实参为r,追加文件内容
with open(filename,'a') as file_object:
	while True:
		file_object.write("I Love m\n")
		file_object.write("I Love python\n")
