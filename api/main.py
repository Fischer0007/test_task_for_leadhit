

from flask import Flask, request, jsonify
from flask_restful import Api
from tinydb import TinyDB
from api.models import *


app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('config.cfg')
db = TinyDB('../db/db.json')


@app.route('/get_form/', methods=['POST'])
def get_form():
    template = db.table(name="_templates").all()[0]
    list_template = list(template.values())
    form = jsonify(request.values).get_json()
    list_of_types = list_template + list(MyModel.parse_obj(form).dict().values())
    if "FIELD_TYPE" not in list_of_types:
        visited = set()
        list_of_types[:] = [x for x in list_of_types if x not in visited and x != None and not visited.add(x)]
        if list_template == list_of_types:
            return list_of_types[0]
    else:
        response = dict(zip(list(MyModel.parse_obj(form).dict().keys()), MyModel.parse_obj(form).dict().values()))
        res = {k: v for k, v in response.items() if v is not None}
        response.clear()
        response.update(res)
        return response


@app.errorhandler(500)
def handle_500(error):
    return str(error), 500


if __name__ == '__main__':
    app.run()
