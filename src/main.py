from flask import Flask
from flask_cors import CORS
from flask_restx import Resource, Api, fields

from src.server.ApplikationsAdministration import ApplikationsAdministration
from src.server.bo.Artikel import Artikel
from src.server.bo.Einzelhaendler import Einzelhaendler
from src.server.bo.Benutzer import Benutzer
from src.server.bo.Einkaufsliste import Einkaufsliste
from src.server.bo.Anwenderverbund import Anwenderverbund



from src.SecurityDecorator import secured

"""requirements: Flask, Flask-Cors, flask-restx, mysql-connector-python"""

app = Flask(__name__)


CORS(app)                  # als zweiter parameter könnte man auch noch folgendes hinzufügen:
                           # , resources=r'/shopping/*'      oder    , resources={r"/shopping/*": {"origins": "*"}}

api = Api(app, version='1.0', title='ShoppingList API',
    description='Das ist unserer API für die Shoppinglist.')

shopping = api.namespace('shopping', description='Funktionen der Shoppinglist')

bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Der Unique Identifier eines Business Object'),
})

namedBO = api.inherit('namedBO', bo, {
    'name': fields.String(attribute='_name', description='Name des namedBO'),
    'erstellungs_zeitpunkt': fields.String(attribute='_erstellungs_zeitpunkt', description='Erstellungszeitpunkt'),
})

artikel = api.inherit('Artikel',namedBO, {
    'einheit': fields.String(attribute='_einheit', description='Name eines Artikels'),
    'standardartikel': fields.Boolean(attribute='_standardartikel', description='Standardartikel'),
})

einzelhaendler = api.inherit('Einzelhandler', namedBO, bo)

benutzer = api.inherit('Benutzer', namedBO, {
    'email': fields.String(attribute='_email', description='Email des Benutzers'),
    'google_id': fields.Integer(attribute='_google_id', description='Google ID des Benutzers')
})

einkaufsliste = api.inherit('Einkaufsliste', namedBO, {
    'änderungs_zeitpunkt': fields.String(attribute='_änderungs_zeitpunkt', description='Änderungszeitpunkt'),
    'anwenderverbund_id': fields.Integer(attribute='_anwenderverbund_id', description='ID des Anwenderverbundes')
})

anwenderverbund = api.inherit('Anwenderverbund', namedBO, {
    'einkaufslisten': fields.String(attribute='_einkaufslisten', description='Einkaufslisten im Anwenderverbund')
})



@shopping.route('/artikel')
@shopping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class ArtikelListOperations(Resource):
    @shopping.marshal_list_with(artikel)
    #@secured
    def get(self):
        """Auslesen aller Artikel"""
        adm = ApplikationsAdministration()
        artikel = adm.get_all_artikel()
        return artikel

    @shopping.marshal_with(artikel)
    @shopping.expect(artikel)
    #@secured
    def post(self):
        """Anlegen eines Artikels"""
        adm = ApplikationsAdministration()

        test = Artikel.from_dict(api.payload)
        if test is not None:
            a = adm.artikel_anlegen(test.get_name(), test.get_einheit(), test.get_standardartikel())
            return a, 200
        else:
            return '', 500



@shopping.route('/artikel-by-id/<int:id>')
@shopping.response(500, 'Serverfehler')
@shopping.param('id', 'ID des Artikels')
class ArtikelOperations(Resource):
    @shopping.marshal_with(artikel)
    #@secured
    def get(self, id):
        """Auslesen eines bestimmten Artikel anhand einer id"""
        adm = ApplikationsAdministration()
        artikel = adm.get_artikel_by_id(id)
        return artikel

    #@secured
    def delete(self, id):
        """Löschen eines Artikels anhand einer id"""
        adm = ApplikationsAdministration()
        artikel = adm.get_artikel_by_id(id)
        adm.delete_artikel(artikel)
        return ''

    @shopping.marshal_with(artikel)
    @shopping.expect(artikel)
    #@secured
    def put(self, id):
        """Update eines durch eine id bestimmten Artikel"""
     
        adm = ApplikationsAdministration()
        a = Artikel.from_dict(api.payload)

        if a is not None:
            a.set_id(id)
            adm.update_artikel(a)
            return '', 200
        else:
            return '', 500

