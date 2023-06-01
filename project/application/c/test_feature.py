import unittest
import random 
from feature import mean
from feature import median
from feature import mode
from feature import numb_count



class TestStat(unittest.TestCase):
    def test_mean_pos(self):
        a,b = 2,2
        self.assertEqual(mean(a,b), (a+b)/2)

    def test_mean_neg(self):
        a,b = -2,-2
        self.assertEqual(mean(a,b), (a+b)/2)
        
    def test_median_even(self):
        numb = [1, 2, 4, 5]
        sort = sorted(numb)
        length = len(sort) 
        mid1 = sort[length // 2 - 1]
        mid2 = sort[length // 2]
        self.assertEqual(median(numb), (mid1 + mid2) / 2)
        
    def test_median_odd(self):
        numb = [1, 2, 4, 5, 3]
        sort = sorted(numb)
        length = len(sort) 
        self.assertEqual(median(numb), sort[length // 2])

    def test_mode(self):
        numb = [1, 2, 4, 5, 3]
        numb_dict = {}
        for i in numb:
            if i in numb_dict:
                numb_dict[i] +=1
            else:
                numb_dict[i] =1
        self.assertEqual(mode(numb), max(numb_dict, key=numb_dict.get))

