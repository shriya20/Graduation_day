import unittest
from graduation_day import testing_purpose


class TestStringMethods(unittest.TestCase):
    # test function to test equality of two value
    def test_first_case(self):
        expected_output = '14/29'
        message = "First value and second value are not equal !"
        grad_test = testing_purpose(5, 0, 0, 0)
        grad = grad_test.test_method()
        grad.calculateMissWays()
        grad.calculate_result()
        result = grad.res
        self.assertEqual(expected_output, result, message)

    def test_second_case(self):
        expected_output = '379/775'
        message = "First value and second value are not equal !"
        grad_test = testing_purpose(10, 0, 0, 0)
        grad = grad_test.test_method()

        grad.calculateMissWays()
        grad.calculate_result()
        result = grad.res
        self.assertEqual(expected_output, result, message)


if __name__ == "__main__":

    unittest.main()
