#测试文件
import sys
print(sys.path.append('..'))
from pythoncode.calc import Calculator

print("aaa")
def test_add():
    cal = Calculator()
    assert 2 == cal.add(1,1)