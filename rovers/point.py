class Point(object):
    """
    The Point object stores coordinate points.
    """

    def __init__(self, x=0, y=0):
        """
        Constructor for the Point object

        :param x: The x coordinate point
        :type x: float

        :param y: The y coordinate point
        :type y: float
        """

        self._x = x
        self._y = y

    def __eq__(self, other):
        """
        Determines whether two Point objects are equivalent

        :param other: The other Point object to test
        :type other: Point

        :returns: A boolean that determines whether the two Point objects are equivalent
        :rtype: bool
        """

        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    @property
    def x(self):
        """
        Gets the x value of the coordinate

        :returns: The x value of the coordinate
        :rtype: float
        """

        return self._x

    @x.setter
    def x(self, x):
        """
        Sets the x value of the coordinate

        :param x: The new x value of the coordinate
        :type x: float

        :returns: None
        :rtype: None
        """

        self._x = x

    @property
    def y(self):
        """
        Gets the y value of the coordinate

        :returns: The y value of the coordinate
        :rtype: float
        """

        return self._y

    @y.setter
    def y(self, y):
        """
        Sets the y value of the coordinate

        :param y: The new y value of the coordinate
        :type y: float

        :returns: None
        :rtype: None
        """

        self._y = y