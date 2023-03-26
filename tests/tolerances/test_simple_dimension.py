from unittest import TestCase

from src.tolerances.dimensions import SimpleDimension

class TestConstructor(TestCase):
    def test_can_init(self):
        bd = SimpleDimension(
            basic=10, 
            upper_tol=0.5,
            lower_tol=0.5
        )
        self.assertIsInstance(bd, SimpleDimension)

    def test_exception_for_negative_base_dimension(self):
        with self.assertRaises(ValueError):
            _ = SimpleDimension(
            basic=-10, 
            upper_tol=0.5,
            lower_tol=0.5
        )
            
    def test_exception_for_negative_upper_tol(self):
        with self.assertRaises(ValueError):
            _ = SimpleDimension(
            basic=10, 
            upper_tol=-0.5,
            lower_tol=0.5
        )
            
    def test_exception_for_negative_lower_tol(self):
        with self.assertRaises(ValueError):
            _ = SimpleDimension(
            basic=10, 
            upper_tol=0.5,
            lower_tol=-0.5
        )
            
class TestBasic(TestCase):
    def test_returns_correct_value(self):
        bd = SimpleDimension(
            basic=10, 
            upper_tol=0.5,
            lower_tol=0.5
        )
        self.assertEqual(bd.basic, 10)

class TestUpperTol(TestCase):
    def test_returns_correct_value(self):
        bd = SimpleDimension(
            basic=10, 
            upper_tol=0.5,
            lower_tol=0.6
        )
        self.assertEqual(bd.upper_tol, 0.5)

class TestLowerTol(TestCase):
    def test_returns_correct_value(self):
        bd = SimpleDimension(
            basic=10, 
            upper_tol=0.5,
            lower_tol=0.6
        )
        self.assertEqual(bd.lower_tol, 0.6)      

class TestUpperLimit(TestCase):
    def test_returns_correct_value(self):
        bd = SimpleDimension(
            basic=10, 
            upper_tol=0.5,
            lower_tol=0.6
        )
        self.assertEqual(bd.upper_limit, 10.5)

class TestLowerLimit(TestCase):
    def test_returns_correct_value(self):
        bd = SimpleDimension(
            basic=10, 
            upper_tol=0.5,
            lower_tol=0.6
        )
        self.assertEqual(bd.lower_limit, 9.4)

class TestMidpoint(TestCase):
    def test_returns_correct_value(self):
        bd = SimpleDimension(
            basic=10, 
            upper_tol=0.5,
            lower_tol=0.6
        )
        self.assertAlmostEqual(bd.midpoint, 9.95)