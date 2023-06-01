import unittest 
from feature import add
from feature import sub
from feature import pyt

class TestAdd(unittest.TestCase):
    def test_add_pos(self):
        a,b = 2,2
        self.assertEqual(add(a,b), a+b)

    def test_add_neg(self):
        a,b = -2,-2
        self.assertEqual(add(a,b), a+b)

    def test_add_float(self):
        a,b = 2.5,2.5
        self.assertEqual(add(a,b), a+b)
   
    def test_add_binary(self):
        a,b = 0b01, 0b10
        self.assertEqual(add(a,b), a+b)

class TestSub(unittest.TestCase):
    def test_sub_pos(self):
        a,b = 2,2
        self.assertEqual(sub(a,b), a-b)

    def test_sub_neg(self):
        a,b = -2,-2
        self.assertEqual(sub(a,b), a-b)

    def test_sub_float(self):
        a,b = 2.5,2.5
        self.assertEqual(sub(a,b), a-b)
   
    def test_sub_binary(self):
        a,b = 0b01, 0b10
        self.assertEqual(sub(a,b), a-b)

class TestPyt(unittest.TestCase):
    def test_pyt(self):
        self.assertEqual(pyt(3,4), 5)


