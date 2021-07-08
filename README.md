# Reseller-api
![#](https://img.shields.io/badge/python-3.7.9-blue.svg)
![#](https://img.shields.io/badge/flask-2.0.1-blue.svg) 
![#](https://img.shields.io/badge/sqlalchemy-1.4.20-blue.svg) 
![#](https://img.shields.io/badge/alembic-1.6.5-blue.svg) 
![#](https://img.shields.io/badge/docker-20.10.7-blue.svg)
![#](https://img.shields.io/badge/docker_compose-1.29.2-blue.svg)

## Application to register resellers and purchases.

### Features
- [X] Token authentication 
- [X] Register Reseller
- [X] Register Purchases
- [X] Edit Purchases
- [X] List Purchases  
- [X] Cashback calculation

### Requirements:
* [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [docker-compose](https://docs.docker.com/compose/install/)

### Tools:
* [Postman](https://www.postman.com/downloads/)

### Install:
- Clone the project
```sh
git clone https://github.com/rdmsilva/reseller-api.git
```

### Run docker


```sh
docker-compose build && docker-compose up 
```

### Postman
Import the collection in folder:

    <project>/postman/Reseller-API.postman_collection.json


## RUN Tests

    docker exec -it reseller-api_app_1 ./cover.sh

## REST API
### New Reseller

---

`POST /v1/resellers`

All data fields are required.

    curl --location --request POST 'localhost:5000/v1/resellers' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "data": {
            "cpf": 12345678900,
            "name": "Rafael Revendedor",
            "email": "rafael-revendedor@hotmail.com",
            "password": "123456"
        }
    }'

### Responses

#### Success:
- Code: 201
- Content:
```json
{
  "id": 1,
  "msg": "saved"
}
```

#### Error:
- Code: 400 
- Content:
```json
{
  "msg": "{{error message}}"
}
```


### Authentication

---
`POST /v1/auth`

Baisc Auth is required in header.

    curl --user 12345678900:123456 --location --request POST 'localhost:5000/v1/auth'

### Responses

#### Success:
- Code: 200
- Content:
```json
{
  "id": 1, 
  "token": "{{token}}"
}
```

#### Error:
- Code: 400 | 401
- Content:
```json
{
  "msg": "{{error message}}"
}
```


### Cashback

---
`POST /v1/resellers/<reseller_id>/cashback`

Bearer token and reseller_id are requrired.

    curl --location --request GET 'localhost:5000/v1/resellers/1/cashback' \
    --header 'Authorization: Bearer {{token}}'

#### Success:
- Code: 200
- Content:
```json
{
    "credit": "<<int:credit>>"
}
```

#### Error:
- Code: 400 | 401 | 503
- Content:
```json
{
  "msg": "{{error message}}"
}
```


### New Purchase

---
`POST /v1/purchases`

Bearer token and all data fields are required.

    curl --location --request POST 'localhost:5000/v1/purchases' \
    --header 'Authorization: Bearer {{token}}' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "data": {
            "code": "b111",
            "value": 999.00,
            "date": "2021-07-06",
            "cpf": "12345678900"
        }
    }'

#### Success:
- Code: 201
- Content:
```json
{
    "id": 1,
    "msg": "saved"
}
```

#### Error:
- Code: 400 | 401
- Content:
```json
{
  "msg": "{{error message}}"
}
```


### List Purchases

---
`GET /v1/purchases`

Bearer token is required.

    curl --location --request GET 'localhost:5000/v1/purchases' --header 'Authorization: Bearer {{token}}'

#### Success:
- Code: 200
- Content:
```json
[
    {
        "cashback": 30.0,
        "code": "b111",
        "date": "2021-07-06",
        "percent": 10,
        "status": "Em validação",
        "value": 300.0
    }
]
```

#### Error:
- Code: 400 | 401
- Content:
```json
{
  "msg": "{{error message}}"
}
```


### Edit Purchase

---
`PUT /v1/purchases/<purchase_id>`

Bearer token and purchase id are required.

    curl --location --request PUT 'localhost:5000/v1/purchases/1' \
    --header 'Authorization: Bearer {{token}}' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "data": {
            "value": 300.0
        }
    }'

#### Success:
- Code: 200
- Content:
```json
{
    "code": "b111",
    "date": "2021-07-06",
    "status": "Em validação",
    "value": 300.0
}
```

#### Error:
- Code: 400 | 401
- Content:
```json
{
  "msg": "{{error message}}"
}
```


### Delete Purchase

---
`DELETE /v1/purchases/<purchase_id>`

Bearer token and purchase id are required.

    curl --location --request DELETE 'localhost:5000/v1/purchases/1' \
    --header 'Authorization: Bearer {{token}}'

#### Success:
- Code: 200
- Content:
```json
{
    "msg": "purchase deleted"
}
```

#### Error:
- Code: 400 | 401
- Content:
```json
{
  "msg": "{{error message}}"
}
```

### Author
#### [![Linkedin Badge](https://img.shields.io/badge/-Rafael_Dantas-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/rafael-dantas-18142291/)](https://www.linkedin.com/in/rafael-dantas-18142291/)
