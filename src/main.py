from flask import Flask
from flask_cors import CORS
from flask_restx import Resource, Api, fields

from src.server.ApplikationsAdministration import ApplikationsAdministration
from src.server.bo.Artikel import Artikel



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

artikel = api.inherit('Artikel',namedBO , {
    'einheit': fields.String(attribute='_einheit', description='Name eines Artikels'),
    'standardartikel': fields.String(attribute='_standardartikel', description='Standardartikel'),
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
    def post(self, id):
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
    def get_by_id(self, id):
        """Auslesen eines bestimmten Artikel"""
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
     
        adm = ApplikationsAdministration()
        a = Artikel.from_dict(api.payload)

        if a is not None:
            a.set_id(id)
            adm.update_artikel(artikel)
            return '', 200
        else:
            return '', 500

@shopping.route('/artikel-by-name/<string:name>')
@shopping.response(500, "Serverfehler")
@shopping.param('name', 'Name des Artikels')
class ArtikelByNameOperations(Resource):
    @shopping.marshal_with(artikel)
    #@secured
    def get_by_name(self,name):
        
        adm = ApplikationsAdministration()
        artikel = adm.get_artikel_by_name(name)
        return artikel



if __name__ == '__main__':
    app.run(debug=True)