@shopping.route('/artikel-by-name/<string:name>')
@shopping.response(500, 'Serverfehler')
@shopping.param('name', 'Name des Artikels')
class ArtikelByNameOperations(Resource):
    @shopping.marshal_with(artikel)
    #@secured
    def get(self, name):
        """Auslesen eines bestimmten Artikel anhand dessen Namen"""
        adm = ApplikationsAdministration()
        artikel = adm.get_artikel_by_name(name)
        return artikel

"""Artikel DONE. Einzelhändler NEXT"""


@shopping.route('/einzelhaendler')
@shopping.response(500, 'Serverfehler')
class EinzelhaendlerListOperations(Resource):
    @shopping.marshal_list_with(einzelhaendler)
    #@secured
    def get(self):
        """Auslesen aller Einzelhändler"""
        adm = ApplikationsAdministration()
        einzelhaendler = adm.get_all_einzelhaendler()
        return einzelhaendler

    @shopping.marshal_with(einzelhaendler)
    @shopping.expect(einzelhaendler)
    #@secured
    def post(self):
        """Anlegen eines Einzelhändlers"""
        adm = ApplikationsAdministration()

        test = Einzelhaendler.from_dict(api.payload)
        if test is not None:
            a = adm.einzelhaendler_anlegen(test.get_name(), test.get_id())
            return a, 200
        else:
            return '', 500



@shopping.route('/einzelhaendler-by-id/<int:id>')
@shopping.response(500, 'Serverfehler')
@shopping.param('id', 'ID des Einzelhaendler')
class EinzelhaendlerOperations(Resource):
    @shopping.marshal_with(einzelhaendler)
    #@secured
    def get(self, id):
        """Auslesen eines bestimmten Einzelhändlers anhand einer id"""
        adm = ApplikationsAdministration()
        einzelhaendler = adm.get_einzelhaendler_by_id(id)
        return einzelhaendler

    #@secured
    def delete(self, id):
        """Löschen eines Einzelhändlers anhand einer id"""
        adm = ApplikationsAdministration()
        einzelhaendler = adm.get_einzelhaendler_by_id(id)
        adm.delete_einzelhaendler(einzelhaendler)
        return ''

    @shopping.marshal_with(einzelhaendler)
    @shopping.expect(einzelhaendler)
    #@secured
    def put(self, id):
        """Update eines durch eine id bestimmten Einzelhändlers"""

        adm = ApplikationsAdministration()
        a = Einzelhaendler.from_dict(api.payload)

        if a is not None:
            a.set_id(id)
            adm.update_einzelhaendler(a)
            return '', 200
        else:
            return '', 500

@shopping.route('/einzelhaendler-by-name/<string:name>')
@shopping.response(500, 'Serverfehler')
@shopping.param('name', 'Name des Einzelhändler')
class ArtikelByNameOperations(Resource):
    @shopping.marshal_with(einzelhaendler)
    #@secured
    def get(self, name):
        """Auslesen eines bestimmten Einzelhändlers anhand dessen Namen"""
        adm = ApplikationsAdministration()
        einzelhaendler = adm.get_einzelhaendler_by_name(name)
        return einzelhaendler

"""Einzelhändler DONE -> keine Error. Benutzer NEXT. """

@shopping.route('/benutzer')
@shopping.response(500, 'Serverfehler')
class BenutzerListOperations(Resource):
    @shopping.marshal_list_with(benutzer)
    #@secured
    def get(self):
        """Auslesen aller Benutzer"""
        adm = ApplikationsAdministration()
        benutzer = adm.get_all_artikel()
        return benutzer

    @shopping.marshal_with(benutzer)
    @shopping.expect(benutzer)
    #@secured
    def post(self):
        """Anlegen eines Benutzers"""
        adm = ApplikationsAdministration()

        test = Benutzer.from_dict(api.payload)
        if test is not None:
            a = adm.benutzer_anlegen(test.get_name(), test.get_email(), test.get_google_id())
            return a, 200
        else:
            return '', 500



