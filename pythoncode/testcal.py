import pytest
from pythoncode.calculator import Calculator
class Testcalcu():
    def setup_class(self):
        self.cal=Calculator()
    def teardown_class(self):
        print('计算器类测试结束')
    @pytest.mark.parametrize('a,b,expect',[(1,1,2),(-1,-2,-3),(0.5,0.1,0.6)],ids=['+','-','.'])
    def test_add(self,a,b,expect):
        assert self.cal.add(a,b)==expect
    @pytest.mark.parametrize('a,b,expect', [(1, 1, 0), (-1, -2, 1), (0.5, 0.1, 0.4)], ids=['+', '-', '.'])
    def test_sub(self,a,b,expect):
        assert self.cal.sub(a,b)==expect
    @pytest.mark.parametrize('a,b,expect', [(1, 1, 1), (-1, -2, 2), (0.5, 0.1, 0.05)], ids=['+', '-', '.'])
    def test_mul(self,a,b,expect):
        assert  self.cal.mul(a,b)==expect
    @pytest.mark.parametrize('a,b,expect', [(1, 1, 1), (-1, -2, 0.5), (0.5, 0.1, 5)], ids=['+', '-', '.'])
    def test_div(self,a,b,expect):
        assert  self.cal.div(a,b)==expect