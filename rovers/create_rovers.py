from rovers.point import Point
from rovers.rover import Rover
from rovers.terrain import Terrain

class CreateRovers(object):
    '''
    CreateRovers onject
    '''

    @staticmethod
    def create_command_from_user_input(input_str):

        # find invalid input
        if not all(Rover.is_valid_movement(char) for char in input_str):
            raise Exception("One of your inputs is not a valid movement")

        return input_str

    @classmethod
    def create_rovers(cls):
        """
        Creates a terrain and rovers based on user input.
        Runs the program until an exception is raised.
        """
        input_str = input(
            "Please enter two positive integer values for the upper-right coordinates of the plateau separated "
            "by a space (like 6 4):")
        terrain = cls.create_terrain_from_user_input(input_str)
        while True:
            input_str = input("Please enter two non-negative integer values for the initial position of the rover "
                              "followed by one of " + "".join([str(elem) + ", " for elem in Rover.DIRECTIONS]) +
                              "for the initial direction separated by a space (like 6 4 W):")
            rover = cls.create_rover_from_user_input(input_str, terrain)
            input_str = input("Please enter a string consisting of " +
                              "".join([str(elem) + ", " for elem in Rover.MOVEMENTS]) + "characters"
                              " that specifies the rover's movement (like LMRLMRLM):").replace(" ", "")
            command = cls.create_command_from_user_input(input_str)
            rover.execute_command(command)
            print("Your rover is at: " + rover.current_position())

    @staticmethod
    def create_rover_from_user_input(input_str, terrain):
        try:
            input_str_list = input_str.split()

            # find invalid input
            if len(input_str_list) != 3:
                raise Exception("You did not input 3 values. Please follow my very polite input instructions next time.")
            num_list = list(map(int, input_str_list[0:2]))
            if not all(i >= 0 for i in num_list):
                raise Exception("One of your first 2 numbers was not a non-negative integer "
                                "[non-negative means bigger than or equal to 0 ;-)].")
            if not Rover.is_valid_direction(input_str_list[2]):
                raise Exception(input_str_list[2] + " is not a valid direction.")
            initial_point = Point(num_list[0], num_list[1])
            if not terrain.is_valid_move(initial_point):
                raise Exception("The initial position (" + str(initial_point.x) + ", " + str(initial_point.y) +") "
                                "of the rover is not on the plateau!")
            # return a Rover object
            return Rover(initial_point, input_str_list[2], terrain)

        except ValueError:
            raise Exception("One of your first two numbers was not an integer. "
                            "Please see the definition for an integer here: https://en.wikipedia.org/wiki/Integer.")

    @staticmethod
    def create_terrain_from_user_input(input_str):
        try:
            num_list = list(map(int, input_str.split()))

            # find invalid input
            if len(num_list) != 2:
                raise Exception("You did not input 2 values. Please follow my very polite input instructions next time.")
            if not all(i > 0 for i in num_list):
                raise Exception("Part of your input was not a positive integer [positive means bigger than 0 ;-)].")

            # return a Terrain object
            return Terrain(Point(num_list[0], num_list[1]))

        except ValueError:
            raise Exception("Part of your input was not an integer. "
                            "Please see the definition for an integer here: https://en.wikipedia.org/wiki/Integer.")