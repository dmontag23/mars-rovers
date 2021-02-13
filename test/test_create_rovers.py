import unittest
from rovers.create_rovers import CreateRovers
from rovers.point import Point
from rovers.terrain import Terrain

class TestCreateRovers(unittest.TestCase):
    '''
    Tests the CreateRovers class.
    '''

    def test_create_command_from_user_input(self):
        input_string = "MLRMMRL"
        self.assertEqual(input_string, CreateRovers.create_command_from_user_input(input_string))

        with self.assertRaises(Exception) as context:
            input_string = "MLRMOMRL"
            CreateRovers.create_command_from_user_input(input_string)
        self.assertTrue("One of your inputs is not a valid movement" in str(context.exception))

    def test_create_rover_from_user_input(self):
        mock_terrain = Terrain(Point(10, 10))

        input_string = "0 0 N"
        rover = CreateRovers.create_rover_from_user_input(input_string, mock_terrain)
        self.assertIsNotNone(rover)
        self.assertEqual(mock_terrain, rover.terrain)
        self.assertEqual('N', rover.direction)
        self.assertEqual(Point(0, 0), rover.position)

        with self.assertRaises(Exception) as context:
            input_string = "MLRMMRL"
            CreateRovers.create_rover_from_user_input(input_string, mock_terrain)
        self.assertTrue("You did not input 3 values. Please follow my very polite input instructions next time."
                        in str(context.exception))

        with self.assertRaises(Exception) as context:
            input_string = "-9 0 W"
            CreateRovers.create_rover_from_user_input(input_string, mock_terrain)
        self.assertTrue("One of your first 2 numbers was not a non-negative integer "
                        "[non-negative means bigger than or equal to 0 ;-)]" in str(context.exception))

        with self.assertRaises(Exception) as context:
            input_string = "0 -2 W"
            CreateRovers.create_rover_from_user_input(input_string, mock_terrain)
        self.assertTrue("One of your first 2 numbers was not a non-negative integer "
                        "[non-negative means bigger than or equal to 0 ;-)]" in str(context.exception))

        with self.assertRaises(Exception) as context:
            input_string = "0.4 6 W"
            CreateRovers.create_rover_from_user_input(input_string, mock_terrain)
        self.assertTrue("One of your first two numbers was not an integer. "
                        "Please see the definition for an integer here: https://en.wikipedia.org/wiki/Integer"
                        in str(context.exception))

        with self.assertRaises(Exception) as context:
            input_string = "0 dfgdf W"
            CreateRovers.create_rover_from_user_input(input_string, mock_terrain)
        self.assertTrue("One of your first two numbers was not an integer. "
                        "Please see the definition for an integer here: https://en.wikipedia.org/wiki/Integer"
                        in str(context.exception))

        with self.assertRaises(Exception) as context:
            input_string = "0 6 w"
            CreateRovers.create_rover_from_user_input(input_string, mock_terrain)
        self.assertTrue("w is not a valid direction." in str(context.exception))

        with self.assertRaises(Exception) as context:
            input_string = "11 6 W"
            CreateRovers.create_rover_from_user_input(input_string, mock_terrain)
        self.assertTrue("The initial position (11, 6) of the rover "
                                "is not on the plateau!" in str(context.exception))

        with self.assertRaises(Exception) as context:
            input_string = "9 11 W"
            CreateRovers.create_rover_from_user_input(input_string, mock_terrain)
        self.assertTrue("The initial position (9, 11) of the rover "
                                "is not on the plateau!" in str(context.exception))

    def test_create_terrain_from_user_input(self):
        input_string = "10 10"
        terrain = CreateRovers.create_terrain_from_user_input(input_string)
        self.assertIsNotNone(terrain)
        self.assertEqual(Terrain(Point(10, 10)), terrain)

        with self.assertRaises(Exception) as context:
            input_string = "0"
            CreateRovers.create_terrain_from_user_input(input_string)
        self.assertTrue("You did not input 2 values. Please follow my very polite input instructions next time."
                        in str(context.exception))

        with self.assertRaises(Exception) as context:
            input_string = "1 -2"
            CreateRovers.create_terrain_from_user_input(input_string)
        self.assertTrue("Part of your input was not a positive integer [positive means bigger than 0 ;-)]"
                        in str(context.exception))

        with self.assertRaises(Exception) as context:
            input_string = "0 1"
            CreateRovers.create_terrain_from_user_input(input_string)
        self.assertTrue("Part of your input was not a positive integer [positive means bigger than 0 ;-)]"
                        in str(context.exception))

        with self.assertRaises(Exception) as context:
            input_string = "6.344 1"
            CreateRovers.create_terrain_from_user_input(input_string)
        self.assertTrue("Part of your input was not an integer. "
                        "Please see the definition for an integer here: https://en.wikipedia.org/wiki/Integer"
                        in str(context.exception))

        with self.assertRaises(Exception) as context:
            input_string = "3 asdfd"
            CreateRovers.create_terrain_from_user_input(input_string)
        self.assertTrue("Part of your input was not an integer. "
                        "Please see the definition for an integer here: https://en.wikipedia.org/wiki/Integer"
                        in str(context.exception))


if __name__ == '__main__':
    unittest.main()