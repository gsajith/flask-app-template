# Sample Flask/Python app

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

## About Me
http://gsajith.com
