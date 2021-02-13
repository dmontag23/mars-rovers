class Terrain(object):
    """
    Creates a Terrain object.
    """

    def __init__(self, upper_edge_coords):
        self._upper_edge_coords = upper_edge_coords

    def __eq__(self, other):
        if isinstance(other, Terrain):
            return self.upper_edge_coords == other.upper_edge_coords
        return False

    @property
    def upper_edge_coords(self):
        return self._upper_edge_coords

    @upper_edge_coords.setter
    def upper_edge_coords(self, new_point):
        self._upper_edge_coords = new_point

    def is_valid_move(self, new_position):
        return 0 <= new_position.x <= self._upper_edge_coords.x and 0<= new_position.y <= self._upper_edge_coords.y