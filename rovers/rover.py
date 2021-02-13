from rovers.point import Point
from rovers.terrain import Terrain

class Rover(object):
    """
    The Rover object stores all information related to a rover and the methods used to manipulate the rover on its
    terrain.
    """

    # stores the possible values of the variables that describe the rover's movements
    DIRECTIONS = ('N', 'E', 'S', 'W')
    MOVEMENTS = ('L', 'R', 'M')

    def __init__(self, initial_position, initial_direction, terrain):
        """
        Constructor for the Rover object

        :param initial_position: Coordinate point that gives the initial position of the rover
        :type initial_position: Point

        :param initial_direction: Gives the initial direction of the rover
        :type initial_direction: str

        :param terrain: Gives the initial direction of the rover
        :type terrain: Terrain
        """

        self._position = initial_position
        self._direction = initial_direction
        self._terrain = terrain

    def current_position(self):
        """
        Gives the current position of the rover in terms of its current coordinates and direction

        :returns: The current position of the rover
        :rtype: str
        """

        return str(self._position.x) + " " + str(self._position.y) + " " + self._direction

    @property
    def direction(self):
        """
        Gives the current direction of the rover

        :returns: The current direction of the rover
        :rtype: str
        """

        return self._direction

    @direction.setter
    def direction(self, new_direction):
        """
        Sets the current direction of the rover

        :param new_direction: The new direction the rover is facing
        :type new_direction: str

        :returns: None
        :rtype: None
        """

        if self.is_valid_direction(new_direction):
            self._direction = new_direction
        else:
            raise Exception(new_direction + " is not a valid direction!")

    def execute_command(self, command):
        """
        Runs a command string to move the rover in the specified directions

        :param command: The command to move the rover
        :type command: str

        :returns: None
        :rtype: None
        """

        for i in range(len(command)):
            self.execute_movement(command[i])

    def execute_movement(self, movement):
        """
        Takes a movement from the MOVEMENTS tuple and executes the corresponding action on the rover

        :param movement: The character from the MOVEMENTS tuple to perform on the rover
        :type movement: str

        :returns: None
        :rtype: None
        """

        if not self.is_valid_movement(movement):
            raise Exception(movement + " is not a valid movement!")
        if movement == 'L':
            self._direction = self.DIRECTIONS[(self.DIRECTIONS.index(self._direction) - 1) % len(self.DIRECTIONS)]
        elif movement == 'R':
            self._direction = self.DIRECTIONS[(self.DIRECTIONS.index(self._direction) + 1) % len(self.DIRECTIONS)]
        elif movement == 'M':
            self.move()

    @classmethod
    def is_valid_direction(cls, input_dir):
        """
        Determines whether the input string is a valid direction

        :param input_dir: The directional string to validate
        :type input_dir: str

        :returns: A boolean that determines whether the input string is a valid direction
        :rtype: bool
        """

        return input_dir in cls.DIRECTIONS

    @classmethod
    def is_valid_movement(cls, input_move):
        """
        Determines whether the input string is a valid movement

        :param input_move: The movement string to validate
        :type input_move: str

        :returns: A boolean that determines whether the input string is a valid movement
        :rtype: bool
        """

        return input_move in cls.MOVEMENTS

    def move(self):
        """
        Moves the rover by one grid point in the direction it is currently headed

        :returns: None
        :rtype: None
        """

        if self._direction == 'N':
            self._position.y += 1
        elif self._direction == 'E':
            self._position.x += 1
        elif self._direction == 'S':
            self._position.y -= 1
        elif self._direction == 'W':
            self._position.x -= 1
        if not self._terrain.is_valid_move(self._position):
            raise Exception("The rover moved off the plateau and burst into flame! (You tried to move to: ("
                            + str(self._position.x) + " " + str(self._position.y) +"))")

    @property
    def position(self):
        """
        Returns the current position of the rover on the terrain grid

        :returns: Coordinates representing the current position of the rover
        :rtype: Point
        """

        return self._position

    @position.setter
    def position(self, new_position):
        """
        Sets the current position of the rover on the terrain grid

        :param new_position: The new coordinates of the rover
        :type new_position: Point

        :returns: None
        :rtype: None
        """

        if self._terrain.is_valid_move(new_position):
            self._position = new_position
        else:
            raise Exception("You realize the position ("
                            + str(new_position.x) + " " + str(new_position.y) +") is off the plateau right?")

    @property
    def terrain(self):
        """
        Gets the current terrain that the rover moves on

        :returns: The current rover terrain
        :rtype: Terrain
        """

        return self._terrain

    @terrain.setter
    def terrain(self, new_terrain):
        """
        Sets the current terrain that the rover moves on

        :param new_terrain: The new terrain the rover moves on
        :type new_terrain: Terrain

        :returns: None
        :rtype: None
        """

        self._terrain = new_terrain

