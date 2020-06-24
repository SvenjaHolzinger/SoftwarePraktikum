from src.server.db.Mapper import Mapper
from src.server.bo.Artikel import Artikel


class ArtikelMapper(Mapper):

    def __init__(self):
        super().__init__()

    """ Mapper-Methode zum ausgeben aller Artikel aus der Datenbank"""

    """Hier werden via SQL-Abfrage alle Artikel aus der Datenbank ausgegeben.
       Anschließend werden aus den Zeilen der Datenbank (welche ein Objekt mit dessen Attributen darstellen) 
       mit der fetchall-Methode Tupel erstellt. 

       Mittels For-Schleife werden die einzelnen Attribute aus einem Tupel gezogen und einer neuen Instanz der
       Klasse "Artikel()" übergeben. Die einzelnen Instanzen werden in einem Array gespeichert.
       Das Array mit allen Instanzen wird schließlich zurückgegeben."""

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM artikel")
        res = cursor.fetchall()

        for (id, name, erstellungs_zeitpunkt, einheit, standardartikel) in res:

            artikel = Artikel()
            artikel.set_id(id)
            artikel.set_name(name)
            artikel.set_standardartikel(standardartikel)
            artikel.set_einheit(einheit)
            artikel.set_erstellungs_zeitpunkt(erstellungs_zeitpunkt)
            result.append(artikel)

        self._cnx.commit()
        cursor.close()

        return result

    """ Mapper-Methode zum speichern eines neuen Artikels in der Datenbank"""

    """ Beim Aufruf der Methode wird eine zuvor erstellte Instanz der Klasse "Artikel()" übergeben.
        Anschließend wird via SQL-Abfrage die höchste ID aus der Tabelle "artikel" ausgegeben und dann
        mit der fetchall-Methode in einem Tupel gespeichert.

        Mit einer for-schleife wird anschließend geschaut ob bereits eine ID in der Tabelle vorhanden ist.
        Falls ja, wird diese genommen und um +1 hochgezählt und anschließend der Instanz, welche in der Datenbank gespeichert
        werden soll übergeben.
        Falls noch keine ID in der Tabelle vorhanden sein sollte, wird die Zahl 1 an die Instanz weitergegeben

        Dann erfolgt erneut ein SQL-Statement welches die Instanz in der Datenbank speichert.
        Mittels der getter-Methoden, welche zuvor in der entsprechenden Business-Object-Klasse definierten wurden, 
        werden die Attribute der Instanz an das SQL-Statement übergeben.
        """

    def insert(self, artikel):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM artikel ")
        ins = cursor.fetchall()

        for (maxid) in ins:
            if maxid[0] is not None:

                artikel.set_id(maxid[0] + 1)
            else:

                artikel.set_id(1)

        template = "INSERT INTO artikel (id, name, erstellungs_zeitpunkt, einheit, standardartikel) VALUES (%s,%s,%s,%s,%s)"
        vals = (artikel.get_id(), artikel.get_name(), artikel.get_erstellungs_zeitpunkt(), artikel.get_einheit(), artikel.get_standardartikel())
        cursor.execute(template, vals)

        self._cnx.commit()
        cursor.close()

        return artikel

    """ Mapper-Methode zum aktualisieren (der Attribute) eines Artikels in der Datenbank"""

    """ Beim Aufruf Methode wird eine zuvor erstellte Instanz der Klasse "Artikel()" übergeben.
        Dann erfolgt ein SQL-Statement welches das Objekt in der Datenbank aktualisiert.
        Mittels der getter-Methoden, welche zuvor in der entsprechenden Business-Object-Klasse definierten wurden, 
        werden die Attribute der Instanz an das SQL-Statement übergeben."""

    def update(self, artikel):

        cursor = self._cnx.cursor()

        template = "UPDATE artikel " + "SET name=%s, einheit=%s, standardartikel=%s WHERE id=%s"
        vals = (artikel.get_name(), artikel.get_einheit(), artikel.get_standardartikel(), artikel.get_id())
        cursor.execute(template, vals)

        self._cnx.commit()
        cursor.close()

    """ Mapper-Methode zum löschen eines Artikels aus der Datenbank"""

    """ Beim Aufruf Methode wird eine zuvor erstellte Instanz der Klasse "Artikel()" übergeben.
        Dann erfolgt ein SQL-Statement welches das Objekt aus der Datenbank löscht.
        Mittels der getter-Methode, welche zuvor in der entsprechenden Business-Object-Klasse definierten wurde, 
        wird die entsprechende ID der Instanz an das SQL-Statement übergeben.."""

    def delete(self, artikel):

        cursor = self._cnx.cursor()

        template = "DELETE FROM artikel WHERE id={}".format(artikel.get_id())
        cursor.execute(template)

        self._cnx.commit()
        cursor.close()

    """ Mapper-Methode zum ausgeben eines Artikels anhand dessen ID"""

    """ Beim Aufruf Methode wird eine ID in der Variablen "id" gespeichert, welche schließlich an das SQL-Statement übergeben wird.
        Das entsprechende Objekt, welches aus der Datenbank ausgegeben wird, wird in einem Tupel gespeichert.
        Anschließend werden die einzelnen Attribute aus dem Tupel an der Stelle 0 genommen und an eine neue Artikel-Instanz via
        den Setter-Methoden übergeben.
        Sollte die Datenbank anhand der ID kein Objekt zurückliefern, wird ausgegeben was innerhalb des IndexErrors steht --> None
        Das Ergebnis wir schließlich von der Mehtode zurückgegeben."""

    def find_by_id(self, id):


        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, erstellungs_zeitpunkt, einheit, standardartikel FROM artikel WHERE id={}".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, name, erstellungs_zeitpunkt, einheit, standardartikel) = tuples[0]
            artikel = Artikel()
            artikel.set_id(id)
            artikel.set_name(name)
            artikel.set_erstellungs_zeitpunkt(erstellungs_zeitpunkt)
            artikel.set_einheit(einheit)
            artikel.set_standardartikel(standardartikel)
            result = artikel
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    """ Mapper-Methode zum ausgeben eines Artikels anhand dessen Name"""

    """ Beim Aufruf Methode wird ein Name in der Variablen "name" gespeichert, welche schließlich an das SQL-Statement übergeben wird.
        Das entsprechende Objekt, welches aus der Datenbank ausgegeben wird, wird in einem Tupel gespeichert.
        Anschließend werden die einzelnen Attribute aus dem Tupel an der Stelle 0 genommen und an eine neue Artikel-Instanz via
        den Setter-Methoden übergeben.
        Sollte die Datenbank anhand des Namens kein Objekt zurückliefern, wird ausgegeben was innerhalb des IndexErrors steht --> None
        Das Ergebnis wir schließlich von der Mehtode zurückgegeben.
        """

    def find_by_name(self, name):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, erstellungs_zeitpunkt, einheit, standardartikel FROM artikel WHERE name LIKE '{}' ORDER BY name".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, name, erstellungs_zeitpunkt, einheit, standardartikel) = tuples[0]
            artikel = Artikel()
            artikel.set_id(id)
            artikel.set_name(name)
            artikel.set_erstellungs_zeitpunkt(erstellungs_zeitpunkt)
            artikel.set_einheit(einheit)
            artikel.set_standardartikel(standardartikel)
            result = artikel
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result











