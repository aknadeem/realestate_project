# Realestate Project with Django

A Dockerized real estate listings website built with `Docker` `python` `django` `bootstrap` `javascript` `Jquery` `Postgresql`.

## How to run this project

1. ### Clone the project

## if you want to run this project on docker
*Make sure docker is installed on your machine if not installed it from here [Docker](https://docs.docker.com/get-docker/)*
- **Make sure you are in realestate_project folder**
- Build an image from a Dockerfile

`docker-compose build`

- starts the containers

`docker-compose up`

2. **Make sure you are in realestate_project folder**

3. Install all dependencies

`pip install -r requirements.txt`

4. **Create Database in postgresql if you have postgresql installed on your machine if not install it**

`CREATE DATABASE btredb;`

5. **Run Migrations**

`python manage.py makemigrations`
`python manage.py migrate`

6. **Run Server**

`python manage.py runserver`



