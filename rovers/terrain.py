from rovers.point import Point

class Terrain(object):
    """
    The Terrain object stores all information related to a terrain that a rover can move on.
    Note: For this project, we assume the terrain is a grid with integer coordinates
    """

    def __init__(self, upper_edge_coords):
        """
        Constructor for the Terrain object

        :param upper_edge_coords: The coordinates of the upper-right edge of the terrain
        :type upper_edge_coords: Point
        """

        self._upper_edge_coords = upper_edge_coords

    def __eq__(self, other):
        """
        Determines whether two Terrain objects are equivalent

        :param other: The other Terrain object to test
        :type other: Terrain

        :returns: A boolean that determines whether the two Terrain objects are equivalent
        :rtype: bool
        """

        if isinstance(other, Terrain):
            return self.upper_edge_coords == other.upper_edge_coords
        return False

    def is_valid_move(self, coords_to_validate):
        """
        Determines whether the given coordinates are on the terrain grid

        :param coords_to_validate: The coordinates of the point to validate
        :type coords_to_validate: Point

        :returns: A boolean that determines whether the coordinates are on the terrain grid
        :rtype: bool
        """

        return 0 <= coords_to_validate.x <= self._upper_edge_coords.x and \
               0<= coords_to_validate.y <= self._upper_edge_coords.y

    @property
    def upper_edge_coords(self):
        """
        Gets the coordinates of the upper-right edge of the terrain

        :returns: The coordinates of the upper-right edge of the terrain
        :rtype: Point
        """

        return self._upper_edge_coords

    @upper_edge_coords.setter
    def upper_edge_coords(self, new_point):
        """
        Sets the coordinates of the upper-right edge of the terrain

        :param new_point: The coordinates of the upper-right edge of the terrain
        :type new_point: Point

        :returns: None
        :rtype: None
        """

        self._upper_edge_coords = new_point