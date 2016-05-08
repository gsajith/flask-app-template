# Sample Flask/Python app

## About the app
This is a simple template for quickly setting up and running a Python/Flask app. It's also got Bootstrap/JQuery/Fontawesome but you can delete that if you hate it.

This setup and app assumes cursory knowledge of:
- git
- Python

## Installation
```
# Initialize the git repo, name it whatever you want
$ git clone https://github.com/gsajith/flask-app-template your_directory_name
Cloning into 'your_directory_name'...
remote: Counting objects: 119, done.
remote: Compressing objects: 100% (98/98), done.
remote: Total 119 (delta 30), reused 99 (delta 15), pack-reused 0
Receiving objects: 100% (119/119), 562.64 KiB | 481.00 KiB/s, done.
Resolving deltas: 100% (30/30), done.
Checking connectivity... done.

# Move into the new git repo
$ cd your_directory_name

# Check git origin
$ git remote -v
origin	https://github.com/gsajith/flask-app-template (fetch)
origin	https://github.com/gsajith/flask-app-template (push)

# Set up new origin
$ git remote rm origin
$ git remote add origin https://github.com/your-github/link-to-your-github-repo
$ git remote -v
origin	https://github.com/your-github/link-to-your-github-repo (fetch)
origin	https://github.com/your-github/link-to-your-github-repo (push)

# Set up and activate virtual environment
$ virtualenv venv
$ source venv/bin/activate

# Install requirements, e.g. Flask, gunicorn
$ pip install -r requirements.txt
```


## Deployment
```
# Run the app, view it locally at address 127.0.0.1:8000
$ gunicorn app:app
[2016-05-07 18:50:20 -0700] [45752] [INFO] Starting gunicorn 19.3.0
[2016-05-07 18:50:20 -0700] [45752] [INFO] Listening at: http://127.0.0.1:8000 (45752)
[2016-05-07 18:50:20 -0700] [45752] [INFO] Using worker: sync
[2016-05-07 18:50:20 -0700] [45755] [INFO] Booting worker with pid: 45755

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
