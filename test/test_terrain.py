import unittest
from rovers.point import Point
from rovers.terrain import Terrain

class TestTerrain(unittest.TestCase):
    '''
    Tests the Terrain class.
    '''

    def setUp(self):
        self._test_point = Point(10, 5)
        self._test_terrain = Terrain(self._test_point)

    def test_upper_edge_coords_getter(self):
        self.assertEqual(self._test_point, self._test_terrain.upper_edge_coords)

    def test_upper_edge_coords_setter(self):
        new_point = Point(-7, 3.2)
        self._test_terrain.upper_edge_coords = new_point
        self.assertEqual(new_point, self._test_terrain.upper_edge_coords)

    def test_is_valid_move(self):
        self.assertTrue(self._test_terrain.is_valid_move(self._test_point))
        self.assertTrue(self._test_terrain.is_valid_move(Point(0, 0)))
        self.assertTrue(self._test_terrain.is_valid_move(Point(0.2, 4.2)))
        self.assertFalse(self._test_terrain.is_valid_move(Point(-0.2, 4.2)))
        self.assertFalse(self._test_terrain.is_valid_move(Point(10.2, 4.2)))
        self.assertFalse(self._test_terrain.is_valid_move(Point(0.2, -4.2)))
        self.assertFalse(self._test_terrain.is_valid_move(Point(0.2, 5.2)))


if __name__ == '__main__':
    unittest.main()
