from flask import Flask, jsonify

from models.entities import Incident

app = Flask(__name__)

@app.route('/ireporter.com/api/v1/resources/red-flags')
def get_red_flags():
	data = {
	  	'createdOn' : 'Date',  
	  	'createdBy' : 'Integer', 
	  	'type' : 'String',       
	  	'location' : 'String',   
	  	'status' : 'String',     
	  	'Images' : ['Image', 'Image'], 
	  	'Videos' : ['Image', 'Image'],
	  	'comment' : 'String'
	}

	db = []
	for x in range(10):
		x = Incident(**data)
		db.append(x.incident)
	result = {'status': 200, 'data': db}
	return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=True)
