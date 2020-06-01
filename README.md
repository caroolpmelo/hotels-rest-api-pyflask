# (:construction: Work In Progress) Hotels RESTful API in Flask

### This application is a study of Python 3 using Flask to make a RESTful API.

#### Implementations

- [x] Basic REST CRUD
- [ ] Database integration
- [ ] Token-Based Authentication
- [ ] Advanced queries
- [x] Deployed

Link: https://hotels-flask-api-caroolpmelo.herokuapp.com/

:warning: Be aware to run `pip install -r requirements.txt` in the root folder of the project to install requirements, otherwise the application may not work correctly.

#### Routes (currently available, more options and features to be added)

- GET `/` or `/hotels`
  - get all hotels
- GET `/hotels/{id}`
  - get hotel by id
- POST `/hotels/{id}`
  - create hotel with specified id
- PUT `/hotels/{id}`
  - update hotel with specified id (if not found, create one)
- DELETE `/hotels/{id}`
  - delete hotel with specified id
