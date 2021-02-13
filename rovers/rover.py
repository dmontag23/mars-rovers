class Rover(object):
    """
    Creates a Rover object.
    """

    # stores the possible values of the variables that describe the rover's movements
    DIRECTIONS = ('N', 'E', 'S', 'W')
    MOVEMENTS = ('L', 'R', 'M')

    def __init__(self, initial_position, initial_direction, terrain):
        """
        Initialize a rover
        """
        self._position = initial_position
        self._direction = initial_direction
        self._terrain = terrain

    def current_position(self):
        return str(self._position.x) + " " + str(self._position.y) + " " + self._direction

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, new_direction):
        if self.is_valid_direction(new_direction):
            self._direction = new_direction
        else:
            raise Exception(new_direction + " is not a valid direction!")

    def execute_command(self, command):
        for i in range(len(command)):
            self.execute_movement(command[i])

    def execute_movement(self, movement):
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
        return input_dir in cls.DIRECTIONS

    @classmethod
    def is_valid_movement(cls, input_move):
        return input_move in cls.MOVEMENTS

    def move(self):
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
        return self._position

    @position.setter
    def position(self, new_position):
        if self._terrain.is_valid_move(new_position):
            self._position = new_position
        else:
            raise Exception("You realize the position ("
                            + str(new_position.x) + " " + str(new_position.y) +") is off the plateau right?")

    @property
    def terrain(self):
        return self._terrain

    @terrain.setter
    def terrain(self, new_terrain):
        self._terrain = new_terrain

