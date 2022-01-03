# DRFAngularToDo


git clone https://github.com/jasoliyanik1071/DRFAngularToDo.git
cd DjangoToDo


# Set up virtual environment
We do this so we install the packages locally instead of to your machine. Our project dependencies are specified in requirements.txt.

### Create Virtual Env.

```sh
virtualenv <virtual_env_name>
```

### Activate Virtual Env.
```sh
source <virtual_env_name>/bin/activate
```

### Clone this Django ToDo application
```sh
git clone https://github.com/jasoliyanik1071/DRFAngularToDo.git 
```

### Install Requirements
```sh
pip install -r requirements.txt
```

### DB related Operations
```sh
./manage.py makemigrations
```
```sh
./manage.py migrate
```

### Launch server
```sh
./manage.py runserver 0:8000
```

This sets up our database and starts the server. Go to localhost:8000. Now angular and drf play nicely

## Need to Change below params from the settings configuration file which if located under ToDoApp ==> settings.py and add your email and password to send email notification
```sh
EMAIL_HOST_USER = "dummy@gmail.com"
EMAIL_HOST_PASSWORD = "dummy@gmail.com"
```
