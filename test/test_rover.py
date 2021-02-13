import unittest
from rovers.point import Point
from rovers.rover import Rover
from rovers.terrain import Terrain

class TestRover(unittest.TestCase):
    '''
    Tests the Rover class.
    '''

    def setUp(self):
        self._test_initial_point = Point(0,0)
        self._test_point = Point(10, 10)
        self._test_direction = 'E'
        self._test_terrain = Terrain(self._test_point)
        self._test_rover = Rover(self._test_initial_point, self._test_direction, self._test_terrain)

    def test_current_position(self):
        self.assertEqual(str(self._test_initial_point.x) + " " + str(self._test_initial_point.y) + " " + self._test_direction,
                         self._test_rover.current_position())

    def test_direction_getter(self):
        self.assertEqual(self._test_direction, self._test_rover.direction)

    def test_direction_setter(self):
        new_value = 'N'
        self._test_rover.direction = new_value
        self.assertEqual(new_value, self._test_rover.direction)

        with self.assertRaises(Exception) as context:
            new_value = 'n'
            self._test_rover.direction = new_value
        self.assertTrue(new_value + ' is not a valid direction!' in str(context.exception))

    def test_execute_command(self):
        self._test_rover.execute_command("LMRRMLMLM")
        self.assertEqual(Point(1,1), self._test_rover.position)
        self.assertEqual('N', self._test_rover.direction)

    def test_execute_movement(self):
        directions = self._test_rover.DIRECTIONS
        self.assertEqual(self._test_direction, self._test_rover.direction)
        new_direction = directions[(directions.index(self._test_rover.direction) + 1) % len(directions)]
        self._test_rover.execute_movement('R')
        self.assertEqual(new_direction, self._test_rover.direction)

        new_direction = directions[(directions.index(self._test_rover.direction) - 1) % len(directions)]
        self._test_rover.execute_movement('L')
        self.assertEqual(new_direction, self._test_rover.direction)

        turns = 6
        new_direction = directions[(directions.index(self._test_rover.direction) + turns) % len(directions)]
        for i in range(turns):
            self._test_rover.execute_movement('R')
        self.assertEqual(new_direction, self._test_rover.direction)

        turns = 6
        new_direction = directions[(directions.index(self._test_rover.direction) - turns) % len(directions)]
        for i in range(turns):
            self._test_rover.execute_movement('L')
        self.assertEqual(new_direction, self._test_rover.direction)

        with self.assertRaises(Exception) as context:
            new_movement = 'n'
            self._test_rover.execute_movement(new_movement)
        self.assertTrue(new_movement + ' is not a valid movement!' in str(context.exception))

    def test_is_valid_direction(self):
        self.assertTrue(self._test_rover.is_valid_direction('N'))
        self.assertTrue(self._test_rover.is_valid_direction('E'))
        self.assertTrue(self._test_rover.is_valid_direction('S'))
        self.assertTrue(self._test_rover.is_valid_direction('W'))
        self.assertFalse(self._test_rover.is_valid_direction('n'))
        self.assertFalse(self._test_rover.is_valid_direction('4'))
        self.assertFalse(self._test_rover.is_valid_direction('432.3'))

    def test_is_valid_movement(self):
        self.assertTrue(self._test_rover.is_valid_movement('L'))
        self.assertTrue(self._test_rover.is_valid_movement('R'))
        self.assertTrue(self._test_rover.is_valid_movement('M'))
        self.assertFalse(self._test_rover.is_valid_movement('l'))
        self.assertFalse(self._test_rover.is_valid_movement('r'))
        self.assertFalse(self._test_rover.is_valid_movement('42'))
        self.assertFalse(self._test_rover.is_valid_movement('42.42'))

    def test_move(self):
        self._test_rover.move()
        self.assertEqual(Point(1,0), self._test_rover.position)

        self._test_rover.direction = 'N'
        self._test_rover.move()
        self.assertEqual(Point(1,1), self._test_rover.position)

        self._test_rover.direction = 'W'
        self._test_rover.move()
        self.assertEqual(Point(0,1), self._test_rover.position)

        self._test_rover.direction = 'S'
        self._test_rover.move()
        self.assertEqual(Point(0,0), self._test_rover.position)

        with self.assertRaises(Exception) as context:
            self._test_rover.move()
        self.assertTrue("The rover moved off the plateau and burst into flame! (You tried to move to: ("
                            + str(self._test_rover._position.x) + " " + str(self._test_rover._position.y) +"))"
                        in str(context.exception))

    def test_position_getter(self):
        self.assertEqual(self._test_initial_point, self._test_rover.position)

    def test_position_setter(self):
        new_value = Point(4,3)
        self._test_rover.position = new_value
        self.assertEqual(new_value, self._test_rover.position)

        with self.assertRaises(Exception) as context:
            new_position = Point(self._test_point.x + 1, 0)
            self._test_rover.position = new_position
        self.assertTrue("You realize the position ("
                            + str(new_position.x) + " " + str(new_position.y) +") is off the plateau right?"
                        in str(context.exception))

    def test_terrain_getter(self):
        self.assertEqual(self._test_terrain, self._test_rover.terrain)

    def test_terrain_setter(self):
        new_terrain = Terrain(Point(9,9))
        self._test_rover.terrain = new_terrain
        self.assertEqual(new_terrain, self._test_rover.terrain)


if __name__ == '__main__':
    unittest.main()
