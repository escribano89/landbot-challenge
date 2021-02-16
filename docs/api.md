# Landbot API

## Signup

**Request**:

`POST` `http://localhost:8000/api/users/`

Parameters:

Name       | Type   | Required |
-----------|--------|----------|
first_name | string | Yes      |
email      | string | Yes      |
phone      | string | Yes      |
origin     | string | Yes      |


```json
Content-Type application/json
201 Created

{
    "first_name": "test",
    "email": "test@test.com",
    "phone": "+41524204242",
    "origin": "landbot",
}
```

## Assistance Request ##

**Request**:

`POST` `http://localhost:8000/api/users/assistance/`

Parameters:

Name       | Type   | Required |
-----------|--------|----------|
topic      | string | Yes      |
email      | string | Yes      |


```json
Content-Type application/json
200 OK

{}
```