@shopping.route('/benutzer-by-id/<int:id>')
@shopping.response(500, 'Serverfehler')
@shopping.param('id', 'ID des Benutzers')
class BenutzerOperations(Resource):
    @shopping.marshal_with(benutzer)
    #@secured
    def get(self, id):
        """Auslesen eines bestimmten Benutzers anhand einer id"""
        adm = ApplikationsAdministration()
        benutzer = adm.get_benutzer_by_id(id)
        return benutzer

    #@secured
    def delete(self, id):
        """Löschen eines Benutzers anhand einer id"""
        adm = ApplikationsAdministration()
        benutzer = adm.get_benutzer_by_id(id)
        adm.delete_benutzer(benutzer)
        return ''

    @shopping.marshal_with(benutzer)
    @shopping.expect(benutzer)
    #@secured
    def put(self, id):
        """Update eines durch eine id bestimmten Benutzer"""

        adm = ApplikationsAdministration()
        a = Benutzer.from_dict(api.payload)

        if a is not None:
            a.set_id(id)
            adm.update_benutzer(a)
            return '', 200
        else:
            return '', 500

@shopping.route('/benutzer-by-name/<string:name>')
@shopping.response(500, 'Serverfehler')
@shopping.param('name', 'Name des Benutzers')
class BenutzerByNameOperations(Resource):
    @shopping.marshal_with(benutzer)
    #@secured
    def get(self, name):
        """Auslesen eines bestimmten Benutzers anhand seines Namen"""
        adm = ApplikationsAdministration()
        benutzer = adm.get_benutzer_by_name(name)
        return benutzer


"""Benutzer DONE. Einkaufsliste NEXT"""



@shopping.route('/einkaufsliste')
@shopping.response(500, 'Serverfehler')
class EinkaufslisteListOperations(Resource):
    @shopping.marshal_list_with(einkaufsliste)
    #@secured
    def get(self):                                          #evtl. unnötig bzw. muss mit anwenderverbund definiert werden
        """Auslesen aller Einkaufslisten"""
        adm = ApplikationsAdministration()
        einkaufsliste = adm.get_all_einkaufslisten(anwenderverbund)
        return einkaufsliste

    @shopping.marshal_with(einkaufsliste)
    @shopping.expect(einkaufsliste)
    #@secured
    def post(self):                                         #Anwenderverbund muss definiert sein
        """Anlegen einer Einkaufsliste"""
        adm = ApplikationsAdministration()

        test = Einkaufsliste.from_dict(api.payload)
        if test is not None:
            a = adm.einkaufsliste_anlegen(test.get_name(), test.get_anwenderId())
            return a, 200
        else:
            return '', 500



@shopping.route('/einkaufsliste-by-id/<int:id>')
@shopping.response(500, 'Serverfehler')
@shopping.param('id', 'ID der Einkaufsliste')
class EinkaufslisteOperations(Resource):                                    #id von Einkaufsliste muss mit id von Anwenderverbund angegeben werden
    @shopping.marshal_with(einkaufsliste)
    #@secured
    def get(self, id):
        """Auslesen einer bestimmten Einkaufsliste anhand einer id"""
        adm = ApplikationsAdministration()
        einkaufsliste = adm.get_einkaufsliste_by_id(id)
        return einkaufsliste

    #@secured
    def delete(self, id):
        """Löschen einer Einkaufsliste anhand einer id"""
        adm = ApplikationsAdministration()
        einkaufsliste = adm.get_einkaufsliste_by_id(id)
        adm.delete_einkaufsliste(einkaufsliste)
        return ''

    @shopping.marshal_with(einkaufsliste)
    @shopping.expect(einkaufsliste)
    #@secured
    def put(self, id):
        """Update einer durch id bestimmten Einkaufsliste"""

        adm = ApplikationsAdministration()
        a = Einkaufsliste.from_dict(api.payload)

        if a is not None:
            a.set_id(id)
            adm.update_einkaufsliste(a)
            return '', 200
        else:
            return '', 500

