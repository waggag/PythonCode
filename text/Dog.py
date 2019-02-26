
class Dog:
    """一次模拟小狗的简单尝试,可以生成文档"""
	# ~ 需要指定self，但不需要给其传实参                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗的蹲下"""
        print(self.name.title() + " is now sitting!")

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + "rolled over!")
