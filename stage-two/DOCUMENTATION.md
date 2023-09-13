# API Documentation

## API Endpoints
| Method | Endpoint|
---------|---------|
| GET | http://hngx-2.iyktech.tech/api/user_id |
| POST | http://hngx-2.iyktech.tech/api |
| PUT | http://hngx-2.iyktech.tech/api/user_id |
| DELETE | http://hngx-2.iyktech.tech/api/user_id |

### GET Endpoint

#### Request
```
   GET:http://hngx-2.iyktech.tech/api/user_id => int
```

#### Response
```
   {
     id:int,
     name:str
   }
```
Content_Type: application/json
Status_Code: 200

#### HTTP Error
```
   {
     error:msg,
     status:code
   }
```

### POST Endpoint

#### Request
```
   POST:http://hngx- 2.iyktech.tech/api
```
##### Request Body
```
  {
     name: str
  }
```
Content_Type: application/json

#### Response
```
   {
     id:int,
     name:str
   }
```
Content_Type: application/json
Status_Code: 201

#### HTTP Error
```
   {
     error:msg,
     status:code
   }
```

### PUT Endpoint

#### Request
```
   PUT:http://hngx-2.iyktech.tech/api/user_id => int
```

#### Request Body
```
  {
    name: str
  }
```
Content_Type: application/json
#### Response
```
{
  id:int,
  name:str
}
```
Content_Type: application/json
Status_Code: 200
#### HTTP Error
```
{
  error:msg,
  status:code
}
```
### DELETE Endpoint
#### Request
```
DELETE:http://hngx-2.iyktech.tech/api/user_id => int
```
#### Response
Status_Code: 200
#### HTTP Error
```
{
  error:msg,
  status:code
}
```
# Environment Setup
## tools
- flask
- flask_sqlachemy
- flask_migrate
- requests
- python-dotenv
To run this program you have to create Python virtual environment which can be down with the command below:
```
$ python3 -m venv venv
```
Activate the venv you created
with the cmd below:
On Linux:
```
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

