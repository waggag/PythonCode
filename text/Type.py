# name = 'abcdefg'
# name[0:4]
#
# name = 'abcdefg'
# for i in name:
#     print(i)
#
# list = [1, 2, 3, 4, 5, 6]
# list1 = [7, 8, 9, 10]
#
# name = 'abcdefb'
# print(name.find("b", 0, len(name)))
# print(name.count('b'))
# name = name.replace('b', 'ab', 2)
# list = name.split(",", 2)
# print(list)
# print(name)
# name = name.join('q')
# print(name)
#
# list.append(7)
# list.extend(list1)
# list.insert(7, 99)
# del list[7]
# del list[7]
# list.pop()
# list.remove(5)
# for i in list:
#     print(i)

dict = {
    'name': "王港",
    'sex': "男",
    'address': "地球亚洲中国"
}
#遍历建
print("遍历键")
for i in dict.keys():
    print(i)

#遍历值
print("遍历值")
for i in dict.values():
    print(i)

#遍历字典元素
print("遍历字典元素")
for i in dict.items():
    print(i)

print(dict.get())

#遍历字典键值对
print("遍历字典键值对")
for key, values in dict.items():
    print("{},{}".format(key, values))
