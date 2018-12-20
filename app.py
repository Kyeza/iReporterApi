from flask import Flask, jsonify

from models.entities import Incident

app = Flask(__name__)

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
for x in range(3):
	x = Incident(**data)
	db.append(x.incident)

@app.route('/ireporter.com/api/v1/red-flags', methods=['GET'])
def get_red_flags():
	result = {'status': 200, 'data': db}
	return jsonify(result), 200

@app.route('/ireporter.com/api/v1/red-flags/<int:incident_id>', methods=['GET'])
def get_red_flag(incident_id):
	pass



if __name__ == '__main__':
    app.run(debug=True)
