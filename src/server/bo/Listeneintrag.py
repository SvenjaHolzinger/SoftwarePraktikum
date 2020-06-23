from src.server.bo.BusinessObject import BusinessObject
import datetime


class Listeneintrag(BusinessObject):
    def __init__(self):
        super().__init__()
        self._anzahl = None
        self._erledigt = False
        self._änderungs_zeitpunkt = datetime.datetime.now()

    def set_anzahl(self, anzahl):
        """Setzen der Anzahl"""
        self._anzahl = anzahl

    def get_anzahl(self):
        """Auslesen der Anzahl"""
        return self._anzahl

    def set_erledigt(self, status):
        """Setzen des Status erledigt"""
        self._erledigt = status

    def get_erledigt(self):
        """Auslesen von dem Status erledigt"""
        return self._erledigt

    def set_änderungs_zeitpunkt(self, erstellungs_zeitpunkt):
        """Setzen des Änderungszeitpunkt"""
        self._änderungs_zeitpunkt = erstellungs_zeitpunkt

    def get_änderungs_zeitpunkt(self):
        """Auslesen des Änderungszeitpunkt"""
        return self._änderungs_zeitpunkt


    def benutzer_hinzufügen(self, Benutzer):
        """Dem Listeneintrag einen Benutzer hinzufügen"""
        pass

    def benutzer_löschen(self):
        """Einen Benutzer aus dem Listeneintrag löschen"""
        pass

    def artikel_hinzufügen(self, Benutzer):
        """Dem Listeneintrag einen Artikel hinzufügen"""
        pass

    def artikel_löschen(self):
        """Einen Artikel aus dem Listeneintrag löschen"""
        pass

    def einzelhaendler_hinzufügen(self, Benutzer):
        """Dem Listeneintrag einen Einzelhaendler hinzufügen"""
        pass

    def einzelhaendler_löschen(self):
        """Einen Einzelhaendler aus dem Listeneintrag löschen"""
        pass

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "Listeneintrag: {}, {}, {}, {}".format(self.get_id(), self._anzahl, self._erledigt, self._änderungs_zeitpunkt)

    @staticmethod
    def from_dict(dictionary=dict()):
        """Einen Python dict() in einen Listeneintrag() umwandeln."""
        obj = Listeneintrag()
        obj.set_id(dictionary["id"])
        obj.set_anzahl(dictionary["anzahl"])
        obj.set_erledigt(dictionary["erledigt"])
        obj.set_änderungs_zeitpunkt(dictionary["änderungs_zeitpunkt"])
        return obj