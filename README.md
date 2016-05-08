# Sample Flask/Python app

## About the app
This is a simple template for quickly setting up and running a Python/Flask app.

This setup and app assumes cursory knowledge of:
- git
- Python

## Installation
```
# Initialize the git repo, name it whatever you want
git clone https://github.com/gsajith/flask-app-template your_directory_name

# Move into the new git repo
cd your_directory_name

# Set up and activate virtual environment
virtualenv venv
source venv/bin/activate

# Install requirements, e.g. Flask, gunicorn
pip install -r requirements.txt
```


## Deployment
```
# Run the app, view it locally at address 127.0.0.1:8000
gunicorn app:app


... (do work here) ...
... (you'll need to restart the gunicorn app every time you change any python files) ...
... (but usually not when you change template/css/js files) ...

# Deactivate virtual environment
deactivate
```

## Results
It should look like this:

![page 1](http://i.imgur.com/D0r7vrk.png)

and this:

![page 2](http://i.imgur.com/40lftb3.png)

## To-Do
- Add files and instructions about how to set up database and data models (psql probably)

## About Me
http://gsajith.com
