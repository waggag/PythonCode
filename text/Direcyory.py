# ~ 常用的字典写法
aliens_0 = {
	'color':'green',
	'point':'5',
}
print(aliens_0)
del aliens_0['point']
print(aliens_0)

# ~ 遍历字典
user_0 = {
	'username' : 'waggag',
	'password' : '256518',
	'last' 	: 'fermi',
}

for key,value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)
	
# ~ set集合，提取相同的值
favorite_language = {
	'jen' : 'pyton',
	'sarch' : 'c',
	'edward' : 'ruby',
	'pjil' : 'python',
}

print("The following languages have been mentioned: ")
for language in set(favorite_language.values()):
	print(language.title())
