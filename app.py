"""docstring for my api module"""
from flask import Flask, jsonify, request

from models.entities import Incident
from handler.error import InvalidApiUsage

APP = Flask(__name__)
DATABASE = []


@APP.route('/ireporter.com/api/v1/red-flags', methods=['GET'])
def get_all_red_flags():
    """get all red-flags"""
    result = {
        'status': 200, 'data': DATABASE
    }
    return jsonify(result), 200


@APP.errorhandler(InvalidApiUsage)
@APP.route('/ireporter.com/api/v1/red-flags', methods=['POST'])
def create_red_flag():
    """create a red-flag"""
    if not request.json or 'type' not in request.json:
        raise InvalidApiUsage('Not a valid red-flag')

    obj = Incident(**request.json).to_dict
    DATABASE.append(obj)
    result = {
        'status': 201, 'data': [{'id': obj['id'], 'message': 'Created red-flag record'}]
    }
    return jsonify(result), 201


@APP.errorhandler(InvalidApiUsage)
@APP.route('/ireporter.com/api/v1/red-flags/<int:incident_id>', methods=['GET'])
def get_a_red_flag(incident_id):
    """get a specific red-flag using its id"""
    red_flag = [red_flag for red_flag in DATABASE if red_flag['id'] == incident_id]
    if not red_flag:
        raise InvalidApiUsage(f"resource not found, red-flag with id={incident_id} doesn't exist",
                              status_code=404)
    result = {
        'status': 200,
        'data': red_flag
    }
    return jsonify(result), 200


@APP.errorhandler(InvalidApiUsage)
@APP.route('/ireporter.com/api/v1/red-flags/<int:incident_id>', methods=['PATCH'])
def update_red_flag(incident_id):
    """update location or comment of a specific red-flag using its id"""
    red_flag = [red_flag for red_flag in DATABASE if red_flag['id'] == incident_id]
    result = {}

    if not red_flag:
        raise InvalidApiUsage(f"resource not found, red-flag with id={incident_id} doesn't exist",
                              status_code=404)
    if not request.json:
        raise InvalidApiUsage('bad request, not a valid red-flag')
    if 'location' not in request.json and 'comment' not in request.json:
        raise InvalidApiUsage('bad request, must pass a comment/location')
    if 'comment' in request.json:
        red_flag[0]['comment'] = request.json.get('comment', red_flag[0]['comment'])
        red_flag_obj = red_flag[0]
        result['status'] = 200
        result['data'] = [
            {'id': red_flag_obj['id'], 'message': "Updated red-flag record’s comment"}
        ]
    if 'location' in request.json:
        red_flag[0]['location'] = request.json.get('location', red_flag[0]['location'])
        red_flag_obj = red_flag[0]
        result['status'] = 200
        result['data'] = [
            {'id': red_flag_obj['id'], 'message': "Updated red-flag record’s location"}
        ]

    return jsonify(result)


@APP.errorhandler(InvalidApiUsage)
@APP.route('/ireporter.com/api/v1/red-flags/<int:incident_id>', methods=['DELETE'])
def delete_red_flag(incident_id):
    """delete a red-flag"""
    red_flag = [red_flag for red_flag in DATABASE if red_flag['id'] == incident_id]

    if not red_flag:
        raise InvalidApiUsage(f"resource not found, red-flag with id={incident_id} doesn't exist",
                              status_code=404)
    DATABASE.remove(red_flag[0])
    result = {
        'status': 200,
        'data': [{'id': incident_id, 'message': 'red-flag record has been deleted'}]
    }
    return jsonify(result)


@APP.errorhandler(InvalidApiUsage)
def handle_invalid_usage(error):
    """handle errors for invalid api usage"""
    result = jsonify(error.to_dict())
    result.status_code = error.status_code
    return result


if __name__ == '__main__':
    APP.run(debug=True)
