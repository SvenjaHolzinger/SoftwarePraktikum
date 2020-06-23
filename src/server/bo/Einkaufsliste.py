from src.server.bo.NamedBO import NamedBO
import datetime


class Einkaufsliste(NamedBO):
    def __init__(self):
        super().__init__()
        self.änderungs_zeitpunkt = datetime.datetime.now()

    def eintrag_hinzufügen(self):
        """Einen Listeneintrag der Einkaufsliste hinzufügen"""
        pass

    def eintrag_löschen(self):
        """Einen Listeneintrag der Einkaufsliste löschen"""
        pass

    def set_änderungs_zeitpunkt(self, erstellungs_zeitpunkt):
        """Setzen des Änderungszeitpunkt"""
        self.änderungs_zeitpunkt = erstellungs_zeitpunkt

    def get_änderungs_zeitpunkt(self):
        """Auslesen des Änderungszeitpunkt"""
        return self.änderungs_zeitpunkt

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "Einkaufsliste: {}, {}, {}, {}".format(self.get_id(), self.get_name(), self.get_erstellungs_zeitpunkt(), self.änderungs_zeitpunkt)

    @staticmethod
    def from_dict(dictionary=dict()):
        """Einen Python dict() in einer Einkaufsleiste() umwandeln."""
        obj = Einkaufsliste()
        obj.set_id(dictionary["id"])
        obj.set_name(dictionary["name"])
        obj.set_erstellungs_zeitpunkt(dictionary["erstellungs_zeitpunkt"])
        obj.set_änderungs_zeitpunkt(dictionary["änderungs_zeitpunkt"])
        return obj