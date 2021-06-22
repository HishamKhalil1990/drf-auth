# drf-auth
In this we project I made an API that uses JWT Authentication.
## Getting started
* Clone the repo -> `git clone git@github.com:HishamKhalil1990/drf-auth.git`
* Run docker-compose -> `docker-compose up`
* Migrate to database -> `docker-compose run web python manage.py migrate`
* Run the server -> `docker-compose run web python manage.py runserver`
* all data are persisted 
## Testing
* Use httpie to get the access token `http :8000/api/token/ username=<username> password=<password>`
* Use the token to access the data `http :8000/api/v1/1/ 'Authorization:Bearer <access-token>'`
## ChangeLog
* First commit - README.md
* Second commit - basic django setting file
* Third commit - the app is ready
## Pull Request
[Pull Request](https://github.com/HishamKhalil1990/drf-auth/pull/1)