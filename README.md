[![Build Status](https://travis-ci.com/Kyeza/iReporterApi.svg?branch=master)](https://travis-ci.com/Kyeza/iReporterApi) [![Coverage Status](https://coveralls.io/repos/github/Kyeza/iReporterApi/badge.svg?branch=develop)](https://coveralls.io/github/Kyeza/iReporterApi?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/7a775bc8e1d7039f4171/maintainability)](https://codeclimate.com/github/Kyeza/iReporterApi/maintainability)

# Introduction
The Api creates, deletes, edits and returns red-flag incidents

# Overview
The api app instance creates three red-flag records when started and more records created after that their primary keys auto increment from 3(inclusive) onwards.

- An Enitity of an incident/red-flag :
  * {
    “id” : Integer,
    “createdOn” : Date,  
    “createdBy” : Integer, // represents the user who created this record
    “type” : String,       // [red-flag, intervention]
    “location” : String,   // Lat Long coordinates
    “status” : String,     // [draft, under investigation, resolved, rejected]
    “Images” : [Image, Image], 
    “Videos” : [Image, Image],
    “comment” : String
     ...
  }

- Pass "ids" to resources to affect a specific record for example :
	* Fetch a specific red-flag record : /ireporter.com/api/v1/red-flags/1
	
- When updating a comment/location of a specific record pass an id and a body of a json object containing the key value pair of either a comment/location. Any other values will be ignore or result in a Bad request 400

# Authentication
No authentication required

# Error Codes
- 404: resource not found, red-flag with id={incident_id} doesn't exist
- 400: bad request, not a valid red-flag
- 400: bad request, must pass a comment
- 400: bad request, must pass location

# Rate limit
no limit

# Usage
# GET /ireporter.com/api/v1/red-flags
  - Get all red-flag records
  
  - http://localhost:5000/ireporter.com/api/v1/red-flags
  
  # # Example request (Python)
    import requests
    url = '/ireporter.com/api/v1/red-flags'
    payload = {}
    headers = {}
    response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
    print(response.text)
    
  # # # Example response
    {
      “status” : 200, 
      “data” : [{...}, {...}, {...}]
    }
    
# POST /ireporter.com/api/v1/red-flags
  - Create a red-flag record
  
  - Headers:
    * Content-Type	application/json
    
  - Body raw (application/json):
    * {"createdBy": 0, "type": "red-flag", "location": "Andela", "status": "draft", "Images": ["image_1.jpg", "image_2.png"], "Videos": ["video_1.mp4", "video_2.mp4"], "comment": "This is a sample comment"}
  
  - http://localhost:5000/ireporter.com/api/v1/red-flags
  
  # # Example request (Python)
    import requests
    url = '/ireporter.com/api/v1/red-flags'
    payload = "{\"createdOn\": \"Date\", \"createdBy\": 0, \"type\": \"red-flag\", \"location\": \"Andela\", \"status\": \"draft\", \"Images\": [\"image_1.jpg\", \"image_2.png\"], \"Videos\": [\"video_1.mp4\", \"video_2.mp4\"], \"comment\": \"This is a sample comment\"}"
    headers = {}
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
    print(response.text)
    
  # # # Example response
    {
      “status” : 201, 
      “data” : [{
        “id” : Integer,    // red flag record primary key
        “message” :  “Created red-flag record”
      }]
    }
    
# GET /ireporter.com/api/v1/red-flags/<int:incident_id>
  - Get a specific red-flag record with a specific id
  
  - http://localhost:5000/ireporter.com/api/v1/red-flags/2
  
  # # Example request (Python)
    import requests
    url = '/ireporter.com/api/v1/red-flags/<int:incident_id>'
    payload = {}
    headers = {}
    response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
    print(response.text)
    
  # # # Example response
    {
      “status” : 200, 
      “data” : [{...}]
    }
    
# PATCH /ireporter.com/api/v1/red-flags/<int:incident_id>
  - Edit a comment of a red-flag record with a specific id
  
  - Headers:
    * Content-Type	application/json
    
  - Body raw (application/json):
    * {"comment": "This is a new sample comment"}
  
  - http://localhost:5000/ireporter.com/api/v1/red-flags/2
  
  # # Example request (Python)
    import requests
    url = '/ireporter.com/api/v1/red-flags/<int:incident_id>'
    payload = "{\"comment\": \"This is a new sample comment\"}"
    headers = {}
    response = requests.request('PATCH', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
    print(response.text)
    
  # # # Example response
    {
      “status” : 200, 
      “data” : [{
         “id” : Integer,  // red-flag record primary key
         “message” : “Updated red-flag record’s comment”
      }]
    }
    
# PATCH /ireporter.com/api/v1/red-flags/<int:incident_id>
  - Edit a location of a red-flag record a specific id
  
  - Headers
    Content-Type	application/json
    
  - Body raw (application/json)
    {"location": "New location"}
  
  - http://localhost:5000/ireporter.com/api/v1/red-flags/2
  
  # # Example request (Python)
    import requests
    url = '/ireporter.com/api/v1/red-flags/<int:incident_id>'
    payload = "{\"location\": \"New location\"}"
    headers = {}
    response = requests.request('PATCH', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
    print(response.text)
    
  # # # Example response
    {
      “status” : 200, 
      “data” : [{
         “id” : Integer,  // red-flag record primary key
         “message” : “Updated red-flag record’s location”
      }]
    }
    
# DELETE /ireporter.com/api/v1/red-flags/<int:incident_id>
  - Delete a red-flag record with a specific id
  
  - http://localhost:5000/ireporter.com/api/v1/red-flags/2
  
  # # Example request (Python)
    import requests
    url = '/ireporter.com/api/v1/red-flags/<int:incident_id>'
    headers = {}
    response = requests.request('DELETE', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
    print(response.text)
    
  # # # Example response
    {
      “status” : 200, 
      “data” : [{
        “id” : Integer,       // red-flag record primary key
        “message” :  “red-flag record has been deleted”
      }]
    }

