from pizza import make_pizza as mp
from collections import OrderedDict 
# ~ 使用as指定模块的别名
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# ~ Python的标准库,OrderedDict是有序字典
favorite_language= OrderedDict()

favorite_language['jen'] = 'python'
favorite_language['jen1'] = 'c'
favorite_language['jen2'] = 'java'
favorite_language['jen3'] = 'ruby'

for name,value in favorite_language.items():
	print(name.title()+" favorite language "+value.title()+".")

                 
