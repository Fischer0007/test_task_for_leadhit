
from app import app, models
from flask import request, jsonify
from tinydb import TinyDB


db = TinyDB('db/db.json')


@app.route('/get_form/', methods=['POST'])
def get_form():
    template = db.table(name="_templates").all()[0]
    list_template = list(template.values())
    form = jsonify(request.values).get_json()
    list_of_types = list_template + list(models.MyModel.parse_obj(form).dict().values())
    print(form)
    if "FIELD_TYPE" in list_of_types:
        response = dict(zip(list(models.MyModel.parse_obj(form).dict().keys()),
                            models.MyModel.parse_obj(form).dict().values())
                        )
        res = {k: v for k, v in response.items() if v is not None}
        response.clear()
        response.update(res)
        return response

    else:
        visited = set()
        list_of_types[:] = [x for x in list_of_types if x not in visited and x != None and not visited.add(x)]
        if list_template == list_of_types:
            return list_of_types[0]


@app.errorhandler(500)
def handle_500(error):
    return str(error), 500

