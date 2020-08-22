# CMPT 470 - Exercise 8 / Exercise 9

## About
Contacts is a web application where users can create, update and delete contacts. User will have to login / sign up to access contacts.

## Instructions
Assuming user already has python3, pip and docker installed.

#### To Run:
1. cd deployment
2. docker-compose build && docker-compose up
3. Go to http://localhost:8080/

#### To Terminate:
1. docker-compose down -v
2. docker system prune -f

## Inspiration
1. Flask tutorial - https://www.youtube.com/user/schafer5
2. Docker tutorial - https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/
