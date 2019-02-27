import json

# ~ 将数字列表存储到Json中
numbers = [2,3,4,5,6,7,8,9]

filename = "nmber.json"
with open(filename, 'w') as f_object:
	json.dump(numbers,f_object)
