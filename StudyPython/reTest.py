import re

str = """这是一个测试字符串"""

re_test = re.compile("一个")

result = re_test.findall(str)

print(result)
