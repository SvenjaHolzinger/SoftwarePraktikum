from abc import ABC


class BusinessObject(ABC):
    """Gemeinsame Basisklasse aller Klassen in bo.
    Dadurch besitzt jedes BusinessObject eine ID."""
    def __init__(self):
        self._id = 0

    def set_id(self, value):
        """Auslesen der ID."""
        self._id = value

    def get_id(self):
        """Setzen der ID."""
        return self._id
