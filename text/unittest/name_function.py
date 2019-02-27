
def get_formatted_name1(first, last):
	"""生成一个标准的名字"""
	full_name = first + " " +last
	return full_name.title().strip()

print(get_formatted_name1("wang","gang"))

def get_formatted_name2(first, last, middle):
	if middle:
		full_name = first + " " + middle + " " +last
	else:
		full_name = first + " " + last
	return full_name
