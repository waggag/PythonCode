import json

#经典的重构代码

#定义问候用户的函数
def greet_user():
	"""问候用户并指出其姓名"""
	#如果以前存储了用户名就加载用户名
	#否则就提示用户输入用户名
	filename = "username.json"
	
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		username = input("What is you name? ")
		with open(filename,'w') as f_obj:
			json.dump(username,f_obj)
			print("We'll remember you when you come back, "+ username + '！')
	else:
		print("Weclome back, "+ username + "!")

greet_user()


def get_stored_username():
	"""如果存在用户名，就获取他"""
	filename = "username.json"
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return NONE
	else:
		return username

def greet_user2():
	"""问候姓名并指出其名字"""
	username = get_stored_username()
	if username:
		print("Weclome back, " + username + " !")
	else:
		username = input("What is you name: ")
		filename = "username.json"
		with open(filename) as f_obj:
			json.dump(username,f_obj)
			print("We'll remember you when you come back, "+ username + " !")
	
greet_user2()


def get_new_user():
	"""获取新用户输入名"""
	username = input("What is you name:")
	filename = "username.json"
	with open(filename) as f_obj:
		json.dump(username,f_obj)
	return username
	
def greet_user3():
	username = get_stored_username()
	if username:
		print("Weclome back, " + username + " !")
	else:
		username = get_new_user()
		print("We'll remember you when you come back, " + username + " !")

greet_user3()
