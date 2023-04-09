import unittest
import chg_exponential_notation


class MyTestCase(unittest.TestCase):
    def test_is_decimal(self):
        self.assertEqual(chg_exponential_notation.is_decimal("123"), True)  # add assertion here
        self.assertEqual(chg_exponential_notation.is_decimal("123.01"), True)
        self.assertEqual(chg_exponential_notation.is_decimal("123."), False)
        self.assertEqual(chg_exponential_notation.is_decimal(".01"), False)
        self.assertEqual(chg_exponential_notation.is_decimal("0.0123.3"), False)

    def test_chg_exponential_notation(self):
        dec_format = "0.000001"
        self.assertEqual(chg_exponential_notation.chg_exponential_notation("123456789", dec_format), "1.234568E+08")
        self.assertEqual(chg_exponential_notation.chg_exponential_notation("-123456789", dec_format), "-1.234568E+08")
        self.assertEqual(chg_exponential_notation.chg_exponential_notation("1.23456789", dec_format), "1.234568E+00")
        self.assertEqual(chg_exponential_notation.chg_exponential_notation("0.0123456789", dec_format), "1.234568E-02")


if __name__ == '__main__':
    unittest.main()
