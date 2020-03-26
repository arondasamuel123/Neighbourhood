# Neighbourhood API
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Description
This is an API backend created for Django Independent Project week 4. This API makes use of Django rest framework, as well as JWT Authentication using Django rest framework. This project shows the use of APIViews and serializers and the two work together to build a REST API. 


## Author

Samuel Aronda


## DB diagram
![Neighborhood (2)](https://user-images.githubusercontent.com/31355212/77662118-84108080-6f8c-11ea-9f48-02eb8194fc8d.png)



# Installation

## Clone
    
```bash
    git clone https://github.com/arondasamuel123/AwwwardsClone.git
    
```
##  Create virtual environment
```bash
    python3.6 -m venv --without-pip virtual
    
```
## Activate virtual and install requirements.txt
```bash
   $ source virtual/bin/activate
   $ pip install - requirements.txt
    
```
## Run initial migration
```bash
   $ python3.6 manage.py makemigrations hood
   $ python3.6 manage.py migrate
    
```


## Run app
```bash
   $ python3 manage.py runserver
    
```

## Test class

```bash
    $ python3 manage.py test
```
## API Endpoints
    POST /api/user- Sign up users
    POST /api/token/- Login users
    POST /api/v1/create_hood - Create Neighbourhood
    GET /api/v1/hoods - View all Neighbourhoods
    GET /api/v1/view_hood/<int:pk> - View specific Neighbourhood
    POST /api/v1/post- Create a blog post
    POST /api/v1/create_business/<int:pk>- Create a business for a specific neighbourhood
    GET /api/v1/create_business/<int:pk>- View all business in specific neighbourhood
    POST /api/v1/create_dept/<int:pk>- Create departments for a specific neighbourhood
    GET  /api/v1/create_dept/<int:pk>- View departments in specific neighbourhood
    PUT  api/v1/profile/<int:pk>/<int:id> - Update user profile






## Known Bugs


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Technologies Used
    Django
    PostgreSQL
    Django Rest Framework




