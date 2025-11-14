# https://github.com/Divya0822/COP-Lab
# Partner 1: Divya Singh
# Partner 2: Anabel
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3,2),5)
        self.assertEqual(add(10,-2),8)
        self.assertEqual(add(-10,2),-8)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5,2),3)
        self.assertEqual(subtract(-10,6),-16)
        self.assertEqual(subtract(10,-6),16) 

    ######### Partner 1
    def test_multiply(self):  
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-4, 5), -20)
        self.assertEqual(mul(0, 10), 0)
    def test_divide(self):  
        self.assertEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(7, 2), 3.5)
        self.assertEqual(div(-9, 3), -3)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(3,27), 3.0)
        self.assertEqual(logarithm(2,0.5), -1.0)
        self.assertEqual(logarithm(10,10),1)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-2,8)
    
    ######### Partner 1
    def test_log_invalid_argument(self): 
        with self.assertRaises(ValueError):
            logarithm(0, 10)
    def test_hypotenuse(self): 
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(8, 15), 17.0)

    def test_sqrt(self): 
        
        with self.assertRaises(ValueError):
            square_root(-4)

        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(2.25), 1.5)  


if __name__ == "__main__":
    unittest.main()