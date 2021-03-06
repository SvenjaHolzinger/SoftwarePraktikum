class Statistik:

    def __init__(self):
        self._anzahl = 0
        self._ArtikelID = 0
        self._ArtikelName = ""

    def set_ArtikelName(self, artikelname):
        """Setzen des Artikelnamens"""
        self._ArtikelName = artikelname

    def get_ArtikelName(self):
        """Auslesen des Artikelnamens"""
        return self._ArtikelName

    def set_anzahl(self, anzahl):
        """Setzen der Anzahl"""
        self._anzahl = anzahl

    def get_anzahl(self):
        """Auslesen der Anzahl"""
        return self._anzahl

    def set_ArtikelID(self, artikel_id):
        """Setzen der Artikel ID"""
        self._ArtikelID = artikel_id

    def get_ArtikelID(self):
        """Auslesen der Artikel ID"""
        return self._ArtikelID

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "Artikel: {}, {}, {}".format(self._ArtikelID, self._anzahl, self._ArtikelName)
