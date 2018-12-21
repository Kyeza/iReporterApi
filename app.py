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
    result = {
        'status': 200, 
        'data': db
    }
    return jsonify(result), 200


@app.errorhandler(InvalidApiUsage)
@app.route('/ireporter.com/api/v1/red-flags', methods=['POST'])
def create_red_flags():
    if not request.json or not 'type' in request.json:
        raise InvalidApiUsage('Not a valid red-flag')

    obj = Incident(**request.json).to_dict
    db.append(obj)
    result = {
        'status': 201, 
        'data': [{'id': obj['id'], 'message': 'Created red-flag record'}]
    }
    return jsonify(result), 201


@app.errorhandler(InvalidApiUsage)
@app.route('/ireporter.com/api/v1/red-flags/<int:incident_id>', methods=['GET'])
def get_red_flag(incident_id):
    red_flag = [red_flag for red_flag in db if red_flag['id'] == incident_id]
    if len(red_flag) == 0:
        raise InvalidApiUsage(f"resource not found, red-flag with id={incident_id} doesn't exist",
         status_code=404)
    result = {
        'status': 200, 
        'data': red_flag
    }
    return jsonify(result), 200


@app.errorhandler(InvalidApiUsage)
@app.route('/ireporter.com/api/v1/red-flags/<int:incident_id>', methods=['PATCH'])
def update_red_flag(incident_id):
    red_flag = [red_flag for red_flag in db if red_flag['id'] == incident_id]

    if len(red_flag) == 0:
        raise InvalidApiUsage(f"resource not found, red-flag with id={incident_id} doesn't exist",
         status_code=404)
    if not request.json:
        raise InvalidApiUsage('bad request, not a valid red-flag')
    if 'comment' in request.json:
        red_flag[0]['comment'] = request.json.get('comment', red_flag[0]['comment'])
        red_flag_obj = red_flag[0]
        result = {
            'status': 200, 
            'data': [{'id': red_flag_obj['id'], 'message': 'Updated red-flag record’s comment'}]
        }
        return jsonify(result)
    elif 'location' in request.json :
        red_flag[0]['location'] = request.json.get('location', red_flag[0]['location'])
        red_flag_obj = red_flag[0]
        result = {
            'status': 200, 
            'data': [{'id': red_flag_obj['id'], 'message': 'Updated red-flag record’s location'}]
        }
        return jsonify(result)
    else:
        raise InvalidApiUsage('bad request, must pass a comment/location')


@app.errorhandler(InvalidApiUsage)
@app.route('/ireporter.com/api/v1/red-flags/<int:incident_id>', methods=['DELETE'])
def delete_red_flag(incident_id):
    red_flag = [red_flag for red_flag in db if red_flag['id'] == incident_id]

    if len(red_flag) == 0:
        raise InvalidApiUsage(f"resource not found, red-flag with id={incident_id} doesn't doesn't exist",
         status_code=404)
    db.remove(red_flag[0])
    result = {
        'status': 200,
        'data': [{'id': incident_id, 'message': 'red-flag record has been deleted'}]
    }
    return jsonify(result)


@app.errorhandler(InvalidApiUsage)
def handle_invalid_usage(error):
    result = jsonify(error.to_dict())
    result.status_code = error.status_code
    return result


if __name__ == '__main__':
    app.run(debug=True)
