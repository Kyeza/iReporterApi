from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/ireporter.com/api/v1/resources/red-flags')
def hello_world():
	result = {'status': 200, 'message': 'Hello World!'}
	return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=True)
