from flask import Flask, jsonify, request, make_response

from models.entities import Incident
from errors.errors import InvalidApiUsage

app = Flask(__name__)

data = {
    'createdOn': 'Date',
    'createdBy': 'Integer',
    'type': 'String',
    'location': 'String',
    'status': 'String',
    'Images': ['Image', 'Image'],
    'Videos': ['Image', 'Image'],
    'comment': 'String'
}

db = []
for x in range(3):
    x = Incident(**data)
    db.append(x.to_dict)


@app.route('/ireporter.com/api/v1/red-flags', methods=['GET'])
def get_red_flags():
    result = {'status': 200, 'data': db}
    return jsonify(result), 200


@app.route('/ireporter.com/api/v1/red-flags', methods=['POST'])
def create_red_flags():
    if not request.json or not 'type' in request.json:
        try:
            raise InvalidApiUsage('Not a valid red-flag')
        except InvalidApiUsage as e:
            print(e.to_dict())
            return jsonify(e.to_dict())

    obj = Incident(**request.json)
    db.append(obj.to_dict)
    result = {'status': 201, 'data': obj.to_dict}
    return jsonify(result), 201


if __name__ == '__main__':
    app.run(debug=True)
