
import unittest
from name_function import get_formatted_name1
	

class NamesTestCase(unittest.TestCase):
	"""测试name_function.py"""
	def test_first_last_name(self):
		"""能够正确的处理wang gang这样的姓名嘛？"""
		formatted_name = get_formatted_name1('wang', "gang")
		self.assertEqual(formatted_name, 'Wang Gang')
	
unittest.main()
