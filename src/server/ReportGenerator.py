from server.bo.Statistik import Statistik
from server.bo.StatistikHaendler import StatistikHaendler
from server.bo.StatistikZeitraum import StatistikZeitraum
from server.bo.StatistikHuZ import StatistikHuZ
from server.db.ListeneintragMapper import ListeneintragMapper
import collections


class ReportGenerator(object):

    def top_artikel(self, benutzer):
        """ Methode um alle Artikel zu einem bestimmten Benutzer heraus zubekommen und dann nach den 5 Artikeln die die
        größte Anzahl haben schauen und diese zurückgeben"""
        artikel = []
        instanzen = []
        x = 0
        with ListeneintragMapper() as mapper:
            tupel = mapper.get_all_listeneintraege_by_benutzer(benutzer)

            for i in tupel:
                for k in i:
                    artikel.append(k)

        a = collections.Counter(artikel)

        for i in a:
            instanz = Statistik()
            instanz.set_ArtikelID(i)
            instanz.set_anzahl(a.get(i))
            instanzen.append(instanz)

        result = []

        for i in range(len(instanzen)):
            if x < 5:
                highest = instanzen[0]
                for obj in instanzen:
                    if obj.get_anzahl() > highest.get_anzahl():
                        highest = obj

                result.append(highest)
                instanzen.remove(highest)
                x += 1
        return result

    def top_artikel_by_einzelhaendler(self, benutzer, einzelhaendler):
        """ Methode um alle Artikel zu einem bestimmten Benutzer und einem bestimmten Einzelhaendler heraus zubekommen
        und dann nach den 5 Artikeln die die größte Anzahl haben schauen und diese zurückgeben """
        artikel = []
        instanzen = []
        x = 0
        with ListeneintragMapper() as mapper:
            tupel = mapper.get_all_listeneintraege_by_Einzelhaendler(benutzer, einzelhaendler)

            for i in tupel:
                for k in i:
                    artikel.append(k)

        a = collections.Counter(artikel)

        for i in a:
            instanz = StatistikHaendler()
            instanz.set_ArtikelID(i)
            instanz.set_anzahl(a.get(i))
            instanzen.append(instanz)

        result = []

        for i in range(len(instanzen)):
            if x < 5:
                highest = instanzen[0]
                for obj in instanzen:
                    if obj.get_anzahl() > highest.get_anzahl():
                        highest = obj

                result.append(highest)
                instanzen.remove(highest)
                x += 1
        return result

    def top_artikel_by_zeitraum(self, benutzer, startzeitpunkt, endzeitpunkt):
        """ Methode um alle Artikel zu einem bestimmten Benutzer heraus zubekommen, welche in dem angegebenen Zeitraum
        liegen und dann nach den 5 Artikeln die die größte Anzahl haben schauen und diese zurückgeben"""
        instanzen = []
        alle = []
        result = []
        x = 0

        with ListeneintragMapper() as mapper:
            tupel = mapper.get_all_listeneintraege_by_Datum(benutzer)

        for i in tupel:
            zeitpunkt = i.get_zeitpunkt()
            zeitpunkt = zeitpunkt.strftime("%Y-%m-%d")
            if startzeitpunkt <= zeitpunkt <= endzeitpunkt:
                alle.append(i.get_ArtikelID())

        a = collections.Counter(alle)

        for i in a:
            instanz = StatistikZeitraum()
            instanz.set_ArtikelID(i)
            instanz.set_anzahl(a.get(i))
            instanzen.append(instanz)

        for i in range(len(instanzen)):
            if x < 5:
                highest = instanzen[0]
                for obj in instanzen:
                    if obj.get_anzahl() > highest.get_anzahl():
                        highest = obj

                result.append(highest)
                instanzen.remove(highest)
                x += 1
        return result

    def top_artikel_by_Einzelhaendler_zeitraum(self, benutzer, einzelhaendler, startzeitpunkt, endzeitpunkt):
        """ Methode um alle Artikel zu einem bestimmten Benutzer und einem bestimmten Einzelhaendler heraus zubekommen,
        welche in dem angegebenen Zeitraum liegen und dann nach den 5 Artikeln die die größte Anzahl haben schauen
        und diese zurückgeben"""
        instanzen = []
        alle = []
        result = []
        x = 0

        with ListeneintragMapper() as mapper:
            tupel = mapper.get_all_listeneintraege_by_Einzelhaendler_Datum(benutzer, einzelhaendler)

        for i in tupel:
            zeitpunkt = i.get_zeitpunkt()
            zeitpunkt = zeitpunkt.strftime("%Y-%m-%d")
            if startzeitpunkt <= zeitpunkt <= endzeitpunkt:
                alle.append(i.get_ArtikelID())

        a = collections.Counter(alle)

        for i in a:
            instanz = StatistikHuZ()
            instanz.set_ArtikelID(i)
            instanz.set_anzahl(a.get(i))
            instanzen.append(instanz)

        for i in range(len(instanzen)):
            if x < 5:
                highest = instanzen[0]
                for obj in instanzen:
                    if obj.get_anzahl() > highest.get_anzahl():
                        highest = obj

                result.append(highest)
                instanzen.remove(highest)
                x += 1
        return result
