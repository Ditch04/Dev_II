import unittest
from Fraction import Fraction


class TestFraction(unittest.TestCase):

    def test_init(self):
        self.assertEqual(str(Fraction(2, 3)), "2/3")
        self.assertEqual(str(Fraction(4, 8)), "1/2")
        self.assertEqual(str(Fraction(3, 3)), "1")
        self.assertEqual(str(Fraction(1, -3)), "-1/3")
        self.assertEqual(str(Fraction(6, 3)), "2")
        self.assertEqual(str(Fraction(9, -3)), "-3")
        self.assertEqual(str(Fraction(-2, 5)), "-2/5")
        self.assertEqual(str(Fraction(-1, -1)), "1")
        self.assertEqual(str(Fraction(-4, 2)), "-2")
        self.assertEqual(str(Fraction(-9, 3)), "-3")
        self.assertEqual(str(Fraction(0, 3)), "0")
        self.assertEqual(str(Fraction(0, -2)), "0")
        self.assertEqual(str(Fraction(0, 3)), "0")

    def test_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)
        with self.assertRaises(ZeroDivisionError):
            Fraction(2, 0)
        with self.assertRaises(ZeroDivisionError):
            Fraction(-1, 0)
        with self.assertRaises(ZeroDivisionError):
            Fraction(-3, 0)
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0)

    def test_mixed_number(self):
        self.assertEqual(Fraction(2, 3).as_mixed_number(), '2/3')
        self.assertEqual(Fraction(9, 4).as_mixed_number(), '2 + 1/4')
        self.assertEqual(Fraction(3, 3).as_mixed_number(), '1')

    def test_float(self):
        self.assertEqual(float(Fraction(2, 5)), 0.4)
        self.assertEqual(float(Fraction(7, 4)), 1.75)
        self.assertEqual(float(Fraction(0, 5)), 0)
        self.assertEqual(float(Fraction(-2, 4)), -0.5)

    def test_is_zero(self):
        self.assertEqual(Fraction(0, 4).is_zero(), True)
        self.assertEqual(Fraction(1, 4).is_zero(), False)

    def test_is_int(self):
        self.assertEqual(Fraction(1, 3).is_integer(), False)
        self.assertEqual(Fraction(3, 3).is_integer(), True)
        self.assertEqual(Fraction(-5, 3).is_integer(), False)
        self.assertEqual(Fraction(0, 3).is_integer(), True)

    def test_is_proper(self):
        self.assertEqual(Fraction(1, 3).is_proper(), True)
        self.assertEqual(Fraction(0, 3).is_proper(), True)
        self.assertEqual(Fraction(-2, 3).is_proper(), True)
        self.assertEqual(Fraction(4, 3).is_proper(), False)

    def test_is_unit(self):
        self.assertEqual(Fraction(1, 3).is_unit(), True)
        self.assertEqual(Fraction(7, 3).is_unit(), False)
        self.assertEqual(Fraction(0, 3).is_unit(), False)
        self.assertEqual(Fraction(-1, 3).is_unit(), False)

    def test_adjacent_to(self):
        self.assertEqual((Fraction(1, 8)).is_adjacent_to(Fraction(1, 9)), True)
        self.assertEqual((Fraction(1, 9)).is_adjacent_to(Fraction(1, 8)), True)
        self.assertEqual((Fraction(3, 4)).is_adjacent_to(Fraction(2, 3)), True)
        self.assertEqual((Fraction(0, 6)).is_adjacent_to(Fraction(3, 7)), False)
        self.assertEqual((Fraction(8, 3)).is_adjacent_to(Fraction(3, 4)), False)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) + 'ah'
        with self.assertRaises(TypeError):
            Fraction(1, 2) - None
        with self.assertRaises(TypeError):
            Fraction(1, 2) / 'st'
        with self.assertRaises(TypeError):
            Fraction(1, 2) * 2

    def test_add(self):
        self.assertEqual(Fraction(1, 3) + Fraction(1, 3), Fraction(2, 3))
        self.assertEqual(Fraction(1, 2) + Fraction(1, 2), Fraction(1, 1))
        self.assertEqual(Fraction(3, 4) + Fraction(5, 2), Fraction(13, 4))
        self.assertEqual(Fraction(0, 2) + Fraction(0, 2), Fraction(0, 1))
        self.assertEqual(Fraction(-1, 3) + Fraction(1, 3), Fraction(0, 1))
        self.assertEqual(Fraction(0, 2) + Fraction(-1, 3), Fraction(-1, 3))
        self.assertEqual(Fraction(-1, 4) + Fraction(-2, 4), Fraction(-3, 4))

    def test_sub(self):
        self.assertEqual(Fraction(1, 3) - Fraction(1, 3), Fraction(0, 1))
        self.assertEqual(Fraction(3, 2) - Fraction(1, 2), Fraction(1, 1))
        self.assertEqual(Fraction(3, 4) - Fraction(5, 2), Fraction(-7, 4))
        self.assertEqual(Fraction(0, 2) - Fraction(0, 2), Fraction(0, 1))
        self.assertEqual(Fraction(-1, 3) - Fraction(1, 3), Fraction(-2, 3))
        self.assertEqual(Fraction(0, 2) - Fraction(-1, 3), Fraction(1, 3))
        self.assertEqual(Fraction(-1, 4) - Fraction(-2, 4), Fraction(1, 4))

    def test_mul(self):
        self.assertEqual(Fraction(1, 3) * Fraction(1, 3), Fraction(1, 9))
        self.assertEqual(Fraction(1, 2) * Fraction(1, 2), Fraction(1, 4))
        self.assertEqual(Fraction(3, 4) * Fraction(5, 2), Fraction(15, 8))
        self.assertEqual(Fraction(0, 2) * Fraction(0, 2), Fraction(0, 1))
        self.assertEqual(Fraction(-1, 3) * Fraction(1, 3), Fraction(-1, 9))
        self.assertEqual(Fraction(0, 2) * Fraction(-1, 3), Fraction(0, 1))
        self.assertEqual(Fraction(-1, 4) * Fraction(-2, 4), Fraction(1, 8))

    def test_div(self):
        self.assertEqual(Fraction(1, 3) / Fraction(1, 3), Fraction(1, 1))
        self.assertEqual(Fraction(-1, 3) / Fraction(1, 3), Fraction(-1, 1))
        self.assertEqual(Fraction(3, 4) / Fraction(5, 2), Fraction(3, 10))
        self.assertEqual(Fraction(0, 2) / Fraction(1, 2), Fraction(0, 1))
        self.assertEqual(Fraction(5, 3) / Fraction(5, 3), Fraction(1, 1))
        self.assertEqual(Fraction(-1, 2) / Fraction(5, 3), Fraction(-3, 10))
        self.assertEqual(Fraction(1, 4) / Fraction(-2, 4), Fraction(-1, 2))
        self.assertEqual(Fraction(-1, 4) / Fraction(-2, 4), Fraction(1, 2))

    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2) / Fraction(0, 3)
        with self.assertRaises(ZeroDivisionError):
            Fraction(7, 3) / Fraction(0, 5)
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 4) / Fraction(0, 2)
        with self.assertRaises(ZeroDivisionError):
            Fraction(-1, 4) / Fraction(0, 2)

    def test_pow(self):
        self.assertEqual(pow(Fraction(1, 3), 0), Fraction(1, 1))
        self.assertEqual(pow(Fraction(1, 3), 1), Fraction(1, 3))
        self.assertEqual(pow(Fraction(1, 3), -1), Fraction(3, 1))
        self.assertEqual(pow(Fraction(-1, 3), -1), Fraction(-3, 1))
        self.assertEqual(pow(Fraction(0, 4), 2), Fraction(0, 1))
        self.assertEqual(pow(Fraction(-2, 3), 2), Fraction(4, 9))
        self.assertEqual(pow(Fraction(1, 3), 2), Fraction(1, 9))
        self.assertEqual(pow(Fraction(7, 3), 2), Fraction(49, 9))

    def test_equal(self):
        self.assertEqual(Fraction(1, 4) == Fraction(1, 4), True)
        self.assertEqual(Fraction(2, 4) == Fraction(1, 2), True)
        self.assertEqual(Fraction(0, 4) == Fraction(0, 4), True)
        self.assertEqual(Fraction(1, 4) == Fraction(3, 4), False)
        self.assertEqual(Fraction(-1, 4) == Fraction(1, 5), False)


if __name__ == "__main__":
    unittest.main()