@shopping.route('/einkaufsliste-by-name/<string:name>')
@shopping.response(500, 'Serverfehler')
@shopping.param('name', 'Name der Einkaufsliste')
class EinkaufslisteByNameOperations(Resource):                                  #name evtl. nicht eindeutig
    @shopping.marshal_with(einkaufsliste)
    #@secured
    def get(self, name):
        """Auslesen einer bestimmten Einkaufsliste anhand dessen Namen"""
        adm = ApplikationsAdministration()
        einkaufsliste = adm.get_einkaufsliste_by_name(name)
        return einkaufsliste


"""Einkaufsliste DONE. Anwenderverbund NEXT"""


@shopping.route('/anwenderverbund')
@shopping.response(500, 'Serverfehler')
class AnwenderverbundListOperations(Resource):
    @shopping.marshal_list_with(anwenderverbund)
    #@secured
    def get(self):
        """Auslesen aller Anwenderverbünde"""
        adm = ApplikationsAdministration()
        anwenderverbund = adm.get_all_anwenderverbunde()
        return anwenderverbund

    @shopping.marshal_with(anwenderverbund)
    @shopping.expect(anwenderverbund)
    #@secured
    def post(self):
        """Anlegen eines Anwenderverbundes"""
        adm = ApplikationsAdministration()

        test = Anwenderverbund.from_dict(api.payload)
        if test is not None:
            a = adm.anwenderverbund_anlegen(test.get_name())
            return a, 200
        else:
            return '', 500



@shopping.route('/anwenderverbund-by-id/<int:id>')
@shopping.response(500, 'Serverfehler')
@shopping.param('id', 'ID des Anwenderverbundes')
class AnwenderverbundOperations(Resource):
    @shopping.marshal_with(anwenderverbund)
    #@secured
    def get(self, id):
        """Auslesen eines bestimmten Anwenderverbundes anhand einer id"""
        adm = ApplikationsAdministration()
        anwenderverbund = adm.get_anwenderverbund_by_id(id)
        return anwenderverbund

    #@secured
    def delete(self, id):
        """Löschen eines Anwenderverbundes anhand einer id"""
        adm = ApplikationsAdministration()
        anwenderverbund = adm.get_anwenderverbund_by_id(id)
        adm.delete_anwenderverbund(anwenderverbund)
        return ''

    @shopping.marshal_with(anwenderverbund)
    @shopping.expect(anwenderverbund)
    #@secured
    def put(self, id):
        """Update eines durch eine id bestimmten Anwenderverbundes"""

        adm = ApplikationsAdministration()
        a = Anwenderverbund.from_dict(api.payload)

        if a is not None:
            a.set_id(id)
            adm.update_anwenderverbund(a)
            return '', 200
        else:
            return '', 500

@shopping.route('/anwenderverbund-by-name/<string:name>')
@shopping.response(500, 'Serverfehler')
@shopping.param('name', 'Name des Anwenderverbundes')
class AnwenderverbundByNameOperations(Resource):
    @shopping.marshal_with(anwenderverbund)
    #@secured
    def get(self, name):
        """Auslesen eines bestimmten Anwenderverbundes anhand dessen Namen"""
        adm = ApplikationsAdministration()
        anwenderverbund = adm.get_anwenderverbund_by_name(name)
        return anwenderverbund

@shopping.route('/anwenderverbund/<int:id>/einkauflisten')
@shopping.response(500, 'Serverfehler')
@shopping.param('id', 'ID des Anwenderverbundes')
class AnwenderverbundRelatedEinkaufslisteOperations(Resource):
    @shopping.marshal_with(einkaufsliste)
    #@secured
    def get(self, id):
        """Auslesen aller Einkaufslisten in einem durch Id definierten Anwenderverbund"""
        adm = ApplikationsAdministration()
        verbund = adm.get_anwenderverbund_by_id(id)

        if verbund is not None:
            einkaufslisten = adm.get_all_einkaufslisten(verbund)
            return einkaufslisten
        else:
            return "Einkaufsliste nicht gefunden", 500


"""Anwenderverbund DONE. Listeneintrag NEXT"""



if __name__ == '__main__':
    app.run(debug=True)



