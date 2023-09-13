# Objective
Create a simple Restful API that support CRUD
oparation on a single resource called person, write an automate test script that to perform CRUD on the endpoint, use any database of one choice for managing the resource. provide an UML describing the structure of your database structure, Host your api and provide public access .

# Requirements

## REST API Development
evelop an API with endpoints for:
CREATE: Adding a new person.  => /api
READ: Fetching details of a person.  => /api/user_id
UPDATE: Modifying details of an existing person => /api/user_id
DELETE: Removing a person => /api/user_id
Ensure all interactions with the database are secure and free from common vulnerabilities (e.g., SQL injections).

## Database Modeling
Design the structure of your model using a UML modeling technology.

## Test Script
write a test script that automate the process of manaul testing of an api.

## Documentation
Write a detailed documentation of request/response data. instruction in settings up required environment to run the api.

## Host
Host the api and make it publicly available.

## API Documentation

### API Endpoints
| Method | Endpoint|
---------|---------|
| GET | http://hngx- 2.iyktech.tech/api/user_id |
| POST | http://hngx-2.iyktech.tech/api |
| PUT | http://hngx-2.iyktech.tech/api/user_id |
| DELETE | http://hngx-2.iyktech.tech/api/user_id |

#### GET Endpoint

##### Request
```
   GET: http://hngx-2.iyktech.tech/api/user_id => int
```

##### Response
```
   {
     id:int,
     name:str
   }
```
Content_Type: application/json
Status_Code: 200

##### HTTP Error
```
   {
     error:msg,
     status:code
   }
```

#### POST Endpoint

##### Request
```
   POST: http://hngx- 2.iyktech.tech/api
```
###### Request Body
```
  {
     name: str
  }
```
Content_Type: application/json

##### Response
```
   {
     id:int,
     name:str
   }
```
Content_Type: application/json
Status_Code: 201

##### HTTP Error
```
   {
     error:msg,
     status:code
   }
```

#### PUT Endpoint

##### Request
```
   PUT: http://hngx-2.iyktech.tech/api/user_id => int
```

##### Request Body
```
  {
    name: str
  }
```
Content_Type: application/json
##### Response
```
{
  id:int,
  name:str
}
```
Content_Type: application/json
Status_Code: 200
##### HTTP Error
```
{
  error:msg,
  status:code
}
```
#### DELETE Endpoint
##### Request
```
GET: http://hngx-2.iyktech.tech/api/user_id => int
```
##### Response
Status_Code: 200
##### HTTP Error
````
{
  error:msg,
  status:code
}
````
## Environment Setup
### tools
- flask
- flask_sqlachemy
- flask_migrate
- requests
- python-dotenv
To run this program you have to create Python virtual environment which can be down with the command below:
````
$ python3 -m venv venv
````
Activate the venv you created
with the cmd below:
On Linux:
````
$ source venv/bin/activate
```
On wins:
for Command Prompt:
```
path\to\venv\Scripts\activate
```
for PowerShell
```
path\to\venv\Scripts\Activate.ps1
```
install flask and it dependency
with is cmd:
```
pip install -r requirements.txt
```
## UML Link
[UML File](https://lucid.app/documents/view/3c6d8e0a-6a21-41c1-b796-ade78083b008)






