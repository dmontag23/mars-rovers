import unittest
from rovers.point import Point

class TestPoint(unittest.TestCase):
    '''
    Tests the Point class.
    '''

    def setUp(self):
        self._x_float_value = -8.45
        self._y_float_value = 4.65
        self._test_point = Point(self._x_float_value, self._y_float_value)

    def test_eq(self):
        new_point = Point(self._x_float_value, self._y_float_value)
        self.assertTrue(self._test_point == new_point)

        new_point = Point(10, 12)
        self.assertFalse(self._test_point == new_point)

        new_point = 34
        self.assertFalse(self._test_point == new_point)

    def test_x_getter(self):
        self.assertEqual(self._x_float_value, self._test_point.x)

    def test_y_getter(self):
        self.assertEqual(self._test_point.y, self._y_float_value)

    def test_x_setter(self):
        new_value = 10
        self._test_point.x = new_value
        self.assertEqual(new_value, self._test_point.x)

    def test_y_setter(self):
        new_value = 5
        self._test_point.y = new_value
        self.assertEqual(new_value, self._test_point.y)


if __name__ == '__main__':
    unittest.main()
