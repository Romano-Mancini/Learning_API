# Flask API Test  

This repository is a test project for learning how to build APIs using Flask and practicing API requests with Postman.  

## Features
- Retreive questions from StackOverflow.com  
- Create, retrieve, and delete drinks using a simple REST API.  
- Uses Flask and Flask-SQLAlchemy with an SQLite database.  

## Setup  
1. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```
2. Set environment variables
   ```sh
   export FLASK_APP=newAPI_example.py  
   export FLASK_ENV=development  
   ```
3. Create and populate the database (optional):
   ```sh
   flask shell
   >>> db.create_all()
   >>> db.session.add(Drink(name:"test", description:"test"))
   >>> db.session.commit()
   ```
4. Testing with Postman
Use Postman to send GET, POST, and DELETE requests to test the API endpoints.

## Endpoints

- GET /drinks – Get all drinks
- GET /drink/\<id\> – Get a single drink by ID
- POST /drinks – Add a new drink
- DELETE /drinks/\<id\> – Delete a drink by ID
