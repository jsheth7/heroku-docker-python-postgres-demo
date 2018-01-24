# heroku-docker-python-postgres-demo
Demo: Develop an app with Python, Postgres, and Docker and deploy it to Heroku

## Setup:

Install Docker
Rename env_sample.txt to .env and adjust values

## Local Development

docker-compose build
docker-compose up

Test: http://127.0.0.1:5000

## Deploy to Heroku

Log in to Heroku container system:

    heroku container:login

Create web container:

    heroku create

Add Postgres add on:

    heroku addons:create heroku-postgresql:hobby-dev

Deploy web container:

    heroku container:push web

Test:

    heroku open