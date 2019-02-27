###读取JSon数据###
import json

filename = 'nmber.json'
with open(filename) as f_obj:
	numbers = json.load(f_obj)
	
print(numbers)
